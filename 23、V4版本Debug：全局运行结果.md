>>> %Run -c $EDITOR_CONTENT

MPY: sync filesystems
MPY: soft reboot
[836492425] [SYSTEM] ==================================================
[836492425] [SYSTEM] 智能骑行头盔系统 v4.0 启动
[836492425] [SYSTEM] ==================================================
[836492425] [I2C] I2C 总线初始化完成，频率 400000Hz
[836492425] [LIS2DH12] 加速度计初始化完成
[836492425] [AHT20] 温湿度传感器初始化完成
[836492425] [ADC] 光敏电阻 ADC 初始化完成，引脚 C5
[836492425] [I2C] 扫描到设备: ['0x19', '0x38']
1970-01-01 00:04:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4960]		sendline: ATI.
1970-01-01 00:04:53 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4960]	execute command (ATI) timeout (5000 ticks)!
1970-01-01 00:04:53 [ERR  ]  [ql_net.c  ]	[ql_net_query_moudle_model():52][4960]	ATI query failed.
Network initialized
[836492430] [NET] 4G 模块初始化完成
1970-01-01 00:04:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4960]		sendline: AT+CPIN?.
1970-01-01 00:04:56 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4960]	execute command (AT+CPIN?) timeout (3000 ticks)!
1970-01-01 00:04:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4960]		sendline: AT+CPIN?.
1970-01-01 00:05:01 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4960]	execute command (AT+CPIN?) timeout (3000 ticks)!
1970-01-01 00:05:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4960]		sendline: AT+CPIN?.
1970-01-01 00:05:06 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4960]	execute command (AT+CPIN?) timeout (3000 ticks)!
[836492446] [NET] SIM 卡状态: False
[836492446] [NET] SIM 卡未检测到，跳过网络附着
[836492446] [NET] 网络未就绪，系统将在无网络模式下运行核心功能
[836492446] [GNSS] GNSS 模块对象创建成功
1970-01-01 00:05:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4960]		sendline: AT+QGPS=1.
1970-01-01 00:05:11 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4960]	execute command (AT+QGPS=1) timeout (3000 ticks)!
1970-01-01 00:05:11 [ERR  ]  [mp_gnss.c ]	[quectel_gnss_start():45][4960]	gnss start failed
[836492449] [GNSS] 定位模块启动失败
[836492449] [GNSS] GNSS 启动失败，定位不可用
[836492449] [SMS] 使用 quectel.SMS 发送短信
[836492449] [SMS] 短信管理器初始化完成
[836492449] [BUZZER] 无外接蜂鸣器（使用板载 LED 替代声光提示）
[836492449] [BUTTON] 按键初始化完成（下降沿中断，200ms 软件消抖）
[836492449] [LCD] LCD 初始化完成（ST7735, 160x80, v4.2 卡片式 UI）
[836492451] [STATE] 碰撞检测状态机初始化完成（五状态FSM）
[836492451] [SYSTEM] 所有模块初始化完成，准备启动双线程并发框架
[836492451] [SYSTEM] 启动单线程系统（采集 + 检测 + 通信合并到主线程）
[836492451] [THREAD] 单线程系统已启动（采集 + 检测 + 通信合并）
1970-01-01 00:05:14 [ERR  ]  [at_client.c]	[at_obj_exec_cmd():365][4960]	input AT Client object is NULL, please create or get AT Client object!
1970-01-01 00:05:14 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4960]	GNSS get location failed, error code: 549
[836492451] [UPLOAD] 数据包: {"温度": "28.0℃", "湿度": "50.6%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
[836492451] [MQTT] MQTT 已断线，尝试重连...
[836492451] [TLS] 成功读取证书文件: /flash/connectlab_rsa_ca.cer
[836492451] [TLS] 成功读取证书文件: /flash/connectlab_rsa_client_tmp.cer
[836492451] [TLS] 成功读取证书文件: /flash/connectlab_rsa_client_tmp.key
[836492451] [TLS] SSL 上下文配置成功
[836492451] [MQTT] 配置: 172.188.83.251:44103  SSL=TLS  user=quectel
[836492451] [MQTT] 正在连接 172.188.83.251:44103...
1970-01-01 00:05:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4948]		sendline: AT+QIDNSGIP=1,"172.188.83.251".
1970-01-01 00:05:19 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4948]	execute command (AT+QIDNSGIP=1,"172.188.83.251") timeout (5000 ticks)!
1970-01-01 00:05:19 [ERR  ]  [ql_socket.c]	[ql_getaddrinfo():888][4948]	get addr failed
[836492457] [MQTT] MQTT 连接失败: [Errno 2] ENOENT
[836492457] [MQTT] 尝试非 TLS 端口 42605...
1970-01-01 00:05:19 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4948]		sendline: AT+QIDNSGIP=1,"172.188.83.251".
1970-01-01 00:05:24 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4948]	execute command (AT+QIDNSGIP=1,"172.188.83.251") timeout (5000 ticks)!
1970-01-01 00:05:24 [ERR  ]  [ql_socket.c]	[ql_getaddrinfo():888][4948]	get addr failed
[836492462] [MQTT] 非 TLS 连接也失败: [Errno 2] ENOENT
HardFault
R0    31000000
R1    00000000
R2    00000000
R3    00000000
R12   0807181f
SP    2000eff0
LR    080a9067
PC    080a3b86
XPSR  61000000
HFSR  40000000
CFSR  00008200
BFAR  3100000c
Stack:
  2000eff0  31000000
  2000eff4  00000000
  2000eff8  00000000
  2000effc  00000000
  2000f000  0807181f
  2000f004  080a9067
  2000f008  080a3b86
  2000f00c  61000000
  2000f010  00000000
  2000f014  00000000
  2000f018  00000000
  2000f01c  080d8e13
  2000f020  2000f02c
  2000f024  200164d0
  2000f028  000007f1
  2000f02c  00000000
  2000f030  2000f00c
  2000f034  00000000
  2000f038  000007f1
  2000f03c  200164d0
  2000f040  20029700
  2000f044  080d8ee0
  2000f048  2000f10c
  2000f04c  2000f0f8
  2000f050  00000001
  2000f054  00000000
  2000f058  00000000
  2000f05c  00000001
  2000f060  200108e8
  2000f064  080a9067
  2000f068  2002fb50
  2000f06c  00000000

FATAL ERROR:
HardFault
