>>> %Run -c $EDITOR_CONTENT

MPY: sync filesystems
MPY: soft reboot
[836438060] [SYSTEM] ==================================================
[836438060] [SYSTEM] 智能骑行头盔系统 v4.0 启动
[836438060] [SYSTEM] ==================================================
[836438060] [I2C] I2C 总线初始化完成，频率 400000Hz
[836438060] [LIS2DH12] 加速度计初始化完成
[836438060] [AHT20] 温湿度传感器初始化完成
[836438060] [ADC] 光敏电阻 ADC 初始化完成，引脚 C5
[836438060] [I2C] 扫描到设备: ['0x19', '0x38']
2026-07-03 23:54:20 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ATI.
2026-07-03 23:54:25 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4560]	execute command (ATI) timeout (5000 ticks)!
2026-07-03 23:54:25 [ERR  ]  [ql_net.c  ]	[ql_net_query_moudle_model():52][4560]	ATI query failed.
Network initialized
[836438065] [NET] 4G 模块初始化完成
2026-07-03 23:54:25 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+CPIN?.
2026-07-03 23:54:33 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4560]	execute command (AT+CPIN?) timeout (3000 ticks)!
2026-07-03 23:54:35 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+CPIN?.
2026-07-03 23:54:38 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4560]	execute command (AT+CPIN?) timeout (3000 ticks)!
[836438081] [NET] SIM 卡状态: False
2026-07-03 23:54:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+CREG?.
2026-07-03 23:54:43 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4560]	execute command (AT+CREG?) timeout (3000 ticks)!
2026-07-03 23:54:43 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+CEREG?.
2026-07-03 23:54:46 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4560]	execute command (AT+CEREG?) timeout (3000 ticks)!
2026-07-03 23:54:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+CREG?.
2026-07-03 23:54:51 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4560]	execute command (AT+CREG?) timeout (3000 ticks)!
2026-07-03 23:54:51 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+CEREG?.
2026-07-03 23:54:54 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4560]	execute command (AT+CEREG?) timeout (3000 ticks)!
2026-07-03 23:54:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+CREG?.
2026-07-03 23:54:59 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4560]	execute command (AT+CREG?) timeout (3000 ticks)!
2026-07-03 23:54:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+CEREG?.
2026-07-03 23:55:02 [WARN ]  [at_client.c]	[at_obj_exec_cmd():407][4560]	execute command (AT+CEREG?) timeout (3000 ticks)!
2026-07-03 23:55:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+CREG?.

