"""
============================================================================
 智能骑行头盔系统 - 版本二 (v2.0)
 功能：基础感知 + 五状态碰撞检测状态机 + 30秒二次确认 + MQTT SOS上报
 硬件：移远 QuecPython 开发板 + 板载传感器 + 蜂鸣器 + 按键 + LCD
 作者：竞赛团队
 日期：2026-07-02
============================================================================
 新增模块（相比 v1）：
   - CollisionDetector: 五状态有限状态机碰撞检测
   - BuzzerHandler:     蜂鸣器声光报警
   - ButtonHandler:     按键中断（200ms消抖，用于取消SOS）
   - LcdHandler:        LCD 屏幕显示（倒计时/状态）
   - 三线程并发架构:    传感器线程 + 碰撞检测线程 + 通信线程
============================================================================
 依赖例程：
   imu.py   - LIS2DH12 三轴加速度计
   aht20.py - AHT20 温湿度传感器
   ldr.py   - 光敏电阻 ADC 读取
   gnss.py  - GNSS 定位模块
   mqtt.py  - MQTT 通信
   lcd.py   - ST7735 LCD 显示
   pin.py   - GPIO 外部中断 + 防抖
   thread.py - _thread 多线程
   mutithread.py - 互斥锁同步
============================================================================
"""

# ==================== 标准库导入 ====================
import machine     # 硬件引脚、I2C、ADC 等
import time        # 延时、时间戳
import json        # JSON 序列化（用于 MQTT 报文）
import sys         # 系统退出
import tls         # TLS 加密上下文
import _thread     # 多线程模块
from collections import OrderedDict  # 有序字典

# ==================== 第三方库导入 ====================
from lis2dh12 import LIS2DH12     # 加速度计驱动
from ahtx0 import AHT20           # 温湿度传感器驱动
from umqtt.robust import MQTTClient  # MQTT 客户端
from st7735 import LCD            # ST7735 LCD 驱动

# ==================== 板载硬件常量 ====================

# ADC 通道：光敏电阻
LDR_ADC_PIN = 'C5'

# I2C 总线
I2C_BUS = 1
I2C_FREQ = 400000

# SPI 总线（LCD）
SPI_BUS = 1
SPI_BAUDRATE = 20000000
LCD_DC_PIN = 'F12'
LCD_CS_PIN = 'D14'

# 板载 LED（用于状态指示，无蜂鸣器时替代声光提示）
LED_PIN = 'LED_BLUE'
# 板载按键（用于取消 SOS）
SW_PIN  = 'SW'


# ====================================================================
# 第一部分：系统配置
# ====================================================================

class Config:
    """系统配置参数"""

    # ------------------------------------------------------------------
    # MQTT 服务器配置
    # ------------------------------------------------------------------
    MQTT_BROKER   = '172.188.83.251'
    MQTT_PORT     = 43719
    MQTT_USER     = 'quectel'
    MQTT_PASSWORD = '12345678'
    MQTT_CLIENT_ID = 'helmet_v2_001'
    MQTT_KEEPALIVE = 60

    # ------------------------------------------------------------------
    # TLS 证书文件路径
    # ------------------------------------------------------------------
    TLS_CA_PATH   = '/flash/connectlab_rsa_ca.cer'
    TLS_CERT_PATH = '/flash/connectlab_rsa_client_tmp.cer'
    TLS_KEY_PATH  = '/flash/connectlab_rsa_client_tmp.key'

    # ------------------------------------------------------------------
    # MQTT 主题
    # ------------------------------------------------------------------
    TOPIC_SENSOR  = b'/helmet/v2/sensor'    # 传感器数据上报
    TOPIC_SOS     = b'/helmet/v2/sos'        # SOS 告警主题

    # ------------------------------------------------------------------
    # 采样周期
    # ------------------------------------------------------------------
    SENSOR_INTERVAL   = 0.1    # 加速度计 100ms（10Hz）
    DETECT_INTERVAL   = 0.05   # 碰撞检测轮询 50ms
    GNSS_INTERVAL     = 1.0    # GNSS 更新 1s
    ENV_INTERVAL      = 2.0    # 环境数据上传 2s

    # ------------------------------------------------------------------
    # 碰撞检测阈值
    # ------------------------------------------------------------------
    FREE_FALL_THRESHOLD = 0.5   # 失重阈值（g）
    FREE_FALL_HOLD_MS   = 100  # 失重持续判定时间（毫秒）
    IMPACT_THRESHOLD    = 3.5  # 碰撞冲击阈值（g）

    # ------------------------------------------------------------------
    # 异常事件检测阈值（拿起 / 自由下落）
    # ------------------------------------------------------------------
    PICKED_UP_THRESHOLD  = 1.3  # 拿起判定阈值（g）
    FREEFALL_THRESHOLD   = 0.5  # 自由下落判定阈值（g）
    NORMAL_LOW           = 0.7  # 正常状态下限（g）
    NORMAL_HIGH          = 1.3  # 正常状态上限（g）

    # ------------------------------------------------------------------
    # SOS 配置
    # ------------------------------------------------------------------
    SOS_COUNTDOWN_SEC  = 30    # 二次确认倒计时秒数
    BUZZER_BEEP_INTERVAL = 0.5 # 蜂鸣器鸣叫间隔（秒）


# ====================================================================
# 第二部分：工具函数
# ====================================================================

def log(tag, message):
    """日志输出"""
    print('[{}] [{}] {}'.format(int(time.time()), tag, message))


def read_cert_file(filepath):
    """读取 TLS 证书文件"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            log('TLS', '成功读取证书文件: {}'.format(filepath))
            return content
    except FileNotFoundError:
        log('TLS', '证书文件不存在: {}'.format(filepath))
        return None
    except PermissionError:
        log('TLS', '无权限读取证书文件: {}'.format(filepath))
        return None
    except Exception:
        try:
            with open(filepath, 'rb') as f:
                content = f.read()
                try:
                    content = content.decode('utf-8')
                except Exception:
                    pass
                log('TLS', '成功读取证书文件(二进制): {}'.format(filepath))
                return content
        except Exception as e:
            log('TLS', '读取证书文件失败 {}: {}'.format(filepath, e))
            return None


# ====================================================================
# 第三部分：传感器管理模块（同 v1）
# ====================================================================

class SensorManager:
    """
    传感器管理器
    统一管理 LIS2DH12 加速度计、AHT20 温湿度传感器、光敏电阻 ADC
    """

    def __init__(self):
        """初始化 I2C 总线和所有板载传感器"""
        # I2C 总线互斥锁（多线程安全）
        self.i2c_lock = _thread.allocate_lock()

        # I2C 总线
        try:
            self.i2c = machine.I2C(I2C_BUS, freq=I2C_FREQ)
            log('I2C', 'I2C 总线初始化完成，频率 {}Hz'.format(I2C_FREQ))
        except Exception as e:
            log('I2C', 'I2C 总线初始化失败: {}'.format(e))
            self.i2c = None

        # LIS2DH12 加速度计
        try:
            self.lis2dh = LIS2DH12(self.i2c) if self.i2c else None
            log('LIS2DH12', '加速度计初始化完成')
        except Exception as e:
            log('LIS2DH12', '加速度计初始化失败: {}'.format(e))
            self.lis2dh = None

        # AHT20 温湿度
        try:
            self.aht20 = AHT20(self.i2c) if self.i2c else None
            log('AHT20', '温湿度传感器初始化完成')
        except Exception as e:
            log('AHT20', '温湿度传感器初始化失败: {}'.format(e))
            self.aht20 = None

        # 光敏 ADC
        try:
            self.adc = machine.ADC(machine.Pin(LDR_ADC_PIN))
            log('ADC', '光敏电阻 ADC 初始化完成，引脚 {}'.format(LDR_ADC_PIN))
        except Exception as e:
            log('ADC', '光敏电阻 ADC 初始化失败: {}'.format(e))
            self.adc = None

        # I2C 设备扫描
        if self.i2c:
            try:
                devices = self.i2c.scan()
                log('I2C', '扫描到设备: {}'.format([hex(d) for d in devices]))
            except Exception:
                pass

    # ------------------------------------------------------------------
    # 加速度
    # ------------------------------------------------------------------

    def read_acceleration(self):
        """
        读取三轴加速度（I2C 互斥，线程安全）
        :return: {'x': float, 'y': float, 'z': float} 单位 m/s²
        """
        result = {'x': 0.0, 'y': 0.0, 'z': 0.0}
        if self.lis2dh is None:
            return result
        try:
            self.i2c_lock.acquire()
            try:
                acc_x, acc_y, acc_z = self.lis2dh.acceleration
            finally:
                self.i2c_lock.release()
            result['x'] = round(acc_x, 3)
            result['y'] = round(acc_y, 3)
            result['z'] = round(acc_z, 3)
        except Exception as e:
            log('LIS2DH12', '读取加速度失败: {}'.format(e))
        return result

    def calc_acc_total(self, acc):
        """
        计算三轴合力幅值（单位：g）
        :param acc: 加速度字典 {'x', 'y', 'z'}
        :return:    合力幅值（g）
        """
        total = (acc['x']**2 + acc['y']**2 + acc['z']**2) ** 0.5
        return round(total / 9.8, 2)

    # ------------------------------------------------------------------
    # 温湿度
    # ------------------------------------------------------------------

    def read_temperature_humidity(self):
        """
        读取温湿度（I2C 互斥，线程安全）
        :return: {'temp': float, 'humidity': float} 或 None
        """
        if self.aht20 is None:
            return None
        try:
            self.i2c_lock.acquire()
            try:
                temp = self.aht20.temperature
                hum  = self.aht20.relative_humidity
            finally:
                self.i2c_lock.release()
            return {'temp': round(temp, 1), 'humidity': round(hum, 1)}
        except Exception as e:
            log('AHT20', '读取温湿度失败: {}'.format(e))
            return None

    # ------------------------------------------------------------------
    # 光照
    # ------------------------------------------------------------------

    def read_light(self):
        """
        读取光敏电压
        :return: 电压值（V）
        """
        if self.adc is None:
            return 0.0
        try:
            raw_16bit = self.adc.read_u16()
            raw_12bit = raw_16bit >> 4
            return round((raw_12bit * 3.3) / 4095.0, 3)
        except Exception as e:
            log('ADC', '读取光敏电压失败: {}'.format(e))
            return 0.0


# ====================================================================
# 第四部分：GNSS 定位管理模块（同 v1）
# ====================================================================

class GnssManager:
    """GNSS 定位管理器"""

    def __init__(self):
        import quectel
        self.gnss = None
        self.valid = False
        self.latitude  = 0.0
        self.longitude = 0.0
        self.speed     = 0.0
        self.altitude  = 0.0
        self.satellites = 0
        try:
            self.gnss = quectel.GNSS()
            log('GNSS', 'GNSS 模块对象创建成功')
        except Exception as e:
            log('GNSS', 'GNSS 模块创建失败: {}'.format(e))
            self.gnss = None

    def start(self):
        """启动 GNSS 定位"""
        if self.gnss is None:
            return False
        try:
            if self.gnss.start():
                log('GNSS', '定位模块启动成功，等待卫星信号...')
                return True
            log('GNSS', '定位模块启动失败')
            return False
        except Exception as e:
            log('GNSS', '定位模块启动异常: {}'.format(e))
            return False

    def stop(self):
        """停止 GNSS"""
        if self.gnss:
            try:
                self.gnss.stop()
                log('GNSS', '定位模块已停止')
            except Exception as e:
                log('GNSS', '定位模块停止失败: {}'.format(e))

    def update(self):
        """更新一次定位数据"""
        if self.gnss is None:
            self.valid = False
            return
        try:
            loc = self.gnss.get_location()
            if loc:
                self.latitude   = loc.get('latitude', 0.0)
                self.longitude  = loc.get('longitude', 0.0)
                self.speed      = loc.get('speed', 0.0)
                self.altitude   = loc.get('altitude', 0.0)
                self.satellites = loc.get('satellites', 0)
                self.valid = True
            else:
                self.valid = False
        except Exception as e:
            log('GNSS', '定位数据更新失败: {}'.format(e))
            self.valid = False


# ====================================================================
# 第五部分：MQTT 通信管理模块（同 v1，增加 SOS 发布）
# ====================================================================

class MqttManager:
    """MQTT 通信管理器"""

    def __init__(self):
        self.client    = None
        self.connected = False

    def start_network(self):
        """启动 4G 蜂窝网络"""
        from quectel import Network
        try:
            net = Network()
            net.init()
            log('NET', '4G 模块初始化完成')
            sim_status = net.query_usim()
            log('NET', 'SIM 卡状态: {}'.format(sim_status))
            net.attach()
            log('NET', '4G 网络附着完成')
            return True
        except Exception as e:
            log('NET', '4G 网络初始化失败: {}'.format(e))
            return False

    def connect(self):
        """连接 MQTT 服务器（TLS 加密）"""
        # 读取证书
        ca   = read_cert_file(Config.TLS_CA_PATH)
        cert = read_cert_file(Config.TLS_CERT_PATH)
        key  = read_cert_file(Config.TLS_KEY_PATH)
        if not ca or not cert or not key:
            log('MQTT', 'TLS 证书读取不完整')
            return False

        # 创建 TLS 上下文
        try:
            context = tls.SSLContext(tls.PROTOCOL_TLS_CLIENT)
            context.verify_mode = tls.CERT_REQUIRED
            if isinstance(ca, str):    ca = ca.encode('utf-8')
            if isinstance(cert, str):  cert = cert.encode('utf-8')
            if isinstance(key, str):   key = key.encode('utf-8')
            context.load_verify_locations(ca)
            context.load_cert_chain(cert, key)
            log('TLS', 'SSL 上下文配置成功')
        except Exception as e:
            log('TLS', 'SSL 上下文配置失败: {}'.format(e))
            return False

        # 创建客户端
        try:
            self.client = MQTTClient(
                client_id  = Config.MQTT_CLIENT_ID,
                server     = Config.MQTT_BROKER,
                port       = Config.MQTT_PORT,
                user       = Config.MQTT_USER,
                password   = Config.MQTT_PASSWORD,
                keepalive  = Config.MQTT_KEEPALIVE,
                ssl        = context
            )
            self.client.set_callback(self._on_message)
            log('MQTT', '配置: {}:{}  TLS  user={}'.format(
                Config.MQTT_BROKER, Config.MQTT_PORT, Config.MQTT_USER))
            log('MQTT', '正在连接 {}:{}...'.format(
                Config.MQTT_BROKER, Config.MQTT_PORT))
            self.client.connect()
            self.connected = True
            log('MQTT', 'MQTT 连接成功！')
            return True
        except Exception as e:
            log('MQTT', 'MQTT 连接失败: {}'.format(e))
            self.connected = False
            return False

    def disconnect(self):
        """断开 MQTT"""
        if self.client and self.connected:
            try:
                self.client.disconnect()
                self.connected = False
                log('MQTT', 'MQTT 连接已断开')
            except Exception as e:
                log('MQTT', 'MQTT 断开失败: {}'.format(e))

    def publish(self, topic, payload):
        """
        发布消息
        :param topic:   主题（bytes）
        :param payload: 内容（str 或 bytes）
        :return:        True/False
        """
        if not self.connected or self.client is None:
            return False
        try:
            if isinstance(payload, str):
                payload = payload.encode()
            self.client.publish(topic, payload)
            return True
        except Exception as e:
            log('MQTT', '消息发布失败: {}'.format(e))
            self.connected = False
            return False

    def check_msg(self):
        """检查下行消息（非阻塞）"""
        if self.client and self.connected:
            try:
                self.client.check_msg()
            except Exception as e:
                log('MQTT', '消息检查异常: {}'.format(e))
                self.connected = False

    @staticmethod
    def _on_message(topic, msg):
        """MQTT 消息回调"""
        log('MQTT', '收到下行消息 [{}]: {}'.format(topic.decode(), msg.decode()))


# ====================================================================
# 第六部分：蜂鸣器管理模块（v2 新增）
# ====================================================================

class BuzzerHandler:
    """
    蜂鸣器管理器
    用于 SOS 倒计时期间声光提示
    """

    def __init__(self):
        """
        初始化蜂鸣器（无外接硬件时不可用，改用 LED 指示）
        """
        self.available = False
        log('BUZZER', '无外接蜂鸣器（使用板载 LED 替代声光提示）')
        # 初始化板载 LED 用于视觉提示
        try:
            self.led = machine.Pin(LED_PIN, machine.Pin.OUT, machine.Pin.PULL_NONE)
            self.led.value(0)
            self.led_available = True
        except Exception:
            self.led_available = False

    def on(self):
        """LED 常亮"""
        if self.led_available:
            self.led.value(1)

    def off(self):
        """LED 熄灭"""
        if self.led_available:
            self.led.value(0)

    def beep_once(self, duration_ms=100):
        """LED 闪烁一次（替代蜂鸣器鸣叫）"""
        if self.led_available:
            self.led.value(1)
            time.sleep_ms(duration_ms)
            self.led.value(0)


# ====================================================================
# 第七部分：按键管理模块（v2 新增）
# ====================================================================

class ButtonHandler:
    """
    按键处理器（GPIO 外部中断 + 200ms 软件消抖）
    用于用户在 SOS 倒计时期间取消告警
    """

    # 按键中断回调函数（由外部设置）
    on_press = None

    def __init__(self, pin=SW_PIN):
        """
        初始化板载按键（上升沿中断 + 200ms 软件消抖）
        :param pin: 按键引脚名（如 'SW'）
        """
        self.last_press_time = 0       # 上次按键时间（防抖）
        self.debounce_ms = 200         # 消抖时间 200ms
        self.pressed = False           # 是否检测到有效按键

        try:
            self.pin = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN)
            # 注册上升沿中断（SW 按键按下为高电平）
            self.pin.irq(
                trigger = machine.Pin.IRQ_RISING,
                handler = self._irq_handler
            )
            log('BUTTON', '按键初始化完成（下降沿中断，200ms 软件消抖）')
        except Exception as e:
            log('BUTTON', '按键初始化失败: {}'.format(e))

    def _irq_handler(self, pin_obj):
        """
        按键中断服务程序（ISR）
        200ms 软件消抖：两次触发间隔小于 200ms 则忽略
        """
        current_ms = time.ticks_ms()
        if current_ms - self.last_press_time > self.debounce_ms:
            self.last_press_time = current_ms
            self.pressed = True
            # 执行外部回调（如果有）
            if self.on_press:
                try:
                    self.on_press()
                except Exception:
                    pass

    def is_pressed(self):
        """
        检测是否有按键按下并清除标志（一次性读取）
        :return: True 表示检测到有效按键
        """
        if self.pressed:
            self.pressed = False
            return True
        return False


# ====================================================================
# 第七部分：LCD 显示管理模块（v2 新增）
# ====================================================================

class LcdHandler:
    """
    LCD 屏幕管理器
    用于显示系统状态和 SOS 倒计时
    """

    def __init__(self):
        """
        初始化 LCD 屏幕（ST7735）
        使用 SPI1，F12/DC，D14/CS
        """
        self.lcd = None
        try:
            spi = machine.SPI(SPI_BUS, baudrate=SPI_BAUDRATE,
                              polarity=0, phase=0)
            self.lcd = LCD(spi, dc_pin=LCD_DC_PIN, cs_pin=LCD_CS_PIN)
            self.lcd.set_rotation(1)
            self.lcd.fill_screen(self.lcd.BLACK)
            log('LCD', 'LCD 初始化完成（ST7735, 160x80）')
        except Exception as e:
            log('LCD', 'LCD 初始化失败: {}'.format(e))

    def clear(self):
        """清屏（黑色）"""
        if self.lcd:
            try:
                self.lcd.fill_screen(self.lcd.BLACK)
                self.lcd.flush()
            except Exception:
                pass

    def show_status(self, text, line=0):
        """
        显示一行状态文本
        :param text: 显示内容（最多 20 字符）
        :param line: 行号（0~4，每行 16px）
        """
        if self.lcd is None:
            return
        try:
            color = self.lcd.WHITE
            self.lcd.set_color(color, self.lcd.BLACK)
            self.lcd.show_text(2, 2 + line * 16, text[:20])
            self.lcd.flush()
        except Exception:
            pass

    def show_countdown(self, seconds):
        """
        显示 SOS 倒计时（大字 + 颜色变化）
        :param seconds: 剩余秒数
        """
        if self.lcd is None:
            return
        try:
            # 清屏
            self.lcd.fill_screen(self.lcd.BLACK)

            # 倒计时数字用红色
            self.lcd.set_color(self.lcd.RED, self.lcd.BLACK)

            # 显示 SOS 标题
            if seconds > 0:
                self.lcd.show_text(2, 2, 'SOS in {}s'.format(seconds))
                self.lcd.show_text(2, 20, 'Press KEY cancel')
            else:
                self.lcd.show_text(2, 2, '=== SOS ===')
                self.lcd.show_text(2, 20, 'Sending alert...')

            # 显示状态（白色）
            self.lcd.set_color(self.lcd.WHITE, self.lcd.BLACK)
            self.lcd.show_text(2, 40, 'Helmet v2.0')

            self.lcd.flush()
        except Exception:
            pass


# ====================================================================
# 第九部分：碰撞检测状态机（v2 新增 - 核心）
# ====================================================================

class CollisionState:
    """
    五状态有限状态机的所有状态常量
    论文对应：IDLE → WEIGHTLESS → IMPACT → POST_ACCIDENT → SOS_TRIGGERED
    """
    IDLE           = 0   # 空闲监测
    WEIGHTLESS     = 1   # 失重（合力≈0.5g，持续100ms）
    IMPACT         = 2   # 冲击（合力>3.5g）
    POST_ACCIDENT  = 3   # 伤后静止（30秒倒计时，等待取消）
    SOS_TRIGGERED  = 4   # SOS 已触发（已发送告警）


class CollisionDetector:
    """
    五状态碰撞检测有限状态机（FSM）
    状态流转：
      IDLE → (合力≈0.5g 持续100ms) → WEIGHTLESS
      WEIGHTLESS → (合力>3.5g) → IMPACT
      IMPACT → (合力回到正常) → POST_ACCIDENT
      POST_ACCIDENT → (30s倒计时归零) → SOS_TRIGGERED
      POST_ACCIDENT → (用户按键) → IDLE
      SOS_TRIGGERED → MQTT 发送完成 → IDLE
      任何状态 → (长时间正常) → IDLE
    """

    def __init__(self, buzzer=None, lcd=None, button=None, mqtt=None, gnss=None):
        """
        初始化状态机
        :param buzzer: BuzzerHandler 实例（用于报警提示）
        :param lcd:    LcdHandler 实例（用于显示倒计时）
        :param button: ButtonHandler 实例（用于取消SOS）
        :param mqtt:   MqttManager 实例（用于发送SOS）
        :param gnss:   GnssManager 实例（获取SOS中的GPS坐标）
        """
        self.state = CollisionState.IDLE
        self.lock = _thread.allocate_lock()  # 状态机锁（线程安全）

        # 外部模块引用
        self.buzzer = buzzer
        self.lcd    = lcd
        self.button = button
        self.mqtt   = mqtt
        self.gnss   = gnss

        # ---------- 失重检测 ----------
        self.freefall_start_time = None   # 进入失重状态的时间
        self.freefall_confirmed  = False  # 失重是否已确认（≥100ms）

        # ---------- 30秒倒计时 ----------
        self.countdown_start = None       # 倒计时开始时间
        self.countdown_remaining = 0       # 剩余秒数
        self.sos_sent = False             # SOS 是否已发送

        # ---------- 日志 ----------
        self.last_log_state = -1          # 上次记录的状态（防止重复日志）
        log('STATE', '碰撞检测状态机初始化完成（五状态FSM）')

    # ------------------------------------------------------------------
    # 线程安全操作
    # ------------------------------------------------------------------

    def get_state(self):
        """获取当前状态（线程安全）"""
        with self.lock:
            return self.state

    def set_state(self, new_state):
        """设置当前状态并打印日志（线程安全）"""
        with self.lock:
            old_state = self.state
            self.state = new_state
            state_names = [
                'IDLE', 'WEIGHTLESS', 'IMPACT',
                'POST_ACCIDENT', 'SOS_TRIGGERED'
            ]
            if new_state != old_state:
                log('STATE', '状态切换: {} → {}'.format(
                    state_names[old_state], state_names[new_state]))
            return old_state

    def reset_to_idle(self):
        """
        复位到 IDLE 状态
        可被按键中断回调调用
        """
        self.set_state(CollisionState.IDLE)
        self.freefall_start_time = None
        self.freefall_confirmed = False
        self.countdown_start = None
        self.countdown_remaining = 0
        self.sos_sent = False
        log('STATE', '复位到 IDLE 状态')

    # ------------------------------------------------------------------
    # 外部中断回调（按键取消）
    # ------------------------------------------------------------------

    def on_button_press(self):
        """
        按键按下回调
        在 POST_ACCIDENT 状态下按键则取消 SOS
        """
        state = self.get_state()
        if state == CollisionState.POST_ACCIDENT:
            log('BUTTON', '用户按下取消按键，SOS 已取消')
            # 关闭蜂鸣器/LED
            if self.buzzer:
                self.buzzer.beep_once(50)
            # 显示取消提示
            if self.lcd:
                self.lcd.show_status('SOS Cancelled', 0)
                self.lcd.show_status('Back to Normal', 1)
            # 复位状态机
            self.reset_to_idle()

    # ------------------------------------------------------------------
    # 主更新接口（外界每秒或每 50ms 调用一次）
    # ------------------------------------------------------------------

    def update(self, acc_total_g, current_time_ms):
        """
        状态机主更新函数（由碰撞检测线程调用）
        :param acc_total_g:    当前合力幅值（g）
        :param current_time_ms: 当前时间戳（毫秒）
        :return:               (state, countdown) 状态和倒计时
        """
        state = self.get_state()

        # ---------- 状态切换日志（防重复） ----------
        if state != self.last_log_state:
            self.last_log_state = state

        # =============================================================
        # 状态 0: IDLE → 监测失重
        # =============================================================
        if state == CollisionState.IDLE:
            self.sos_sent = False
            if acc_total_g < Config.FREE_FALL_THRESHOLD:
                # 检测到失重，记录开始时间
                if self.freefall_start_time is None:
                    self.freefall_start_time = current_time_ms
                    self.freefall_confirmed = False
                # 判断失重是否持续了足够时间
                elif not self.freefall_confirmed:
                    elapsed = current_time_ms - self.freefall_start_time
                    if elapsed >= Config.FREE_FALL_HOLD_MS:
                        self.freefall_confirmed = True
                        self.set_state(CollisionState.WEIGHTLESS)
            else:
                # 合力正常，重置失重计时
                self.freefall_start_time = None
                self.freefall_confirmed = False

        # =============================================================
        # 状态 1: WEIGHTLESS → 监测冲击
        # =============================================================
        elif state == CollisionState.WEIGHTLESS:
            if acc_total_g > Config.IMPACT_THRESHOLD:
                # 检测到冲击，进入冲撞状态
                self.set_state(CollisionState.IMPACT)
            elif acc_total_g > Config.FREE_FALL_THRESHOLD:
                # 合力恢复正常但没检测到冲击 → 回到 IDLE（颠簸误报）
                self.reset_to_idle()

        # =============================================================
        # 状态 2: IMPACT → 进入伤后静止倒计时
        # =============================================================
        elif state == CollisionState.IMPACT:
            # 等待合力回到正常范围（1g 附近）
            if 0.5 < acc_total_g < 2.0:
                # 进入事故后监测
                self.countdown_start = current_time_ms
                self.countdown_remaining = Config.SOS_COUNTDOWN_SEC
                self.set_state(CollisionState.POST_ACCIDENT)

                # 打开蜂鸣器提示
                if self.buzzer:
                    self.buzzer.beep_once(200)

                # LCD 显示倒计时
                if self.lcd:
                    self.lcd.show_countdown(self.countdown_remaining)

        # =============================================================
        # 状态 3: POST_ACCIDENT → 倒计时 → SOS
        # =============================================================
        elif state == CollisionState.POST_ACCIDENT:
            if self.countdown_start is None:
                self.reset_to_idle()
                return StateResult(state, 0)

            # 计算剩余秒数
            elapsed_ms = current_time_ms - self.countdown_start
            remaining = Config.SOS_COUNTDOWN_SEC - int(elapsed_ms / 1000)

            if remaining != self.countdown_remaining:
                # 倒计时变化，更新 LCD 和蜂鸣器
                self.countdown_remaining = remaining
                if remaining > 0:
                    if self.lcd:
                        self.lcd.show_countdown(remaining)
                    # 蜂鸣器间歇鸣叫
                    if self.buzzer:
                        self.buzzer.beep_once(80)

            if remaining <= 0:
                # 倒计时归零 → 触发 SOS
                self.set_state(CollisionState.SOS_TRIGGERED)
                self._send_sos_alert()
                if self.lcd:
                    self.lcd.show_countdown(0)
                if self.buzzer:
                    self.buzzer.beep_once(500)

        # =============================================================
        # 状态 4: SOS_TRIGGERED → 复位
        # =============================================================
        elif state == CollisionState.SOS_TRIGGERED:
            # SOS 已发送，等待人为复位
            # 一段时间后自动回到 IDLE
            if self.sos_sent:
                self.reset_to_idle()

        # 返回当前状态和倒计时
        return StateResult(self.get_state(), self.countdown_remaining)

    def _send_sos_alert(self):
        """
        发送 SOS 告警到 MQTT 服务器
        包含：GPS 坐标、时间戳、事件类型
        """
        if self.mqtt is None or not self.mqtt.connected:
            log('SOS', 'MQTT 不可用，无法发送 SOS')
            return

        try:
            # 构建 SOS 报文
            sos_data = OrderedDict()
            sos_data['type'] = 'SOS'
            sos_data['event'] = 'collision_detected'

            # GPS 坐标
            if self.gnss and self.gnss.valid:
                sos_data['lat'] = self.gnss.latitude
                sos_data['lon'] = self.gnss.longitude
                sos_data['speed'] = self.gnss.speed
            else:
                sos_data['lat'] = 0.0
                sos_data['lon'] = 0.0

            sos_data['timestamp'] = int(time.time())
            sos_data['status'] = 'emergency'

            payload = json.dumps(sos_data)
            log('SOS', '发送 SOS 告警: {}'.format(payload))

            # 发布到 SOS 主题
            self.mqtt.publish(Config.TOPIC_SOS, payload)
            self.sos_sent = True
            log('SOS', 'SOS 告警已发送！')

        except Exception as e:
            log('SOS', 'SOS 发送失败: {}'.format(e))


class StateResult:
    """状态机更新结果（用于线程间传递）"""

    def __init__(self, state, countdown):
        self.state = state
        self.countdown = countdown


# ====================================================================
# 第十部分：共享数据缓冲区（线程安全）
# ====================================================================

class SharedData:
    """
    线程间共享数据缓冲区
    使用互斥锁保护，避免数据竞争
    """

    def __init__(self):
        self.lock = _thread.allocate_lock()

        # 加速度数据（由传感器线程写入，检测线程读取）
        self.acc = {'x': 0.0, 'y': 0.0, 'z': 0.0}
        self.acc_total_g = 1.0

        # 环境数据（由传感器线程写入，通信线程读取）
        self.env_data = None
        self.light_v = 0.0

        # 系统状态（由检测线程写入，通信线程读取）
        self.state = CollisionState.IDLE
        self.sos_active = False
        self.sos_payload = None

    def update_acc(self, acc, acc_g):
        """更新加速度数据（线程安全）"""
        with self.lock:
            self.acc = acc
            self.acc_total_g = acc_g

    def get_acc(self):
        """读取加速度数据（线程安全）"""
        with self.lock:
            return self.acc, self.acc_total_g

    def update_env(self, env, light):
        """更新环境数据（线程安全）"""
        with self.lock:
            if env:
                self.env_data = env
            self.light_v = light

    def get_env(self):
        """读取环境数据（线程安全）"""
        with self.lock:
            return self.env_data, self.light_v

    def set_sos(self, payload=None):
        """设置 SOS 标志（线程安全）"""
        with self.lock:
            self.sos_active = True
            self.sos_payload = payload

    def clear_sos(self):
        """清除 SOS 标志（线程安全）"""
        with self.lock:
            self.sos_active = False
            self.sos_payload = None

    def has_sos(self):
        """检查是否有 SOS 需要发送（线程安全）"""
        with self.lock:
            return self.sos_active, self.sos_payload


# ====================================================================
# 第十一部分：系统主控制类
# ====================================================================

class HelmetSystem:
    """
    系统主控制器
    管理所有子模块的初始化与三线程并发运行
    """

    def __init__(self):
        log('SYSTEM', '=' * 50)
        log('SYSTEM', '智能骑行头盔系统 v2.0 启动')
        log('SYSTEM', '=' * 50)

        # ---------- 1. 初始化传感器 ----------
        self.sensor = SensorManager()

        # ---------- 2. 初始化 GNSS ----------
        self.gnss = GnssManager()
        self.gnss.start()

        # ---------- 3. 初始化 MQTT ----------
        self.mqtt = MqttManager()
        if self.mqtt.start_network():
            # 等待 NTP 时间同步完成（TLS 证书校验需要正确的系统时间）
            log('SYSTEM', '等待 NTP 时间同步...')
            for _ in range(10):  # 最多等 10 秒
                if int(time.time()) > 1700000000:  # 时间大于 2023 年即视为已同步
                    log('SYSTEM', 'NTP 时间同步完成')
                    break
                time.sleep(1)
            self.mqtt.connect()

        # ---------- 4. 初始化蜂鸣器、按键、LCD ----------
        self.buzzer = BuzzerHandler()
        self.button = ButtonHandler()
        self.lcd    = LcdHandler()
        if self.lcd.lcd:
            self.lcd.show_status('Helmet v2.0', 0)
            self.lcd.show_status('System Ready', 1)

        # ---------- 5. 初始化共享数据区 ----------
        self.shared = SharedData()

        # ---------- 6. 初始化碰撞检测状态机 ----------
        self.detector = CollisionDetector(
            buzzer=self.buzzer,
            lcd=self.lcd,
            button=self.button,
            mqtt=self.mqtt,
            gnss=self.gnss
        )

        # 注册按键回调（关联到状态机的取消处理）
        self.button.on_press = self.detector.on_button_press

        # ---------- 7. 运行标志 ----------
        self.running = True

        log('SYSTEM', '所有模块初始化完成，准备启动三线程并发框架')

    # ------------------------------------------------------------------
    # 线程 1：传感器采集线程（10Hz）
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # 线程 2：碰撞检测线程（50ms 轮询）
    # ------------------------------------------------------------------

    def detect_thread(self):
        """
        碰撞检测线程
        以 50ms 周期从共享缓冲区读取加速度数据
        驱动五状态有限状态机进行碰撞判别
        **注意：** 本线程不操作 I2C 总线，仅读取共享缓冲区，
                  I2C 传感器采集全部在主线程（comm_thread）中完成
        """
        log('THREAD', '碰撞检测线程已启动（50ms 轮询）')

        while self.running:
            try:
                # 读取加速度（来自共享缓冲区，非 I2C）
                acc, acc_g = self.shared.get_acc()

                # 获取当前时间（毫秒）
                now_ms = time.ticks_ms()

                # 更新状态机
                result = self.detector.update(acc_g, now_ms)

                # 如果触发 SOS，通过共享区通知通信线程
                if result.state == CollisionState.SOS_TRIGGERED:
                    self.shared.set_sos('emergency')

                time.sleep(Config.DETECT_INTERVAL)  # 50ms

            except Exception as e:
                log('THREAD', '碰撞检测线程异常: {}'.format(e))
                time.sleep(0.5)

        log('THREAD', '碰撞检测线程已退出')

    # ------------------------------------------------------------------
    # 主线程：通信线程
    # ------------------------------------------------------------------

    def comm_thread(self):
        """
        通信线程（主线程）
        负责：
          1. 每 100ms 采集加速度（I2C 在主线程中运行，避免子线程递归溢出）
          2. 每 1s 采集温湿度 + 光照 + GNSS
          3. 每 2s 上传传感器数据（加速度+温湿度+光照+GPS）
          4. 每 10s 发送心跳包
          5. 检测到 SOS 标志时立即发送告警
          6. 检查 MQTT 下行消息
        """
        log('THREAD', '通信/采集线程已启动（主线程，含 I2C 传感器读取）')
        last_acc_ms = 0
        last_env_time = 0
        last_upload_time = 0

        while self.running:
            try:
                now = time.time()
                now_ms = time.ticks_ms()

                # ============================================================
                # 1. 传感器采集（主线程运行，子线程不碰 I2C）
                # ============================================================

                # -- 加速度（每 100ms 采集，10Hz） --
                if now_ms - last_acc_ms >= Config.SENSOR_INTERVAL * 1000:
                    acc = self.sensor.read_acceleration()
                    acc_g = self.sensor.calc_acc_total(acc)
                    self.shared.update_acc(acc, acc_g)

                    # -- 温湿度 + 光照（每 1s 采集一次） --
                    if now - last_env_time >= 1:
                        env = self.sensor.read_temperature_humidity()
                        light = self.sensor.read_light()
                        self.shared.update_env(env, light)
                        # GPS 更新
                        self.gnss.update()
                        last_env_time = now

                    last_acc_ms = now_ms

                # ============================================================
                # 2. MQTT 上传
                # ============================================================

                # -- 检查 SOS 标志 --
                sos_active, sos_payload = self.shared.has_sos()
                if sos_active:
                    if self.mqtt and self.mqtt.connected:
                        log('SOS', '紧急！发送 SOS 告警到云端')
                        sos_data = OrderedDict()
                        sos_data['type'] = 'SOS'
                        sos_data['event'] = 'collision_detected'
                        if self.gnss.valid:
                            sos_data['lat'] = self.gnss.latitude
                            sos_data['lon'] = self.gnss.longitude
                        else:
                            sos_data['lat'] = 0.0
                            sos_data['lon'] = 0.0
                        sos_data['timestamp'] = int(now)
                        self.mqtt.publish(Config.TOPIC_SOS, json.dumps(sos_data))
                    self.shared.clear_sos()

                # -- 每 2s 上传传感器数据（唯一数据包） --
                if now - last_upload_time >= Config.ENV_INTERVAL:
                    acc_data, acc_g = self.shared.get_acc()
                    env_data, light_v = self.shared.get_env()
                    payload = self._build_sensor_payload(acc_data, acc_g, env_data)
                    log('UPLOAD', '数据包: {}'.format(payload))
                    self.mqtt.publish(Config.TOPIC_SENSOR, payload)
                    last_upload_time = now

                # -- 检查 MQTT 下行消息 --
                self.mqtt.check_msg()

                time.sleep(0.05)  # 50ms

            except Exception as e:
                log('THREAD', '通信/采集线程异常: {}'.format(e))
                time.sleep(0.5)

        log('THREAD', '通信/采集线程已退出')

    # ------------------------------------------------------------------
    # 报文构建
    # ------------------------------------------------------------------

    @staticmethod
    def _gps_to_dms(decimal_deg):
        """
        将十进制 GPS 坐标转换为 度分秒毫秒 字符串
        例如: 31.26291 → 31度15分44秒38毫秒
        """
        if decimal_deg is None:
            return '0度0分0秒0毫秒'
        dd = int(decimal_deg)                     # 度
        remainder = abs(decimal_deg - dd) * 60
        mm = int(remainder)                        # 分
        ss_remainder = (remainder - mm) * 60
        ss = int(ss_remainder)                     # 秒
        ms = int((ss_remainder - ss) * 1000)       # 毫秒
        return '{}度{}分{}秒{}毫秒'.format(dd, mm, ss, ms)

    def _build_sensor_payload(self, acc, acc_g, env_data):
        """构建中文格式数据包（温度/湿度/状态/GPS定位/速度）"""
        data = OrderedDict()
        # 温度
        if env_data:
            data['温度'] = '{:.1f}℃'.format(env_data['temp'])
            data['湿度'] = '{:.1f}%'.format(env_data['humidity'])
        else:
            data['温度'] = '--'
            data['湿度'] = '--'

        # 状态（拿起/自由落体/正常：通过加速度判断）
        if acc_g > Config.PICKED_UP_THRESHOLD:
            data['状态'] = '拿起'
        elif acc_g < Config.FREEFALL_THRESHOLD:
            data['状态'] = '自由落体'
        else:
            data['状态'] = '正常'

        # GPS 定位（中文度分秒格式）
        if self.gnss.valid:
            lat_dms = self._gps_to_dms(self.gnss.latitude)
            lon_dms = self._gps_to_dms(self.gnss.longitude)
            data['GPS定位'] = '北纬{} 东经{}'.format(lat_dms, lon_dms)
        else:
            data['GPS定位'] = '定位中...'

        # 速度（m/s，来自GNSS）
        data['速度'] = '{:.1f}m/s'.format(self.gnss.speed)

        return json.dumps(data)

    # ------------------------------------------------------------------
    # 启动系统
    # ------------------------------------------------------------------

    def run(self):
        """
        启动双线程并发系统
          子线程（检测）： 50ms 碰撞状态机（只读共享缓冲区，不碰 I2C）
          主线程（采集+通信）： 传感器 I2C 采集 + MQTT 上传 + 心跳
        """
        log('SYSTEM', '启动双线程并发框架...')

        try:
            # 启动碰撞检测线程（子线程，只读共享缓冲区）
            _thread.start_new_thread(self.detect_thread, ())

            # 主线程执行传感器采集 + 通信任务
            self.comm_thread()

        except KeyboardInterrupt:
            log('SYSTEM', '收到中断信号，正在停止系统...')
        except Exception as e:
            log('SYSTEM', '系统异常: {}'.format(e))
        finally:
            self.stop()

    def stop(self):
        """停止系统"""
        log('SYSTEM', '正在停止系统...')
        self.running = False
        self.gnss.stop()
        self.mqtt.disconnect()
        if self.buzzer:
            self.buzzer.beep_once(50)
        log('SYSTEM', '系统已停止')


# ====================================================================
# 第十二部分：程序入口
# ====================================================================

def main():
    """主函数入口"""
    system = HelmetSystem()
    system.run()


if __name__ == '__main__':
    main()
