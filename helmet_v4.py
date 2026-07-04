"""
============================================================================
 智能骑行头盔系统 - 版本四 (v4.0)
 功能：基础感知 + 五状态碰撞检测状态机 + 30秒二次确认 + MQTT SOS上报
       + 增强LCD显示
 硬件：移远 QuecPython 开发板 + 板载传感器 + 蜂鸣器 + 按键 + LCD
 作者：竞赛团队
 日期：2026-07-03
============================================================================
 新增模块（相比 v3）：
   - LcdHandler 增强： 启动画面/传感器仪表盘/增强倒计时/取消提示/GPS详情
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

# 板载 LED
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
    MQTT_PORT     = 44345      # TLS 端口
    MQTT_PORT_NO_TLS = 44345   # 非 TLS 端口（备用）
    MQTT_USER     = 'quectel'
    MQTT_PASSWORD = '12345678'
    MQTT_CLIENT_ID = 'helmet_v4_001'
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
    TOPIC_SENSOR  = b'/helmet/v4/sensor'    # 传感器数据上报
    TOPIC_SOS     = b'/helmet/v4/sos'        # SOS 告警主题

    # ------------------------------------------------------------------
    # 采样周期
    # ------------------------------------------------------------------
    SENSOR_INTERVAL   = 0.1    # 加速度计 100ms（10Hz）
    DETECT_INTERVAL   = 0.05   # 碰撞检测轮询 50ms
    GNSS_INTERVAL     = 1.0    # GNSS 更新 1s
    ENV_INTERVAL      = 2.0    # 环境数据上传 2s

    # ------------------------------------------------------------------
    # 碰撞检测阈值（优化：更容易触发碰撞检测）
    # ------------------------------------------------------------------
    FREE_FALL_THRESHOLD = 0.6   # 失重阈值（g），降低阈值更容易触发
    FREE_FALL_HOLD_MS   = 50   # 失重持续判定时间（毫秒），缩短触发时间
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

    # ------------------------------------------------------------------
    # 短信紧急告警配置
    # ------------------------------------------------------------------
    EMERGENCY_PHONE = '19825069205'  # 紧急联系人手机号（用户可修改）


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
    except OSError as e:
        log('TLS', '证书文件读取失败 {}: {}'.format(filepath, e))
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

    @staticmethod
    def classify_light(voltage):
        """
        根据光敏 ADC 电压值分类光照强度
        :param voltage: 电压值（V）
        :return:        "亮" / "暗" / "正常"
        """
        if voltage > 2.5:
            return '亮'
        elif voltage < 1.0:
            return '暗'
        else:
            return '正常'


# ====================================================================
# 第四部分：GNSS 定位管理模块（同 v1）
# ====================================================================

class GnssManager:
    """GNSS 定位管理器"""

    def __init__(self):
        import quectel
        self.gnss = None
        self.gnss_started = False
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
                self.gnss_started = True
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
        """启动 4G 蜂窝网络（简化版，快速失败）"""
        from quectel import Network
        try:
            net = Network()
            net.init()
            log('NET', '4G 模块初始化完成')
            sim_status = net.query_usim()
            log('NET', 'SIM 卡状态: {}'.format(sim_status))
            if sim_status:
                net.attach()
                log('NET', '4G 网络附着完成')
                return True
            else:
                log('NET', 'SIM 卡未检测到，跳过网络附着')
                return False
        except Exception as e:
            log('NET', '4G 网络初始化失败: {}'.format(e))
            return False

    def connect(self):
        """连接 MQTT 服务器（优先 TLS，失败则尝试非 TLS）"""
        ssl_context = None
        port = Config.MQTT_PORT
        
        # 尝试创建 TLS 上下文
        try:
            ca   = read_cert_file(Config.TLS_CA_PATH)
            cert = read_cert_file(Config.TLS_CERT_PATH)
            key  = read_cert_file(Config.TLS_KEY_PATH)
            
            if ca and cert and key:
                context = tls.SSLContext(tls.PROTOCOL_TLS_CLIENT)
                context.verify_mode = tls.CERT_NONE
                if isinstance(ca, str):    ca = ca.encode('utf-8')
                if isinstance(cert, str):  cert = cert.encode('utf-8')
                if isinstance(key, str):   key = key.encode('utf-8')
                context.load_verify_locations(ca)
                context.load_cert_chain(cert, key)
                ssl_context = context
                log('TLS', 'SSL 上下文配置成功')
            else:
                log('TLS', '证书文件不完整，将使用非 TLS 连接')
                port = Config.MQTT_PORT_NO_TLS
        except Exception as e:
            log('TLS', 'SSL 上下文配置失败: {}，将使用非 TLS 连接'.format(e))
            port = Config.MQTT_PORT_NO_TLS

        # 创建客户端（尝试当前配置）
        try:
            self.client = MQTTClient(
                client_id  = Config.MQTT_CLIENT_ID,
                server     = Config.MQTT_BROKER,
                port       = port,
                user       = Config.MQTT_USER,
                password   = Config.MQTT_PASSWORD,
                keepalive  = Config.MQTT_KEEPALIVE,
                ssl        = ssl_context
            )
            self.client.set_callback(self._on_message)
            log('MQTT', '配置: {}:{}  SSL={}  user={}'.format(
                Config.MQTT_BROKER, port, 
                'TLS' if ssl_context else 'None', Config.MQTT_USER))
            log('MQTT', '正在连接 {}:{}...'.format(Config.MQTT_BROKER, port))
            self.client.connect(timeout=15)
            self.connected = True
            log('MQTT', 'MQTT 连接成功！')
            return True
        except Exception as e:
            log('MQTT', 'MQTT 连接失败: {}'.format(e))
            
            # 如果失败且使用了 TLS，尝试非 TLS 端口
            if ssl_context is not None:
                log('MQTT', '尝试非 TLS 端口 {}...'.format(Config.MQTT_PORT_NO_TLS))
                try:
                    self.client = MQTTClient(
                        client_id  = Config.MQTT_CLIENT_ID,
                        server     = Config.MQTT_BROKER,
                        port       = Config.MQTT_PORT_NO_TLS,
                        user       = Config.MQTT_USER,
                        password   = Config.MQTT_PASSWORD,
                        keepalive  = Config.MQTT_KEEPALIVE,
                        ssl        = None
                    )
                    self.client.set_callback(self._on_message)
                    self.client.connect(timeout=15)
                    self.connected = True
                    log('MQTT', 'MQTT 非 TLS 连接成功！')
                    return True
                except Exception as e2:
                    log('MQTT', '非 TLS 连接也失败: {}'.format(e2))
        
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
# 第六部分：短信紧急告警模块（v4 新增）
# ====================================================================

# ====================================================================
# 第七部分：蜂鸣器管理模块（v2 新增）
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
# 第八部分：按键管理模块（v2 新增）
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
# 第八部分：短信管理模块（v4 新增）
# ====================================================================

class SmsManager:
    """
    短信管理器
    通过 quectel.SMS 发送紧急求救短信
    注：需要 SIM 卡已配置短信中心号码（SMSC），
        将 SIM 卡插入手机发送一条短信即可自动配置。
    """

    def __init__(self):
        """
        初始化短信管理器
        检测 quectel.SMS 模块是否可用
        """
        self._sms_cls = None
        self.available = False
        try:
            from quectel import SMS as _sms_cls
            self._sms_cls = _sms_cls
            self.available = True
            log('SMS', '使用 quectel.SMS 发送短信')
        except (ImportError, AttributeError) as e:
            log('SMS', 'quectel.SMS 不可用: {}'.format(e))
        if self.available:
            log('SMS', '短信管理器初始化完成')

    @staticmethod
    def _decimal_to_dms(decimal_deg):
        """
        将十进制 GPS 坐标转换为度分秒字符串
        :param decimal_deg: 十进制经纬度
        :return:            (度, 分, 秒) 三元组
        """
        if decimal_deg is None:
            return 0, 0, 0
        dd = int(decimal_deg)
        remainder = abs(decimal_deg - dd) * 60
        mm = int(remainder)
        ss = int((remainder - mm) * 60)
        return dd, mm, ss

    def send_sos_alert(self, phone, lat, lon, speed):
        """
        发送 SOS 紧急求救短信
        :param phone: 接收手机号码
        :param lat:   纬度（十进制）
        :param lon:   经度（十进制）
        :param speed: 速度（m/s）
        :return:      True 成功 / False 失败
        """
        if not self.available or self._sms_cls is None:
            log('SMS', 'SMS 模块不可用，无法发送短信')
            return False
        try:
            lat_d, lat_m, lat_s = self._decimal_to_dms(lat)
            lon_d, lon_m, lon_s = self._decimal_to_dms(lon)
            lat_dir = '北纬' if lat >= 0 else '南纬'
            lon_dir = '东经' if lon >= 0 else '西经'
            msg = '【智能头盔紧急求救】位置：{}{}度{}分{}秒 {}{}度{}分{}秒，速度：{:.1f}m/s，请救援！'.format(
                lat_dir, lat_d, lat_m, lat_s,
                lon_dir, lon_d, lon_m, lon_s,
                speed
            )
            sms = self._sms_cls()
            result = sms.send(phone, msg)
            sms.deinit()
            if result:
                log('SMS', 'SOS 短信已发送到 {}'.format(phone))
            else:
                log('SMS', 'SOS 短信发送失败（返回 False）')
            return result
        except Exception as e:
            log('SMS', 'SOS 短信发送异常: {}'.format(e))
            return False


# ====================================================================
# 第九部分：LCD 显示管理模块（v4.2 现代卡片式 UI）
# ====================================================================

class LcdHandler:
    """
    LCD 极致重构渲染引擎
    内置动态字符居中算法，采用高级多调色块进行卡片化分区，呈现高度饱满的现代科技质感
    屏幕尺寸：ST7735 160x80
    """

    def __init__(self):
        self.lcd = None
        # 预设高端色彩（16位RGB565高雅色系）
        self.DARK_NAVY = 0x012B  # 玄青蓝
        self.CARD_BG   = 0x18E3  # 灰墨蓝卡片背景
        self.CARD_ACC  = 0x2A65  # 钛金蓝卡片背景
        self.TEXT_GRAY = 0xA714  # 极客低调灰
        try:
            spi = machine.SPI(SPI_BUS, baudrate=SPI_BAUDRATE,
                              polarity=0, phase=0)
            self.lcd = LCD(spi, dc_pin=LCD_DC_PIN, cs_pin=LCD_CS_PIN)
            self.lcd.set_rotation(1)
            self.lcd.fill_screen(self.DARK_NAVY)
            self.lcd.flush()
            log('LCD', 'LCD 初始化完成（ST7735, 160x80, v4.2 卡片式 UI）')
        except Exception as e:
            log('LCD', 'LCD 初始化失败: {}'.format(e))

    def center_x(self, text, font_width=8):
        """核心算法：根据字符长度，自动计算横向绝对居中坐标"""
        screen_width = 160
        text_width = len(text) * font_width
        return max(0, (screen_width - text_width) // 2)

    def draw_window(self, title, theme_color=0x197F, bg_color=None):
        """渲染带半通透边框的全面屏顶部高级标题栏"""
        if not self.lcd: return
        bg = theme_color if bg_color is None else bg_color
        self.lcd.fill_rectangle(0, 0, 160, 14, bg)
        cx = self.center_x(title)
        self.lcd.show_string(cx, 1, title, self.lcd.WHITE, bg)
        self.lcd.fill_rectangle(146, 4, 8, 6, self.lcd.GREEN)

    def clear(self):
        """清屏（玄青蓝）"""
        if self.lcd:
            try:
                self.lcd.fill_screen(self.DARK_NAVY)
                self.lcd.flush()
            except Exception:
                pass

    def show_status(self, text, line=0):
        """显示一行状态文本"""
        if self.lcd is None:
            return
        try:
            self.lcd.show_string(2, 2 + line * 16, text[:20],
                                self.lcd.WHITE, self.DARK_NAVY)
            self.lcd.flush()
        except Exception:
            pass

    def show_boot(self, version):
        """显示启动画面"""
        if self.lcd is None:
            return
        try:
            self.lcd.fill_screen(self.lcd.BLACK)
            t1 = "SMART HELMET"
            t2 = "SYSTEM OS"
            t3 = version
            self.lcd.show_string(self.center_x(t1), 18, t1, self.lcd.CYAN, self.lcd.BLACK)
            self.lcd.show_string(self.center_x(t2), 38, t2, self.lcd.WHITE, self.lcd.BLACK)
            self.lcd.show_string(self.center_x(t3), 58, t3, self.TEXT_GRAY, self.lcd.BLACK)
            self.lcd.flush()
        except Exception:
            pass

    def show_normal(self, temp, humidity, gps_valid, speed):
        """[第1级：主仪表盘] 双卡片矩阵微格大盘，视觉信息饱满丰盈"""
        if self.lcd is None:
            return
        try:
            self.lcd.fill_screen(self.DARK_NAVY)
            self.draw_window("HELMET MONITOR")

            # ===== 左卡片：环境仓 =====
            self.lcd.fill_rectangle(4, 18, 74, 58, self.CARD_BG)
            self.lcd.show_string(8, 22, "ENV.DATA", 0x7BEF, self.CARD_BG)
            self.lcd.show_string(8, 38, "T:{:.1f}C".format(temp), self.lcd.WHITE, self.CARD_BG)
            self.lcd.show_string(8, 54, "H:{:.1f}%".format(humidity), self.lcd.WHITE, self.CARD_BG)

            # ===== 右卡片：运动仓 =====
            self.lcd.fill_rectangle(82, 18, 74, 58, self.CARD_ACC)
            self.lcd.show_string(86, 22, "GNSS.MOV", 0x7BEF, self.CARD_ACC)
            
            if gps_valid:
                self.lcd.show_string(86, 38, "FIXED", self.lcd.GREEN, self.CARD_ACC)
                self.lcd.show_string(86, 54, "{:.1f} m/s".format(speed), self.lcd.WHITE, self.CARD_ACC)
            else:
                self.lcd.show_string(86, 38, "SEARCHING", self.lcd.RED, self.CARD_ACC)
                self.lcd.show_string(86, 54, "SPD: --", self.TEXT_GRAY, self.CARD_ACC)

            self.lcd.flush()
        except Exception:
            pass

    def show_countdown(self, seconds):
        """[异常事件级] 全屏无留白反色预警，高亮卡片包围突出倒计时数据"""
        if self.lcd is None:
            return
        try:
            if seconds > 0:
                self.lcd.fill_screen(self.lcd.BLACK)
                # 奢华血红危急置顶通栏
                self.lcd.fill_rectangle(0, 0, 160, 16, self.lcd.RED)
                header_text = "CRITICAL WARNING"
                self.lcd.show_string(self.center_x(header_text), 1, header_text, self.lcd.WHITE, self.lcd.RED)

                str1 = "CRASH DETECTED"
                str2 = "SOS IN: {:02d} SEC".format(seconds)
                self.lcd.show_string(self.center_x(str1), 26, str1, self.lcd.RED, self.lcd.BLACK)
                self.lcd.show_string(self.center_x(str2), 46, str2, self.lcd.WHITE, self.lcd.BLACK)
                
                # 底部按钮底框交互区
                self.lcd.fill_rectangle(6, 66, 148, 13, 0x3186)
                btn_text = "PRESS KEY TO CANCEL"
                self.lcd.show_string(self.center_x(btn_text), 67, btn_text, self.lcd.WHITE, 0x3186)
            else:
                # 危机落地，大字全屏极速跳变反闪
                flash_toggle = (int(time.ticks_ms()) // 300) % 2
                bg = self.lcd.RED if flash_toggle else self.lcd.BLACK
                fg = self.lcd.WHITE if flash_toggle else self.lcd.RED
                
                self.lcd.fill_screen(bg)
                s1 = "EMERGENCY"
                s2 = "SOS SENT"
                self.lcd.show_string(self.center_x(s1), 24, s1, fg, bg)
                self.lcd.show_string(self.center_x(s2), 44, s2, fg, bg)
                
            self.lcd.flush()
        except Exception:
            pass

    def show_sos_cancelled(self):
        """[交互过渡态] 全覆盖祖母绿安全回归确认框"""
        if self.lcd is None:
            return
        try:
            self.lcd.fill_screen(0x03E0)
            text1 = "SYSTEM SAFE"
            text2 = "ALARM CANCELLED"
            self.lcd.show_string(self.center_x(text1), 25, text1, self.lcd.WHITE, 0x03E0)
            self.lcd.show_string(self.center_x(text2), 45, text2, self.lcd.WHITE, 0x03E0)
            self.lcd.flush()
        except Exception:
            pass

    def show_sms_sent(self, phone):
        """显示短信已发送提示"""
        if self.lcd is None:
            return
        try:
            self.lcd.fill_screen(self.DARK_NAVY)
            self.draw_window("SMS STATUS")
            self.lcd.fill_rectangle(4, 18, 152, 58, self.CARD_BG)
            
            self.lcd.show_string(self.center_x("SENT TO:"), 24, "SENT TO:", 
                               self.lcd.CYAN, self.CARD_BG)
            self.lcd.show_string(self.center_x(phone), 42, phone, 
                               self.lcd.WHITE, self.CARD_BG)
            self.lcd.show_string(self.center_x("OK"), 58, "OK", 
                               self.lcd.GREEN, self.CARD_BG)
            self.lcd.flush()
        except Exception:
            pass

    def show_gps_info(self, lat, lon, satellites):
        """[第2级：详情层] 大文本环绕式卡片，全面榨干屏幕留白空间"""
        if self.lcd is None:
            return
        try:
            self.lcd.fill_screen(self.DARK_NAVY)
            self.draw_window("GNSS NMEA DETAIL")

            # 大面积中央详情卡片槽填充
            self.lcd.fill_rectangle(4, 18, 152, 58, self.CARD_BG)

            # 数据在卡片内精细对齐排列
            self.lcd.show_string(10, 24, "LAT: {:.5f}".format(lat), self.lcd.CYAN, self.CARD_BG)
            self.lcd.show_string(10, 41, "LON: {:.5f}".format(lon), self.lcd.CYAN, self.CARD_BG)
            self.lcd.show_string(10, 58, "SATS TRACKED: {:02d}".format(satellites), self.lcd.WHITE, self.CARD_BG)
            
            self.lcd.flush()
        except Exception:
            pass


# ====================================================================
# 第十部分：碰撞检测状态机（v2 新增 - 核心）
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
        self._last_sos_time_ms = 0         # 上次 SOS 发送时间

        # ---------- 按键取消标志 ----------
        self.sos_cancelled_flag = False    # 按键取消标志（ISR 中设置，主线程消费）

        # ---------- 日志 ----------
        self.last_log_state = -1          # 上次记录的状态（防止重复日志）
        log('STATE', '碰撞检测状态机初始化完成（五状态FSM）')

    # ------------------------------------------------------------------
    # 线程安全操作
    # ------------------------------------------------------------------

    def get_state(self):
        """获取当前状态（线程安全）"""
        self.lock.acquire()
        s = self.state
        self.lock.release()
        return s

    def set_state(self, new_state):
        """设置当前状态并打印日志（线程安全）"""
        self.lock.acquire()
        old_state = self.state
        self.state = new_state
        state_names = [
            'IDLE', 'WEIGHTLESS', 'IMPACT',
            'POST_ACCIDENT', 'SOS_TRIGGERED'
        ]
        if new_state != old_state:
            log('STATE', '状态切换: {} → {}'.format(
                state_names[old_state], state_names[new_state]))
        self.lock.release()
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
        按键按下回调（在硬件 ISR 中运行，只能做最轻量操作）
        仅设置取消标志，LCD 显示由主线程 comm_thread 处理
        """
        state = self.get_state()
        if state == CollisionState.POST_ACCIDENT or state == CollisionState.SOS_TRIGGERED:
            log('BUTTON', '用户按下取消按键，SOS 已取消')
            # 蜂鸣器短鸣一声（简单 GPIO，ISR 中可做）
            if self.buzzer:
                self.buzzer.beep_once(50)
            # 设置标志位，主线程检测到后显示 + 复位
            self.sos_cancelled_flag = True

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
        # 状态 1: WEIGHTLESS → 失重确认后直接进入倒计时
        # =============================================================
        elif state == CollisionState.WEIGHTLESS:
            # 失重已确认，直接进入事故后倒计时（不等待冲击检测）
            # 这样无论后续加速度如何变化，30s倒计时都会正常启动
            self.countdown_start = current_time_ms
            self.countdown_remaining = Config.SOS_COUNTDOWN_SEC
            self.set_state(CollisionState.POST_ACCIDENT)

            # 打开蜂鸣器提示
            if self.buzzer:
                self.buzzer.beep_once(200)
            # 注：LCD 显示由主线程 comm_thread 处理（子线程栈空间不足）

        # =============================================================
        # 状态 2: IMPACT → 保留（兼容旧逻辑，现在可直通）
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
                # 注：LCD 由主线程处理

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
                # 倒计时变化，更新蜂鸣器（LCD 由主线程 comm_thread 处理）
                self.countdown_remaining = remaining
                if remaining > 0:
                    # 蜂鸣器间歇鸣叫
                    if self.buzzer:
                        self.buzzer.beep_once(80)

            if remaining <= 0:
                # 倒计时归零 → 触发 SOS
                self.set_state(CollisionState.SOS_TRIGGERED)
                self.sos_sent = True
                self._last_sos_time_ms = current_time_ms
                log('SOS', 'SOS 告警已标记！')
                if self.buzzer:
                    self.buzzer.beep_once(500)

        # =============================================================
        # 状态 4: SOS_TRIGGERED → 保持 SOS 状态，等待按键取消
        # =============================================================
        elif state == CollisionState.SOS_TRIGGERED:
            # 保持 SOS 状态不变，等待用户按键手动取消
            # 每 5 秒重发一次 SOS 确保送达
            if self.sos_sent and (current_time_ms - self._last_sos_time_ms) > 5000:
                self.sos_sent = True
                self._last_sos_time_ms = current_time_ms
                log('SOS', 'SOS 告警已标记！')
            pass

        # 返回当前状态和倒计时
        return StateResult(self.get_state(), self.countdown_remaining)


class StateResult:
    """状态机更新结果（用于线程间传递）"""

    def __init__(self, state, countdown):
        self.state = state
        self.countdown = countdown


# ====================================================================
# 第十一部分：共享数据缓冲区（线程安全）
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
        self.lock.acquire()
        self.acc = acc
        self.acc_total_g = acc_g
        self.lock.release()

    def get_acc(self):
        """读取加速度数据（线程安全）"""
        self.lock.acquire()
        a = self.acc
        g = self.acc_total_g
        self.lock.release()
        return a, g

    def update_env(self, env, light):
        """更新环境数据（线程安全）"""
        self.lock.acquire()
        if env:
            self.env_data = env
        self.light_v = light
        self.lock.release()

    def get_env(self):
        """读取环境数据（线程安全）"""
        self.lock.acquire()
        e = self.env_data
        l = self.light_v
        self.lock.release()
        return e, l

    def set_sos(self, payload=None):
        """设置 SOS 标志（线程安全）"""
        self.lock.acquire()
        self.sos_active = True
        self.sos_payload = payload
        self.lock.release()

    def clear_sos(self):
        """清除 SOS 标志（线程安全）"""
        self.lock.acquire()
        self.sos_active = False
        self.sos_payload = None
        self.lock.release()

    def has_sos(self):
        """检查是否有 SOS 需要发送（线程安全）"""
        self.lock.acquire()
        active = self.sos_active
        payload = self.sos_payload
        self.lock.release()
        return active, payload


# ====================================================================
# 第十二部分：系统主控制类
# ====================================================================

class HelmetSystem:
    """
    系统主控制器
    管理所有子模块的初始化与三线程并发运行
    """

    def __init__(self):
        log('SYSTEM', '=' * 50)
        log('SYSTEM', '智能骑行头盔系统 v4.0 启动')
        log('SYSTEM', '=' * 50)

        # ---------- 1. 初始化传感器 ----------
        self.sensor = SensorManager()

        # ---------- 2. 初始化网络和 MQTT（带超时保护） ----------
        self.mqtt = MqttManager()
        self.mqtt_available = False
        try:
            if self.mqtt.start_network():
                # 等待 NTP 时间同步（最多 3 秒，超时继续）
                log('SYSTEM', '等待 NTP 时间同步...')
                ntp_wait = 0
                while ntp_wait < 3 and int(time.time()) <= 1700000000:
                    time.sleep(1)
                    ntp_wait += 1
                if int(time.time()) > 1700000000:
                    log('SYSTEM', 'NTP 时间同步完成')
                else:
                    log('SYSTEM', 'NTP 时间同步超时，继续启动')
                # 重试 MQTT 连接（最多 2 次，缩短超时）
                for attempt in range(1, 3):
                    log('MQTT', 'MQTT 连接尝试 {}/2...'.format(attempt))
                    if self.mqtt.connect():
                        self.mqtt_available = True
                        break
                    if attempt < 2:
                        log('MQTT', '3 秒后重试...')
                        time.sleep(3)
                else:
                    log('MQTT', 'MQTT 连接失败，系统将在无 MQTT 模式下运行')
            else:
                log('NET', '网络未就绪，系统将在无网络模式下运行核心功能')
        except Exception as e:
            log('NET', '网络初始化异常: {}'.format(e))

        # ---------- 3. 初始化 GNSS（放在 MQTT 之后，避免 AT 命令冲突） ----------
        self.gnss = GnssManager()
        if self.gnss.start():
            log('GNSS', 'GNSS 定位已启动')
        else:
            log('GNSS', 'GNSS 启动失败，定位不可用')

        # ---------- 4. 初始化短信管理器 ----------
        self.sms = SmsManager()

        # ---------- 5. 初始化蜂鸣器、按键、LCD ----------
        self.buzzer = BuzzerHandler()
        self.button = ButtonHandler()
        self.lcd    = LcdHandler()
        # v4 增强启动画面
        if self.lcd:
            self.lcd.show_boot('v4.0')
            time.sleep(1.5)
            self.lcd.clear()

        # ---------- 6. 初始化共享数据区 ----------
        self.shared = SharedData()

        # ---------- 7. 初始化碰撞检测状态机 ----------
        self.detector = CollisionDetector(
            buzzer=self.buzzer,
            lcd=self.lcd,
            button=self.button,
            mqtt=self.mqtt,
            gnss=self.gnss
        )

        # 注册按键回调（关联到状态机的取消处理）
        self.button.on_press = self.detector.on_button_press

        # ---------- 8. 运行标志 ----------
        self.running = True

        log('SYSTEM', '所有模块初始化完成，准备启动双线程并发框架')

    # ------------------------------------------------------------------
    # 主线程：单线程循环（所有任务合并，避免子线程栈溢出）
    # ------------------------------------------------------------------

    def comm_thread(self):
        """
        通信+采集+检测线程（单主线程运行）
        受 QuecPython 子线程栈空间限制（默认 4KB），所有任务合并到主线程
        负责：
          1. 每 100ms 采集加速度（I2C，10Hz）
          2. 每 50ms 运行碰撞检测状态机
          3. 每 2s 采集温湿度 + 光照
          4. 每 5s 更新 GNSS
          5. 每 2s 上传传感器数据（MQTT）
          6. 检测到 SOS 标志时发送告警（MQTT + 短信）
          7. 检查 MQTT 下行消息 + 断线重连
          8. 更新 LCD 显示
          9. 检测按键取消 SOS
        """
        log('THREAD', '单线程系统已启动（采集 + 检测 + 通信合并）')
        last_acc_ms = time.ticks_ms()
        last_env_time = time.time()
        last_gps_time = time.time()
        last_upload_time = time.time()
        last_reconnect_time = time.time()
        last_sos_send_time = time.time()
        last_lcd_update = time.time()
        sos_sms_sent = False

        while self.running:
            try:
                now = time.time()
                now_ms = time.ticks_ms()

                # ============================================================
                # 1. 传感器采集（主线程运行，避免子线程 I2C 栈溢出）
                # ============================================================

                # -- 加速度（每 100ms 采集，10Hz） --
                if now_ms - last_acc_ms >= Config.SENSOR_INTERVAL * 1000:
                    acc = self.sensor.read_acceleration()
                    acc_g = self.sensor.calc_acc_total(acc)
                    self.shared.update_acc(acc, acc_g)

                    # -- 温湿度 + 光照（每 2s 采集一次） --
                    if now - last_env_time >= 2:
                        env = self.sensor.read_temperature_humidity()
                        light = self.sensor.read_light()
                        self.shared.update_env(env, light)
                        last_env_time = now
                    
                    # -- GPS 更新（每 5s 一次，GNSS启动失败则跳过） --
                    if now - last_gps_time >= 5:
                        if self.gnss.gnss_started:
                            try:
                                self.gnss.update()
                            except Exception as e:
                                log('GNSS', '更新异常: {}'.format(e))
                        last_gps_time = now

                    last_acc_ms = now_ms

                # ============================================================
                # 1b. 碰撞检测状态机（每 50ms 轮询）
                # ============================================================
                acc_data, acc_g = self.shared.get_acc()
                result = self.detector.update(acc_g, now_ms)
                if result.state == CollisionState.SOS_TRIGGERED:
                    self.shared.set_sos('emergency')

                # ============================================================
                # 2. MQTT 上传
                # ============================================================

                # -- SOS 告警发送（含 5 秒重发机制 + v4 短信发送） --
                sos_active, _ = self.shared.has_sos()
                should_send_sos = sos_active
                # 如果状态机仍在 SOS_TRIGGERED 状态，每 5 秒重发
                if (not sos_active and
                    self.detector.get_state() == CollisionState.SOS_TRIGGERED and
                    now - last_sos_send_time >= 5):
                    should_send_sos = True

                if should_send_sos:
                    if self.mqtt and self.mqtt.connected:
                        log('SOS', '紧急！发送 SOS 告警到云端')
                        sos_data = OrderedDict()
                        sos_data['type'] = 'SOS'
                        sos_data['event'] = 'collision_detected'
                        if self.gnss and self.gnss.valid:
                            sos_data['lat'] = self.gnss.latitude
                            sos_data['lon'] = self.gnss.longitude
                        else:
                            sos_data['lat'] = 0.0
                            sos_data['lon'] = 0.0
                        sos_data['timestamp'] = int(now)
                        self.mqtt.publish(Config.TOPIC_SOS, json.dumps(sos_data))
                        last_sos_send_time = now

                    # 发送短信（仅一次）
                    if not sos_sms_sent:
                        lat = self.gnss.latitude if self.gnss and self.gnss.valid else 0.0
                        lon = self.gnss.longitude if self.gnss and self.gnss.valid else 0.0
                        speed = self.gnss.speed if self.gnss and self.gnss.valid else 0.0
                        try:
                            sms_ok = self.sms.send_sos_alert(
                                Config.EMERGENCY_PHONE, lat, lon, speed)
                            if sms_ok:
                                sos_sms_sent = True
                                if self.lcd:
                                    self.lcd.show_sms_sent(Config.EMERGENCY_PHONE)
                                    time.sleep(1)
                            else:
                                log('SMS', 'SOS 短信发送失败，将在下次 SOS 触发时重试')
                        except Exception as e:
                            log('SMS', '发送短信异常: {}'.format(e))
                            sos_sms_sent = True

                    # 清除共享标志（避免下一轮重复触发）
                    if sos_active:
                        self.shared.clear_sos()

                # -- 每 2s 上传传感器数据（唯一数据包） --
                if now - last_upload_time >= Config.ENV_INTERVAL:
                    acc_data, acc_g = self.shared.get_acc()
                    env_data, light_v = self.shared.get_env()
                    payload = self._build_sensor_payload(acc_data, acc_g, env_data)
                    log('UPLOAD', '数据包: {}'.format(payload))
                    if self.mqtt and self.mqtt.connected:
                        self.mqtt.publish(Config.TOPIC_SENSOR, payload)
                    last_upload_time = now

                # -- 检查 MQTT 下行消息 --
                if self.mqtt and self.mqtt.connected:
                    self.mqtt.check_msg()

                # -- MQTT 断线自动重连（无网络时 120s，有网络时 30s） --
                if not self.mqtt.connected and (now - last_reconnect_time) >= (120 if not self.mqtt_available else 30):
                    last_reconnect_time = now
                    if not self.mqtt_available:
                        log('MQTT', '网络未就绪，跳过重连')
                    else:
                        log('MQTT', 'MQTT 已断线，尝试重连...')
                        try:
                            self.mqtt.connect()
                        except Exception as e:
                            log('MQTT', '重连失败: {}'.format(e))

                # ============================================================
                # 3. LCD 更新（主线程处理，避免子线程栈溢出）
                # ============================================================
                if self.lcd:
                    current_state = self.detector.get_state()

                    # -- 按键取消标志（ISR 中设置，主线程执行 LCD + 复位） --
                    if self.detector.sos_cancelled_flag:
                        self.detector.sos_cancelled_flag = False
                        self.lcd.show_sos_cancelled()
                        self.detector.reset_to_idle()
                        sos_sms_sent = False  # 复位，下次 SOS 可再次发送短信

                    # -- SOS/倒计时状态：LCD 由主线程控制（不交给子线程） --
                    if current_state in (CollisionState.POST_ACCIDENT,
                                         CollisionState.SOS_TRIGGERED):
                        if now - last_lcd_update >= 1:
                            if current_state == CollisionState.POST_ACCIDENT:
                                remaining = self.detector.countdown_remaining
                                self.lcd.show_countdown(max(remaining, 1))
                            else:
                                self.lcd.show_countdown(0)  # 红色闪烁 SOS
                            last_lcd_update = now

                    # -- 正常状态：每 2 秒刷新仪表盘 --
                    elif current_state == CollisionState.IDLE:
                        if now - last_lcd_update >= 2:
                            env_data, _ = self.shared.get_env()
                            temp = env_data['temp'] if env_data else 0.0
                            humidity = env_data['humidity'] if env_data else 0.0
                            gps_valid = self.gnss.valid if self.gnss else False

                            # 构建 DMS 字符串用于显示
                            if gps_valid:
                                lat_dms = self._gps_to_dms_short(self.gnss.latitude)
                                lon_dms = self._gps_to_dms_short(self.gnss.longitude)
                            else:
                                lat_dms = ''
                                lon_dms = ''

                            speed = self.gnss.speed if self.gnss else 0.0
                            self.lcd.show_normal(temp, humidity, gps_valid, speed)
                            last_lcd_update = now

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

    @staticmethod
    def _gps_to_dms_short(decimal_deg):
        """
        将十进制 GPS 坐标转换为简短度分秒字符串（用于 LCD 显示）
        例如: 31.26291 → 31度15分44秒
        """
        if decimal_deg is None:
            return '0度0分0秒'
        dd = int(decimal_deg)
        remainder = abs(decimal_deg - dd) * 60
        mm = int(remainder)
        ss_remainder = (remainder - mm) * 60
        ss = int(ss_remainder)
        return '{}度{}分{}秒'.format(dd, mm, ss)

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

        # 状态（从碰撞检测状态机读取：碰撞/正常/跌倒/SOS）
        st = self.detector.get_state()
        if st == CollisionState.IDLE:
            data['状态'] = '正常'
        elif st == CollisionState.WEIGHTLESS:
            data['状态'] = '跌倒'
        elif st == CollisionState.SOS_TRIGGERED:
            data['状态'] = 'SOS'
        else:  # IMPACT / POST_ACCIDENT
            data['状态'] = '碰撞'

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
        启动单线程系统（所有任务合并到主线程）
        受 QuecPython 子线程栈空间限制（默认 4KB），子线程会导致栈溢出
        采用单主线程分时轮询架构：采集 + 检测 + 通信全部在主线程循环内执行
        """
        log('SYSTEM', '启动单线程系统（采集 + 检测 + 通信合并到主线程）')

        try:
            # 主线程执行所有任务
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
# 第十三部分：程序入口
# ====================================================================

def main():
    """主函数入口"""
    system = HelmetSystem()
    system.run()


if __name__ == '__main__':
    main()
