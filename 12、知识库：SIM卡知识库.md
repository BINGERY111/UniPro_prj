# 移远Quectel MicroPython SMS-API 知识库（适配Vibe-Coding）
## 一、文档基础元信息
| 字段 | 内容 |
| ---- | ---- |
| 文档名称 | SMS-API参考手册.pdf |
| 厂商 | 上海移远通信QUECTEL |
| 文档版本 | V1.0 |
| 发布日期 | 2026-06-02 |
| 适用环境 | MicroPython 移远4G/5G模组 |
| 模块能力 | 仅支持**短信发送**；无短信接收/读取/删除接口 |
| 保密等级 | 受控临时文件 |
| 编制人 | Wells Li |
| 官方支持渠道 | 技术支持邮箱：support@quectel.com<br>销售咨询：info@quectel.com |

## 二、模块总览 quectel.SMS
### 1. 核心能力
提供MicroPython环境下模组文本短信发送接口，支持纯英文、数字、中文、中英文混合短信内容。
### 2. 生命周期流程
创建SMS实例 → 调用send()发送短信 → deinit()释放底层资源（必须收尾释放）

## 三、完整API接口定义（结构化，代码提示友好）
### 3.1 构造函数：quectel.SMS()
#### 接口说明
新建SMS对象实例，初始化短信底层资源
#### 函数原型
```python
sms = quectel.SMS()
```
#### 参数
无入参
#### 返回值
成功：SMS实例对象
#### 代码示例
```python
import quectel
# 实例化短信对象
sms = quectel.SMS()
```

### 3.2 发送接口：SMS.send(number, text)
#### 接口说明
向指定手机号发送文本短信，兼容中英文字符
#### 函数原型
```python
result = sms.send(number: str, text: str) -> bool
```
#### 参数表
| 参数名 | 必填 | 类型 | 默认值 | 说明 |
| ---- | ---- | ---- | ---- | ---- |
| number | 是 | str | 无 | 接收方完整手机号字符串 |
| text | 是 | str | 无 | 短信正文，支持中文/英文/数字混合 |
#### 返回值
- `True`：短信提交发送成功
- `False`：发送失败（网络/参数/模组异常）
#### 完整可运行示例
```python
from quectel import SMS

# 初始化短信模块
sms = SMS()
# 发送短信
ret = sms.send("13800138000", "Hello,你好！测试短信")
# 判断发送结果
if ret:
    print("短信发送成功")
else:
    print("短信发送失败")
# 释放资源
sms.deinit()
```

### 3.3 释放接口：SMS.deinit()
#### 接口说明
反初始化短信模块，释放模组底层短信通道资源，业务结束必须调用
#### 函数原型
```python
sms.deinit()
```
#### 参数
无入参
#### 返回值
无返回值
#### 使用示例
```python
from quectel import SMS
sms = SMS()
sms.send("13800138000", "测试消息")
# 释放资源
sms.deinit()
```

## 四、编码规范 & Vibe-Coding 智能提示规则
### 4.1 导入规范
推荐两种导入方式，IDE自动识别：
1. 全量导入
```python
import quectel
sms = quectel.SMS()
```
2. 按需导入（推荐，代码简洁）
```python
from quectel import SMS
sms = SMS()
```

### 4.2 编码约束（代码校验提示）
1. 手机号必须为字符串类型，禁止传入数字`13800138000`（报错），需`"13800138000"`
2. send两个参数均为必填，缺失任一参数抛出语法提示
3. 使用完成后必须调用`deinit()`，知识库添加静态检查提示：`检测到SMS实例未执行deinit释放资源`
4. 本模块**无接收短信、读取短信、删除短信API**，IDE提示屏蔽相关不存在方法

### 4.3 类型注解（适配Vibe-Coding类型推断）
```python
class SMS:
    def __init__(self) -> None: ...
    def send(self, number: str, text: str) -> bool: ...
    def deinit(self) -> None: ...
```

## 五、限制与注意事项（知识库告警提示）
1. 功能限制：仅支持发送，不支持收短信、读取存量短信、删除短信
2. 资源规范：每个SMS实例使用完毕必须执行`deinit()`释放通道，避免模组资源占用
3. 内容编码：接口内部自动兼容中文，无需手动转码
4. 文档免责提示：接口为移远参考API，实际产品需自行验证适配，文档更新不另行通知
5. 保密约束：API文档及底层驱动禁止未授权转发、商用复刻

## 六、完整标准业务模板（可直接复制运行）
```python
# Quectel MicroPython SMS 标准发送模板
from quectel import SMS

def send_sms(phone: str, content: str) -> bool:
    """
    封装短信发送工具函数
    :param phone: 接收手机号字符串
    :param content: 短信文本内容
    :return: 发送成功返回True，失败False
    """
    sms = SMS()
    try:
        res = sms.send(phone, content)
        return res
    finally:
        # 无论发送成功失败，强制释放资源
        sms.deinit()

# 调用示例
if __name__ == "__main__":
    status = send_sms("13800138000", "设备告警：温度异常！")
    print("发送状态：", "成功" if status else "失败")
```