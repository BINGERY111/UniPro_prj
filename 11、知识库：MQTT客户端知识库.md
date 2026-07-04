# 移远umqtt MQTT客户端API知识库（适配Vibe-Coding）
## 文档基础元信息
```json
{
  "vendor": "移远通信 QUECTEL",
  "doc_name": "umqtt-MQTT客户端API参考手册",
  "version": "V1.0",
  "release_date": "2026-01-12",
  "language": "Python(嵌入式MicroPython)",
  "core_module": ["umqtt.simple", "umqtt.robust"],
  "support_feature": ["MQTT3.1.1基础发布订阅", "QoS0/QoS1", "TLS单向/双向加密", "自动重连(robust)", "阻塞/非阻塞消息接收"],
  "limitation": "文档FTP章节书签丢失，无FTP相关可用API；仅支持Python嵌入式环境"
}
```

## 一、模块总览
### 1. umqtt整体介绍
`umqtt`是移远基于Python实现的**轻量级嵌入式MQTT客户端**，专为物联网低带宽设备设计，分为两个子模块：
1. `umqtt.simple`：基础MQTT客户端，手动处理断线重连，轻量无额外容错
2. `umqtt.robust`：增强客户端，内置自动重连、异常恢复，API与simple完全兼容

### 2. MQTT协议核心特性
- 头部最小2字节，超低流量开销
- 发布/订阅一对多模型
- QoS分级：0(最多一次)、1(至少一次)
- 适配低功耗电池设备
- 支持TLS加密传输防窃听、中间人攻击

## 二、umqtt.simple 完整API手册
### 3.1 构造函数 MQTTClient
#### 接口说明
创建MQTT客户端实例
#### 函数原型
```python
class umqtt.simple.MQTTClient(client_id, server, port=0, user=None, password=None, keepalive=0, ssl=None)
```
#### 参数表
| 参数 | 必填 | 类型 | 默认值 | 说明 |
|------|------|------|--------|------|
| client_id | 是 | str | - | 设备唯一客户端ID，重复会被服务端踢下线 |
| server | 是 | str | - | MQTT服务器IP/域名 |
| port | 否 | int | 0 | 0自动适配：1883(明文) / 8883(TLS)；可手动指定端口 |
| user | 否 | str | None | 服务端鉴权用户名 |
| password | 否 | str | None | 服务端鉴权密码 |
| keepalive | 否 | int | 0 | 心跳保活秒数，0=禁用心跳 |
| ssl | 否 | tls.SSLContext | None | TLS加密上下文对象，None=明文连接 |

#### 返回值
MQTTClient 客户端对象
#### 代码示例
```python
from umqtt import simple
# 明文客户端初始化
client = simple.MQTTClient(
    client_id="device_001",
    server="mqtt.eclipseprojects.io",
    port=1883
)
```

### 3.2 connect() 连接服务端
#### 接口说明
建立MQTT TCP连接，完成握手
#### 函数原型
```python
MQTTClient.connect(clean_session=True, timeout=None)
```
#### 参数
| 参数 | 必填 | 类型 | 默认 | 说明 |
|------|------|------|------|------|
| clean_session | 否 | bool | True | True：断开后清空订阅会话；False：保留离线消息 |
| timeout | 否 | int | None | 连接超时秒数 |

#### 返回值
成功返回`session_present`(bool会话标识)；失败直接抛出异常
#### 示例
```python
try:
    session = client.connect()
    print("连接成功，会话状态：", session)
except Exception as e:
    print("连接失败：", e)
```

### 3.3 disconnect() 断开连接
#### 原型
```python
MQTTClient.disconnect()
```
#### 参数：无
#### 返回：无
#### 示例
```python
client.disconnect()
```

### 3.4 publish() 发布消息
#### 原型
```python
MQTTClient.publish(topic, msg, retain=False, qos=0)
```
#### 参数
| 参数 | 必填 | 类型 | 默认 | 说明 |
|------|------|------|------|------|
| topic | 是 | str/bytes | - | 发布主题，推荐bytes提升兼容性 |
| msg | 是 | str/bytes | - | 消息载荷 |
| retain | 否 | bool | False | True：服务端保留该主题最新消息，新订阅设备上线立即接收 |
| qos | 否 | int | 0 | 0最多一次，1至少一次 |

#### 返回：无
#### 示例
```python
# QoS1 上传传感器数据
client.publish(b"sensors/temp", b"25.6", qos=1)
# 保留消息
client.publish("device/status", "online", retain=True)
```

### 3.5 subscribe() 订阅主题
#### 原型
```python
MQTTClient.subscribe(topic, qos=0)
```
#### 参数
| 参数 | 必填 | 类型 | 默认 |
|------|------|------|------|
| topic | 是 | str/bytes | 订阅主题，支持`#`通配符 |
| qos | 否 | int | 0 |

#### 配套回调函数：set_callback(func)
必须注册回调才能接收订阅消息，回调固定入参 `(topic, msg)`，均为bytes类型
#### 完整示例
```python
# 定义消息回调
def msg_cb(topic, msg):
    print("收到主题：", topic.decode())
    print("消息内容：", msg.decode())

# 绑定回调
client.set_callback(msg_cb)
# 订阅全量传感器主题
client.subscribe(b"sensors/#", qos=1)
client.subscribe("control/device001")
```

### 3.6 wait_msg() 阻塞轮询消息
#### 接口
阻塞等待，直到收到订阅消息才返回，适合单线程纯MQTT业务
#### 原型
```python
MQTTClient.wait_msg()
```
#### 参数：无
#### 返回：内部操作码
#### 示例
```python
# 持续阻塞接收消息
while True:
    client.wait_msg()
```

### 3.7 check_msg() 非阻塞轮询消息
#### 接口
无阻塞检测消息，无消息立即返回None，适合多业务并发（定时采集+MQTT）
#### 原型
```python
MQTTClient.check_msg()
```
#### 返回：有消息返回操作码，无消息返回None
#### 示例
```python
import time
while True:
    op = client.check_msg()
    if op is None:
        time.sleep(0.1) # 空闲休眠降低功耗
```

## 三、umqtt.robust 增强客户端
### 4.1 构造函数
原型、参数、返回值与`umqtt.simple.MQTTClient`**完全一致**
#### 导入与初始化示例
```python
from umqtt import robust
client = robust.MQTTClient(
    client_id="robust_device_001",
    server="mqtt.eclipseprojects.io"
)
```
### 4.2 接口说明
`robust`封装了断线自动重连、网络异常重试、会话恢复逻辑，其余API（connect/publish/subscribe/wait_msg等）调用方式与simple完全通用，业务代码几乎无需修改，仅切换导入模块即可提升稳定性。

## 四、TLS加密安全连接完整API
### 5.1 TLS整体说明
通过`tls.SSLContext`对象传入MQTTClient构造函数`ssl`参数开启加密，端口需改为8883；支持单向证书校验、双向客户端证书认证。

### 5.2 创建TLS上下文
#### 原型
```python
import tls
tls_context = tls.SSLContext(tls.PROTOCOL_TLS_CLIENT)
```

### 5.3 设置证书校验模式
#### 枚举值
1. `tls.CERT_NONE`：不校验服务端证书（不安全，测试专用）
2. `tls.CERT_REQUIRED`：强制校验CA证书（生产环境推荐）
#### 示例
```python
tls_context.verify_mode = tls.CERT_REQUIRED
```

### 5.4 加载CA根证书（单向加密必备）
#### 原型
```python
tls_context.load_verify_locations(cadata)
```
#### 参数
`cadata`：PEM格式CA证书完整字符串
#### 示例
```python
ca_pem = """-----BEGIN CERTIFICATE-----
MIIFkjCCA3qgAwIBAgIQBQ3aPQqNQmT4C5N4Lp1OJzANBgkqhkiG9w0BAQsFADBh
MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3
d3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VcnQgR2xvYmFsIFJvb3QgRzI
...
-----END CERTIFICATE-----"""
tls_context.load_verify_locations(ca_pem)
```

### 5.5 加载客户端证书+私钥（双向TLS认证）
#### 原型
```python
tls_context.load_cert_chain(cert, key)
```
#### 参数
- cert：客户端PEM证书字符串
- key：客户端私钥PEM字符串
#### 完整双向TLS初始化示例
```python
import tls
from umqtt.simple import MQTTClient

# 1. 创建TLS上下文
ctx = tls.SSLContext(tls.PROTOCOL_TLS_CLIENT)
ctx.verify_mode = tls.CERT_REQUIRED

# 2. 加载CA根证书
ca = """-----BEGIN CERTIFICATE----- ... -----END CERTIFICATE-----"""
ctx.load_verify_locations(ca)

# 3. 加载客户端证书私钥
client_cert = """-----BEGIN CERTIFICATE----- ... -----END CERTIFICATE-----"""
client_key = """-----BEGIN PRIVATE KEY----- ... -----END PRIVATE KEY-----"""
ctx.load_cert_chain(client_cert, client_key)

# 4. 创建TLS加密MQTT客户端，端口8883
mqtt_client = MQTTClient(
    client_id="tls_device_001",
    server="mqtt.example.com",
    port=8883,
    ssl=ctx
)
```

## 五、通用开发规范（Vibe-Coding智能提示专用）
### 1. 编码规范
1. 主题、消息优先使用`bytes(b"xxx")`，避免嵌入式编码解码异常
2. 生产环境必须开启TLS+CERT_REQUIRED证书校验
3. 高稳定性场景使用`umqtt.robust`替代simple
4. 低功耗设备使用`check_msg()`非阻塞轮询，搭配sleep休眠
5. 所有connect/publish操作增加try-except捕获网络异常

### 2. 完整可运行Demo模板（明文simple）
```python
from umqtt.simple import MQTTClient
import time

# 配置常量
MQTT_ID = "dev_001"
MQTT_SERVER = "mqtt.eclipseprojects.io"
MQTT_PORT = 1883
SUB_TOPIC = b"control/dev_001"
PUB_TOPIC = b"sensors/data"

# 消息回调
def on_msg(topic, payload):
    print(f"Recv [{topic.decode()}]: {payload.decode()}")

# 初始化客户端
client = MQTTClient(MQTT_ID, MQTT_SERVER, port=MQTT_PORT)
client.set_callback(on_msg)

# 连接订阅
try:
    client.connect()
    client.subscribe(SUB_TOPIC, qos=1)
    print("MQTT连接成功")
except Exception as e:
    print("连接失败", e)

# 主循环
while True:
    client.check_msg()
    # 定时上报数据
    client.publish(PUB_TOPIC, b"temp:26,humi:55", qos=1)
    time.sleep(5)
```

### 3. 完整TLS加密Demo模板
```python
from umqtt.simple import MQTTClient
import tls
import time

# TLS配置
ca_content = """-----BEGIN CERTIFICATE-----
# 填入CA证书完整内容
-----END CERTIFICATE-----"""

# 构建TLS上下文
tls_ctx = tls.SSLContext(tls.PROTOCOL_TLS_CLIENT)
tls_ctx.verify_mode = tls.CERT_REQUIRED
tls_ctx.load_verify_locations(ca_content)

# TLS MQTT客户端
client = MQTTClient(
    client_id="tls_dev_001",
    server="mqtt.example.com",
    port=8883,
    ssl=tls_ctx
)

def callback(t, m):
    print(t.decode(), m.decode())

client.set_callback(callback)
client.connect()
client.subscribe(b"device/cmd")

while 1:
    client.check_msg()
    time.sleep(0.2)
```

## 六、异常与限制知识库
1. 文档FTP章节全部书签失效，无可用FTP文件操作API，项目中不可调用ftp相关接口
2. client_id必须全局唯一，相同ID同时在线会互相踢下线
3. keepalive=0时服务端不会主动检测死连接，建议设置30~120秒心跳
4. QoS仅支持0、1，不支持MQTT QoS2
5. TLS证书必须传入完整PEM字符串，不支持文件路径加载证书
6. 断开后`clean_session=True`会丢失所有离线消息，需要离线缓存消息设置`clean_session=False`

## 七、Vibe-Coding提示标签（可直接用于代码补全规则）
```
# 触发关键词
umqtt.simple MQTTClient connect publish subscribe wait_msg check_msg umqtt.robust tls.SSLContext load_verify_locations load_cert_chain TLS MQTT 移远 模组MQTT
# 补全优先级规则
1. 先提示robust模块（生产推荐）
2. TLS相关接口自动补全CA证书模板
3. publish/subscribe自动填充bytes主题示例
4. 自动插入try-except异常捕获模板
5. 区分阻塞wait_msg/非阻塞check_msg使用场景注释
```