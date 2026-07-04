"""
============================================================================
 智能骑行头盔系统 - 版本一 (v1.0)
 功能：基础传感器数据采集 + 4G MQTT 云端上传
 硬件：移远 QuecPython 开发板 + 板载传感器
 作者：竞赛团队
 日期：2026-07-02
============================================================================
 模块说明：
   - SensorManager:   统一管理所有板载传感器（加速度、温湿度、光敏）
   - GnssManager:     GNSS 定位数据获取
   - MqttManager:     MQTT 通信客户端管理
   - DataCollector:   数据采集与上传主循环协调器
============================================================================
 依赖例程：
   imu.py  - LIS2DH12 三轴加速度计
   aht20.py - AHT20 温湿度传感器（实际用 application.py 中的 AHT20 库）
   ldr.py  - 光敏电阻 ADC 读取
   gnss.py - GNSS 定位模块
   mqtt.py - MQTT 通信
============================================================================
"""

# ==================== 标准库导入 ====================
import machine  # 硬件引脚、I2C、ADC 等
import time     # 延时、时间戳
import json     # JSON 序列化（用于 MQTT 报文）
import sys      # 系统退出（TLS 证书读取失败时使用）
import tls      # TLS 加密上下文（用于 MQTT 加密连接）
from collections import OrderedDict  # 有序字典，保证 JSON 字段顺序

# ==================== 第三方库导入（板载传感器驱动） ====================
from lis2dh12 import LIS2DH12  # 加速度计驱动
from ahtx0 import AHT20        # 温湿度传感器驱动
from umqtt.robust import MQTTClient  # MQTT 客户端（支持自动重连）

# ==================== 板载硬件常量定义 ====================

# ADC 通道：光敏电阻接在 PC5 引脚上
LDR_ADC_PIN = 'C5'

# I2C 总线：板载 LIS2DH12 和 AHT20 共用 I2C1，频率 400kHz
I2C_BUS = 1
I2C_FREQ = 400000

# SPI 总线：LCD 屏幕（版本一中暂不使用，预留）
# SPI_BUS = 1
# SPI_BAUDRATE = 20000000


# ====================================================================
# 第一部分：配置类
# 集中管理所有可调参数，方便后期标定与修改
# ====================================================================

class Config:
    """系统配置参数"""

    # ------------------------------------------------------------------
    # MQTT 服务器配置（使用 mqtt_duplex.py 验证通过的 TLS 服务器）
    # ------------------------------------------------------------------
    MQTT_BROKER   = '172.188.83.251'   # MQTT 服务器 IP 或域名
    MQTT_PORT     = 43719              # MQTT 服务器端口（TLS 加密端口）
    MQTT_USER     = 'quectel'          # 登录用户名
    MQTT_PASSWORD = '12345678'         # 登录密码
    MQTT_CLIENT_ID = 'helmet_v1_001'   # 客户端 ID（需唯一）
    MQTT_KEEPALIVE = 60                # MQTT 心跳保活秒数（建议 30~120s）

    # ------------------------------------------------------------------
    # TLS 证书文件路径（与 mqtt_duplex.py 保持一致）
    # ------------------------------------------------------------------
    TLS_CA_PATH   = '/flash/connectlab_rsa_ca.cer'
    TLS_CERT_PATH = '/flash/connectlab_rsa_client_tmp.cer'
    TLS_KEY_PATH  = '/flash/connectlab_rsa_client_tmp.key'

    # ------------------------------------------------------------------
    # MQTT 主题（Topic）定义
    # ------------------------------------------------------------------
    TOPIC_SENSOR  = b'/helmet/v1/sensor'   # 传感器数据上报主题
    TOPIC_STATUS  = b'/helmet/v1/status'   # 系统状态上报主题

    # ------------------------------------------------------------------
    # 传感器采样周期（单位：秒）
    # ------------------------------------------------------------------
    SENSOR_INTERVAL = 0.1    # 加速度计采样周期 100ms（即 10Hz）
    GNSS_INTERVAL   = 1.0    # GNSS 定位更新周期 1s（即 1Hz）
    ENV_INTERVAL    = 2.0    # 温湿度/光照上传周期 2s
    HEARTBEAT_INTERVAL = 10  # MQTT 心跳包间隔 10s

    # ------------------------------------------------------------------
    # 传感器阈值（版本二碰撞检测时使用，此处预留）
    # ------------------------------------------------------------------
    FREE_FALL_THRESHOLD = 0.5   # 失重阈值（单位：g）
    IMPACT_THRESHOLD    = 3.5   # 碰撞冲击阈值（单位：g）


# ====================================================================
# 第二部分：工具函数
# ====================================================================

def log(tag, message):
    """
    日志输出函数
    :param tag:     模块标签（如 'SENSOR', 'GNSS', 'MQTT'）
    :param message: 日志内容
    """
    timestamp = time.time()
    print('[{}] [{}] {}'.format(int(timestamp), tag, message))


def format_gps_coord(latitude, longitude):
    """
    将 GPS 坐标格式化为固定宽度字符串
    :param latitude:  纬度
    :param longitude: 经度
    :return:          (纬度字符串, 经度字符串)
    """
    lat_str = '{:.6f}'.format(latitude) if latitude else '0.000000'
    lon_str = '{:.6f}'.format(longitude) if longitude else '0.000000'
    return lat_str, lon_str


def read_cert_file(filepath):
    """
    读取 TLS 证书文件内容（从 mqtt_duplex.py 移植）
    支持文本模式和二进制模式两种读取方式
    :param filepath: 证书文件路径
    :return:         证书内容字符串
    """
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
        # 尝试二进制读取
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
# 第三部分：传感器管理模块 (SensorManager)
# 负责初始化与读取所有板载传感器
# ====================================================================

class SensorManager:
    """
    传感器管理器
    统一管理 LIS2DH12 加速度计、AHT20 温湿度传感器、光敏电阻 ADC
    """

    def __init__(self):
        """
        构造函数：初始化 I2C 总线以及所有板载传感器
        如果某个传感器初始化失败，将其置为 None 并打印警告
        """
        # ---------- 1. 初始化 I2C 总线 ----------
        try:
            self.i2c = machine.I2C(I2C_BUS, freq=I2C_FREQ)
            log('I2C', 'I2C 总线初始化完成，频率 {}Hz'.format(I2C_FREQ))
        except Exception as e:
            log('I2C', 'I2C 总线初始化失败: {}'.format(e))
            self.i2c = None

        # ---------- 2. 初始化 LIS2DH12 加速度计 ----------
        try:
            if self.i2c:
                self.lis2dh = LIS2DH12(self.i2c)
                log('LIS2DH12', '加速度计初始化完成')
            else:
                self.lis2dh = None
        except Exception as e:
            log('LIS2DH12', '加速度计初始化失败: {}'.format(e))
            self.lis2dh = None

        # ---------- 3. 初始化 AHT20 温湿度传感器 ----------
        try:
            if self.i2c:
                self.aht20 = AHT20(self.i2c)
                log('AHT20', '温湿度传感器初始化完成')
            else:
                self.aht20 = None
        except Exception as e:
            log('AHT20', '温湿度传感器初始化失败: {}'.format(e))
            self.aht20 = None

        # ---------- 4. 初始化光敏电阻 ADC ----------
        try:
            self.adc = machine.ADC(machine.Pin(LDR_ADC_PIN))
            log('ADC', '光敏电阻 ADC 初始化完成，引脚 {}'.format(LDR_ADC_PIN))
        except Exception as e:
            log('ADC', '光敏电阻 ADC 初始化失败: {}'.format(e))
            self.adc = None

        # ---------- 5. 扫描 I2C 总线上的所有设备（调试用） ----------
        if self.i2c:
            try:
                devices = self.i2c.scan()
                log('I2C', '扫描到设备: {}'.format([hex(d) for d in devices]))
            except Exception:
                pass

    # ------------------------------------------------------------------
    # 加速度数据采集
    # ------------------------------------------------------------------

    def read_acceleration(self):
        """
        读取三轴加速度数据
        :return: dict，包含 x, y, z 三个轴的值（单位：m/s²）
                 读取失败时返回全零字典
        """
        result = {'x': 0.0, 'y': 0.0, 'z': 0.0}
        if self.lis2dh is None:
            return result

        try:
            acc_x, acc_y, acc_z = self.lis2dh.acceleration
            result['x'] = round(acc_x, 3)
            result['y'] = round(acc_y, 3)
            result['z'] = round(acc_z, 3)
        except Exception as e:
            log('LIS2DH12', '读取加速度失败: {}'.format(e))

        return result

    def calc_acc_total(self, acc):
        """
        计算三轴合力幅值（标量）
        :param acc: 加速度字典，包含 x, y, z
        :return:    合力幅值 sqrt(x^2 + y^2 + z^2)，单位 m/s²
                    转换为重力加速度 g（除以 9.8）
        """
        total = (acc['x']**2 + acc['y']**2 + acc['z']**2) ** 0.5
        # 保留两位小数，转换为 g 值
        return round(total / 9.8, 2)

    # ------------------------------------------------------------------
    # 温湿度数据采集
    # ------------------------------------------------------------------

    def read_temperature_humidity(self):
        """
        读取温湿度数据
        :return: dict，包含 temp（温度，°C）和 humidity（湿度，%RH）
                 读取失败时返回 None
        """
        if self.aht20 is None:
            return None

        try:
            temp = self.aht20.temperature
            hum  = self.aht20.relative_humidity
            return {
                'temp': round(temp, 1),
                'humidity': round(hum, 1)
            }
        except Exception as e:
            log('AHT20', '读取温湿度失败: {}'.format(e))
            return None

    # ------------------------------------------------------------------
    # 光照数据采集
    # ------------------------------------------------------------------

    def read_light(self):
        """
        读取光敏电阻电压值
        :return: 电压值（单位：V），读取失败时返回 0.0
        """
        if self.adc is None:
            return 0.0

        try:
            # 读取 16 位原始值
            raw_16bit = self.adc.read_u16()      # 范围 0~65535
            # 右移 4 位，转换为 12 位精度
            raw_12bit = raw_16bit >> 4            # 范围 0~4095
            # 转换为电压值（参考电压 3.3V）
            voltage = (raw_12bit * 3.3) / 4095.0
            return round(voltage, 3)
        except Exception as e:
            log('ADC', '读取光敏电压失败: {}'.format(e))
            return 0.0


# ====================================================================
# 第四部分：GNSS 定位管理模块 (GnssManager)
# 负责 GNSS 模块的启停与位置数据获取
# ====================================================================

class GnssManager:
    """
    GNSS 定位管理器
    封装 quectel.GNSS() 的启动、停止和位置读取
    """

    def __init__(self):
        """构造函数：初始化 GNSS 模块"""
        import quectel  # 移远平台专用库，在此处导入避免顶层加载失败

        self.gnss = None
        self.valid = False          # 上次定位是否有效
        self.latitude  = 0.0        # 纬度
        self.longitude = 0.0        # 经度
        self.speed     = 0.0        # 速度（km/h）
        self.altitude  = 0.0        # 海拔（m）
        self.satellites = 0         # 卫星颗数

        try:
            self.gnss = quectel.GNSS()
            log('GNSS', 'GNSS 模块对象创建成功')
        except Exception as e:
            log('GNSS', 'GNSS 模块创建失败: {}'.format(e))
            self.gnss = None

    def start(self):
        """
        启动 GNSS 定位
        :return: True 表示启动成功，False 表示失败
        """
        if self.gnss is None:
            return False

        try:
            if self.gnss.start():
                log('GNSS', '定位模块启动成功，等待卫星信号...')
                return True
            else:
                log('GNSS', '定位模块启动失败')
                return False
        except Exception as e:
            log('GNSS', '定位模块启动异常: {}'.format(e))
            return False

    def stop(self):
        """停止 GNSS 定位，释放资源"""
        if self.gnss:
            try:
                self.gnss.stop()
                log('GNSS', '定位模块已停止')
            except Exception as e:
                log('GNSS', '定位模块停止失败: {}'.format(e))

    def update(self):
        """
        更新一次定位数据（无返回值，结果存入实例属性中）
        调用后访问 self.latitude, self.longitude, self.valid 等字段
        """
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

    def get_position_str(self):
        """
        获取可读的位置字符串
        :return: 格式化的位置描述
        """
        if self.valid:
            return '纬度:{}  经度:{}  速度:{}km/h'.format(
                self.latitude, self.longitude, self.speed)
        else:
            return '定位中...'


# ====================================================================
# 第五部分：MQTT 通信管理模块 (MqttManager)
# 负责 4G 网络初始化与 MQTT 客户端管理
# ====================================================================

class MqttManager:
    """
    MQTT 通信管理器
    封装网络初始化、MQTT 连接、发布/订阅操作
    """

    def __init__(self):
        """构造函数：初始化网络和 MQTT 客户端"""
        self.client    = None
        self.connected = False

    def start_network(self):
        """
        启动 4G 蜂窝网络
        使用 quectel.Network 模块完成网络附着
        :return: True 表示网络就绪，False 表示失败
        """
        from quectel import Network

        try:
            net = Network()
            net.init()
            log('NET', '4G 模块初始化完成')

            # 查询 SIM 卡状态
            sim_status = net.query_usim()
            log('NET', 'SIM 卡状态: {}'.format(sim_status))

            # 附着网络
            net.attach()
            log('NET', '4G 网络附着完成')
            return True
        except Exception as e:
            log('NET', '4G 网络初始化失败: {}'.format(e))
            return False

    def connect(self):
        """
        连接 MQTT 服务器（TLS 加密连接）
        从 mqtt_duplex.py 移植证书读取与 TLS 上下文配置
        :return: True 表示连接成功，False 表示失败
        """
        # ---------- 1. 读取 TLS 证书 ----------
        ca   = read_cert_file(Config.TLS_CA_PATH)
        cert = read_cert_file(Config.TLS_CERT_PATH)
        key  = read_cert_file(Config.TLS_KEY_PATH)

        if not ca or not cert or not key:
            log('MQTT', 'TLS 证书读取不完整，无法建立加密连接')
            return False

        # ---------- 2. 创建 TLS 上下文 ----------
        try:
            context = tls.SSLContext(tls.PROTOCOL_TLS_CLIENT)
            context.verify_mode = tls.CERT_REQUIRED

            # 证书内容统一转为 bytes
            if isinstance(ca, str):
                ca = ca.encode('utf-8')
            if isinstance(cert, str):
                cert = cert.encode('utf-8')
            if isinstance(key, str):
                key = key.encode('utf-8')

            context.load_verify_locations(ca)
            context.load_cert_chain(cert, key)
            log('TLS', 'SSL 上下文配置成功')
        except Exception as e:
            log('TLS', 'SSL 上下文配置失败: {}'.format(e))
            return False

        # ---------- 3. 创建 MQTT 客户端（使用 TLS） ----------
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

            # 设置消息回调
            self.client.set_callback(self._on_message)

            # 打印当前 MQTT 配置
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
        """断开 MQTT 连接"""
        if self.client and self.connected:
            try:
                self.client.disconnect()
                self.connected = False
                log('MQTT', 'MQTT 连接已断开')
            except Exception as e:
                log('MQTT', 'MQTT 断开失败: {}'.format(e))

    def publish(self, topic, payload):
        """
        发布消息到指定主题
        :param topic:   主题（bytes 类型）
        :param payload: 消息内容（字符串或 bytes）
        :return:        True 表示发布成功，False 表示失败
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
        """
        检查是否有新消息到达（非阻塞）
        需要在主循环中周期性调用
        """
        if self.client and self.connected:
            try:
                self.client.check_msg()
            except Exception as e:
                log('MQTT', '消息检查异常: {}'.format(e))
                self.connected = False

    @staticmethod
    def _on_message(topic, msg):
        """
        MQTT 消息回调函数（内部使用，版本一留空）
        :param topic: 消息主题
        :param msg:   消息内容
        """
        # 版本一暂不处理下行消息，仅打印日志
        log('MQTT', '收到下行消息 [{}]: {}'.format(topic.decode(), msg.decode()))


# ====================================================================
# 第六部分：数据采集与主循环 (DataCollector)
# 协调各模块，按固定周期采集数据并通过 MQTT 上传
# ====================================================================

class DataCollector:
    """
    数据采集协调器
    负责：
      1. 以不同频率采集各传感器数据
      2. 周期性通过 MQTT 上传至云平台
      3. 打印系统运行日志
    """

    def __init__(self):
        """构造函数：初始化所有子模块"""
        log('SYSTEM', '=' * 50)
        log('SYSTEM', '智能骑行头盔系统 v1.0 启动')
        log('SYSTEM', '=' * 50)

        # ---------- 1. 初始化各管理模块 ----------
        self.sensor = SensorManager()
        self.gnss   = GnssManager()
        self.mqtt   = MqttManager()

        # ---------- 2. 启动 GNSS ----------
        self.gnss.start()

        # ---------- 3. 启动 4G 网络并连接 MQTT ----------
        if self.mqtt.start_network():
            self.mqtt.connect()

        # ---------- 4. 计时器变量 ----------
        self.last_env_time   = 0    # 上次环境数据上传时间
        self.last_beat_time  = 0    # 上次心跳包发送时间
        self.last_gnss_log_time = 0 # 上次打印 GNSS 日志时间

    # ------------------------------------------------------------------
    # 构建 MQTT 报文
    # ------------------------------------------------------------------

    def build_sensor_payload(self, acc, acc_total_g, env_data, light_v):
        """
        构建传感器数据 JSON 报文
        :param acc:          加速度字典 {'x', 'y', 'z'}
        :param acc_total_g:  合力幅值（单位：g）
        :param env_data:     环境数据字典 {'temp', 'humidity'} 或 None
        :param light_v:      光照电压值
        :return:             JSON 格式的字符串
        """
        data = OrderedDict()

        # -- 加速度数据 --
        data['acc_x'] = acc['x']
        data['acc_y'] = acc['y']
        data['acc_z'] = acc['z']
        data['acc_total_g'] = acc_total_g

        # -- 环境数据 --
        if env_data:
            data['temp']     = env_data['temp']
            data['humidity'] = env_data['humidity']
        data['light_v'] = light_v

        # -- GPS 位置 --
        if self.gnss.valid:
            data['lat'] = self.gnss.latitude
            data['lon'] = self.gnss.longitude
            data['speed'] = self.gnss.speed
        else:
            data['lat']  = 0.0
            data['lon']  = 0.0
            data['speed'] = 0.0

        # -- 时间戳 --
        data['timestamp'] = int(time.time())

        return json.dumps(data)

    def build_heartbeat_payload(self):
        """
        构建心跳包 JSON 报文
        :return: JSON 格式的字符串
        """
        data = OrderedDict()
        data['type']     = 'heartbeat'
        data['lat']      = self.gnss.latitude if self.gnss.valid else 0.0
        data['lon']      = self.gnss.longitude if self.gnss.valid else 0.0
        data['speed']    = self.gnss.speed
        data['gps_valid'] = self.gnss.valid
        data['timestamp'] = int(time.time())
        return json.dumps(data)

    # ------------------------------------------------------------------
    # 主循环
    # ------------------------------------------------------------------

    def run(self):
        """
        系统主循环
        执行以下任务（各自按独立周期运行）：
          1. 每 100ms 读取加速度数据
          2. 每 1s 更新 GNSS 定位
          3. 每 2s 上传温湿度 + 光照 + 加速度 + GPS 数据
          4. 每 10s 发送心跳包
        """
        log('SYSTEM', '系统主循环开始运行')

        # 主循环计数（调试用）
        loop_count = 0

        try:
            while True:
                loop_count += 1
                current_time = time.time()

                # =========================================================
                # 任务 1：读取加速度数据（每次循环都执行，约 10Hz）
                # =========================================================
                acc = self.sensor.read_acceleration()
                acc_total_g = self.sensor.calc_acc_total(acc)

                # =========================================================
                # 任务 2：更新 GNSS 定位（每 1 秒执行一次）
                # =========================================================
                if current_time - self.last_gnss_log_time >= Config.GNSS_INTERVAL:
                    self.gnss.update()
                    self.last_gnss_log_time = current_time

                    # 打印 GNSS 日志（方便调试）
                    if self.gnss.valid:
                        log('GNSS', '定位有效: {}'.format(self.gnss.get_position_str()))
                    else:
                        log('GNSS', '定位中... 已运行 {}s'.format(int(current_time)))

                # =========================================================
                # 任务 3：上传环境 + 加速度 + GPS 完整数据（每 2 秒）
                # =========================================================
                if current_time - self.last_env_time >= Config.ENV_INTERVAL:
                    # 读取温湿度
                    env_data = self.sensor.read_temperature_humidity()
                    # 读取光照
                    light_v = self.sensor.read_light()
                    # 构建 JSON 报文
                    payload = self.build_sensor_payload(acc, acc_total_g, env_data, light_v)
                    # 打印到控制台
                    log('UPLOAD', '传感器数据: {}'.format(payload))
                    # 通过 MQTT 上传
                    self.mqtt.publish(Config.TOPIC_SENSOR, payload)
                    # 更新时间戳
                    self.last_env_time = current_time

                # =========================================================
                # 任务 4：发送心跳包（每 10 秒）
                # =========================================================
                if current_time - self.last_beat_time >= Config.HEARTBEAT_INTERVAL:
                    payload = self.build_heartbeat_payload()
                    log('HEARTBEAT', '心跳包: {}'.format(payload))
                    self.mqtt.publish(Config.TOPIC_STATUS, payload)
                    self.last_beat_time = current_time

                # =========================================================
                # 任务 5：检查 MQTT 下行消息（非阻塞）
                # =========================================================
                self.mqtt.check_msg()

                # =========================================================
                # 控制主循环频率：延时 100ms（即 10Hz）
                # =========================================================
                time.sleep(Config.SENSOR_INTERVAL)

        except KeyboardInterrupt:
            # 用户按 Ctrl+C 时优雅退出
            log('SYSTEM', '收到中断信号，正在停止系统...')

        except Exception as e:
            log('SYSTEM', '主循环异常: {}'.format(e))

        finally:
            # ---------- 清理资源 ----------
            log('SYSTEM', '正在清理资源...')
            self.gnss.stop()
            self.mqtt.disconnect()
            log('SYSTEM', '系统已停止')


# ====================================================================
# 第七部分：程序入口
# ====================================================================

def main():
    """
    主函数入口
    创建 DataCollector 实例并启动主循环
    """
    collector = DataCollector()
    collector.run()


# 当此文件作为主程序运行时，执行 main()
if __name__ == '__main__':
    main()
