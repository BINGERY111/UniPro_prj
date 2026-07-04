MPY: sync filesystems
MPY: soft reboot
[836384183] [SYSTEM] ==================================================
[836384183] [SYSTEM] 智能骑行头盔系统 v3.0 启动
[836384183] [SYSTEM] ==================================================
[836384183] [I2C] I2C 总线初始化完成，频率 400000Hz
[836384183] [LIS2DH12] 加速度计初始化完成
[836384183] [AHT20] 温湿度传感器初始化完成
[836384183] [ADC] 光敏电阻 ADC 初始化完成，引脚 C5
[836384183] [I2C] 扫描到设备: ['0x19', '0x38']
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4992]		sendline: ATI.
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: Quectel..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: EC200U..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: Revision: EC200UCNAAR03A15M08..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: OK..
2026-07-03 08:56:14 [INFO ]  [ql_module_compat.c]	[ql_set_module_model():72][4992]	model = EC200U
Network initialized
[836384183] [NET] 4G 模块初始化完成
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4992]		sendline: AT+CPIN?.
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CPIN: READY..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: OK..
2026-07-03 08:56:14 [INFO ]  [ql_net.c  ]	[ql_net_query_sim_state():100][4992]	SIM card detected successfully
[836384183] [NET] SIM 卡状态: True
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4992]		sendline: AT+CREG?.
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CREG: 0,1..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: OK..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4992]		sendline: AT+CEREG?.
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CEREG: 0,1..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: OK..
2026-07-03 08:56:14 [INFO ]  [ql_net.c  ]	[ql_net_query_register_status():214][4992]	Network registration successful
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4992]		sendline: AT+QIACT?.
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +QIACT: 1,1,3,"10.46.73.41","2409:8D1E:1023:1B1B:18BE:A0EA:AEA9:AB47"..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: OK..
2026-07-03 08:56:14 [INFO ]  [ql_net.c  ]	[ql_net_query_actice_state():245][4992]	device IP address: 10.46.73.41
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4992]		sendline: AT+QNTP=1,"ntp.aliyun.com".
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: OK..
[836384183] [NET] 4G 网络附着完成
[836384183] [SYSTEM] 等待 NTP 时间同步...
2026-07-03 08:56:20 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:20 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +QNTP: 0,"2026/07/03,00:56:27+32"..
Setting RTC: 2026-07-03 08:56:27
[836384190] [MQTT] MQTT 连接尝试 1/3...
[836384190] [TLS] 成功读取证书文件: /flash/connectlab_rsa_ca.cer
[836384190] [TLS] 成功读取证书文件: /flash/connectlab_rsa_client_tmp.cer
[836384190] [TLS] 成功读取证书文件: /flash/connectlab_rsa_client_tmp.key
[836384191] [TLS] SSL 上下文配置成功
[836384191] [MQTT] 配置: 172.188.83.251:42605  TLS  user=quectel
[836384191] [MQTT] 正在连接 172.188.83.251:42605...
2026-07-03 08:56:31 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4984]		sendline: AT+QIDNSGIP=1,"172.188.83.251".
2026-07-03 08:56:31 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:31 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: OK..
2026-07-03 08:56:31 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:31 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +QIURC: "dnsgip",0,1,0..
2026-07-03 08:56:31 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:31 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +QIURC: "dnsgip","172.188.83.251"..
2026-07-03 08:56:31 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4984]		sendline: AT+QIOPEN=1,0,"TCP","172.188.83.251",42605,0,1.
2026-07-03 08:56:31 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:31 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: OK..
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +QIOPEN: 0,0..
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4912]		sendline: AT+QISEND=0,147.
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4912]		sendline: ...........1.5.|g..Z..M..PhS.....%.=p.*.*....&.,.0.$.(.....+./.#.'.......=.5...<./.....;........
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4912]		sendline: .172.188.83.251....................................
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +QIURC: "recv",0,1500..
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +QIURC: "recv",0,1001..
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4912]		sendline: AT+QISEND=0,823.
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4912]		sendline: ....2......+..(0..$0.....C........A8..T.\....0...*.H........0b1.0...U....XX1.0...U....XX1.0...U.
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4912]		sendline: ...XX1.0...U....Test1.0...U....Test1.0...U....ConnectLab Test CA0...260317064112Z..360314064112Z
2026-07-03 08:56:32 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4912]		sendline: 0;1.0...U....connectlab_client_test1.0...U....ConnectLab Test0.."0...*.H.............0.........5
2026-07-03 08:56:33 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4912]		sendline: $.V.'.....s...T.2...J.F....=f....|...W..Ja.pg.~.......l..3Qh..#...........}T...5.%.?.s.*..x.NT..
2026-07-03 08:56:33 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4912]		sendline: .=....b...=..C...DI.0...E..Z..YK...P..>......m...'.De..nd.....@W....r.6^u|...1+..)...?.=.Dm.MB~.
2026-07-03 08:56:33 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4912]		sendline: ..n....k'W~7.I.0..Z)..;w.......b.1.0".......3.w.\....U..P..W.;.....0...*.H................e.....
2026-07-03 08:56:33 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4912]		sendline: r..+..hZB..V....y.P....s..t._hL.....#\..c.Z......P..l:.L..#X17K{.l......K...~..........m...l.]f.
2026-07-03 08:56:33 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4912]		sendline: ...O&..........N:./.....*....;.l....,;}.aN.J).=..Q.QO..?S.c!vpS...>N|8.U.yY@G....sA......../3H..
2026-07-03 08:56:33 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4912]		sendline: .p.p.......O,y.a.)......^..|.?W.t..8.u\.......*.u.-..w.
2026-07-03 08:56:33 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:33 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:35 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4760]		sendline: AT+QISEND=0,75.
2026-07-03 08:56:35 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:35 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:35 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4760]		sendline: ....F...BA..9%u....Z.sX.....G~F..2C".8.FT.J._...;.../....[....c`.)...1.....
2026-07-03 08:56:35 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:35 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: AT+QISEND=0,269.
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: .............Q.]a..r.k.w...Y...K....m...}...6(S/....y.....'.#.b.Y2.~.......Yt.p0...U......AG..8.
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: .1n.K%.s.....am..3.R!s..z..@._...UL.?.......U....D....n.....,.|9......N.}]..c }?Q7.%...d|...Z...
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: ....J..Y.S..[.'...lSq...r`.....c.gI.=3joc..k-..?)...x[.......9.@.,....G...!.5
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: AT+QISEND=0,6.
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: ......
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: AT+QISEND=0,45.
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: ....(..........FH[.?.o......+...p;........1..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +QIURC: "recv",0,51..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: AT+QISEND=0,32.
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: ..............`..nP..N.V~..'.v..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: AT+QISEND=0,38.
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: ....!.........o.S...!I.f.O..X.V..5Y...
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: AT+QISEND=0,31.
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: .............6d.E..X..x......+.
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: AT+QISEND=0,42.
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:38 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: ....%.........K.2>:.Ad..+........X.m.~..:P
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: AT+QISEND=0,31.
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: ...............|......."@A.....
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: AT+QISEND=0,36.
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: .............LIVC...H.......Mj...R..
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: AT+QISEND=0,31.
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: ................:.o..j!.S.e.)[h
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: AT+QISEND=0,37.
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: .... .........M...c+...:B....5..w...&
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:39 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +QIURC: "recv",0,33..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
[836384199] [MQTT] MQTT 连接成功！
[836384199] [GNSS] GNSS 模块对象创建成功
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: AT+QGPS=1.
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: OK..
[836384199] [GNSS] 定位模块启动成功，等待卫星信号...
[836384199] [GNSS] GNSS 定位已启动
[836384199] [BUZZER] 无外接蜂鸣器（使用板载 LED 替代声光提示）
[836384199] [BUTTON] 按键初始化完成（下降沿中断，200ms 软件消抖）
[836384200] [LCD] LCD 初始化完成（ST7735, 160x80）
[836384200] [STATE] 碰撞检测状态机初始化完成（五状态FSM）
[836384200] [SYSTEM] 所有模块初始化完成，准备启动三线程并发框架
[836384200] [SYSTEM] 启动双线程并发框架...
[836384200] [THREAD] 通信/采集线程已启动（主线程，含 I2C 传感器读取）
[836384200] [THREAD] 碰撞检测线程已启动（50ms 轮询）
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:40 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4736]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:40 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4736]	GNSS get location failed, error code: 516
[836384200] [UPLOAD] 数据包: {"温度": "27.8℃", "湿度": "56.2%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: AT+QISEND=0,32.
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4736]		sendline: ..............U...9C.S`......VU.
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ................$UK%......^K.`6
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....).........d....7...A.L.....1&)6SDqDOB..I..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:40 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:56:41 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:41 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:41 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ..............^.,iF.V....-7r..Vue....G.m.W....x..._8.!.c......z.<...gl..f....8G.....0....eU3.../
2026-07-03 08:56:41 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .. ..@@....5......S..m8.~O......@./.n..4.:
2026-07-03 08:56:41 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:41 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:41 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:41 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:41 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:41 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:41 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +QGPS: "firmware",0,0..
[836384202] [UPLOAD] 数据包: {"温度": "27.8℃", "湿度": "56.2%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .................B...$Js..u.WI..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ...............Ns... 51C.v...`-
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....)........o...N..k...d/t.`....gU...\...d.J.
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .................Z..%d}...BSF.\.p.N.s........4....Y#o=....Z.\%~... ....6a./Dq...j...y.(..}......
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .b.B bT..bz.h..t..({..v.....%u"..4........
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:42 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:42 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:42 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:56:43 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:43 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:43 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:43 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:43 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384204] [UPLOAD] 数据包: {"温度": "27.8℃", "湿度": "56.2%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .............2.<....;....9a...|.
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ...............bF.aB.....f.....
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....)........&...R.O.......[~[......l..V6\.7..
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .............l..I?[R.|.^?...8.......0..v.<d.e[.o....6u.D..1..3....2..P...Lb...E.......,..D..=.y.
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ...k.y.1.I.Qg..i.`{.)..=a\........EE..J.4.
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:44 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:44 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:44 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:56:45 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:45 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:45 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:45 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:45 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384206] [UPLOAD] 数据包: {"温度": "27.8℃", "湿度": "56.2%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ..............`x..|,....i.:.|...
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ...................mvg*t.......
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....)........V.....u.Yh......w.C.&.E.+7....]2.
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .................e.{.!J....c.=tC...U4<h.a...U..?....&......uC...d@..Uj~..~....+T......C&x.>=.1..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ...,Cui.$.8Fv.L.....f<>.Y.....y.q..aR..I..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:46 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:46 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:56:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:47 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:47 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:48 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:48 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384208] [UPLOAD] 数据包: {"温度": "27.8℃", "湿度": "56.2%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .............j..H.{.* o.u....R..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .....................V_.....8..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....).............%#..T..m..]A.O..U..R..%..N..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .................!|\v....(...{....?&../....a2...%F..=.........NUt..r..s...r.....rv.[.....'...F..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: G....b..Z-4....@O..K4.$g...p......?.t..I*.
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:48 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:49 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:49 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:49 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:49 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:49 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:56:49 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:49 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:49 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:49 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:49 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384210] [UPLOAD] 数据包: {"温度": "27.8℃", "湿度": "56.2%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ...............M...BU.)....Z.<.v
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .......................]......g
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....).........J..Gy.T.." ....B................
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............ ....;.J]3.^.../....*.....A..P.n....^U..YXp.0..:5.=U.QR.s........+......."....(...X.
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: J(s...:....Rw*U25|..aK.5%2............k...
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:50 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:50 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:56:51 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:51 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:51 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:51 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:51 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384212] [UPLOAD] 数据包: {"温度": "27.8℃", "湿度": "56.1%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:56:51 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:56:51 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:51 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:51 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............!:|..d~..G..]h.V'..B
2026-07-03 08:56:51 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:51 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............".....]..)G...0.)/B
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....).......#.<..37o^\.m....Z....o7t&!..v..Whv
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............$..4I...e..g...n.........2..-s.[.I..]2Pb..z..y.. ..7......$&.,...|{.>..n...B..%..>..
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ..8B.d.r...l...,Jy..F.|...!..r.~....q.....
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:52 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:52 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:53 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:53 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384214] [UPLOAD] 数据包: {"温度": "27.8℃", "湿度": "56.1%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............%.y.....r9Ud).W...e!
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............&!(v..".......H..Hv
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....).......'.Q..n.E...[FH.C...+..2K.|..hn...x
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............(.S#_45....f......a.....!sI..W..).....+n....g.._w."?........|.^ .U.!s..G&"u..#.`.U..
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ..0..L..&...`.T...C...Z%,.5a.e.B..o..R_...
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:54 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:54 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384216] [UPLOAD] 数据包: {"温度": "27.8℃", "湿度": "56.1%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............)..^.k`.....!.,.;...
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............*..w..1G.G]....:...
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....).......+U.>.dO.Y.....W.n.....r[.av.......
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............,.4.aG7..v._.O.._..scH2&....G.Z.*...z6.q Kky...c.g.........)..+YW^_ .z.?.1..R.....z.
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: C......w..f]Ry...X..:.....N$.....V...w....
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:56 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:56 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:56:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:56 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:56 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384218] [UPLOAD] 数据包: {"温度": "27.9℃", "湿度": "56.2%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............-....KA...X.^.^+....
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .............&.0.t.yI......o_Q.
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....)......./......y;S"[..[.a.. .g.\.....U.,..
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............0h......Mt.....0:&.....3..c......z.?a.6..vs..3.....`..S@.q....C.[4..A..W.......2....
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: o..@N.cl?.....J....U..~.C%..R.0(W^..#..f..
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:58 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:58 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:56:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:58 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:58 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:56:59 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:56:59 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384220] [UPLOAD] 数据包: {"温度": "27.8℃", "湿度": "56.1%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............1D.V.....oH0........
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............2..cm.m....{3....~}
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....).......3c.T.WnLH.O...W9..:C.=..OK&...|.S.
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............4....E......m9p........=...*?,..h....P.(4.|...".'j.._...O..y.....!.&...u..(v....<.S.
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: t1....~.Sj[.r..5.p7.}.Y...2..V.9(.t}....B.
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:56:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:00 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:00 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:01 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:01 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384222] [UPLOAD] 数据包: {"温度": "27.9℃", "湿度": "56.2%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............5Kw;...^.....\.....h
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............6...(}....I..U....g
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....).......7.........6k......=.2........="...
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............8...&..w-b.....i..M9.+..g...N.........._..cB+._Y....U..FGv@.....p.I..A......o@.[....
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: B........ioE.J.Ix.G..Br.-p..W..7..;z#.....
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:02 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:02 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:03 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:03 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384224] [UPLOAD] 数据包: {"温度": "27.9℃", "湿度": "56.0%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............9.........@.W].i....
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............:..X....Du...^...&.
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....).......;..yr.2.......4..P..Oa......J...Jr
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............<...pNoT.s...Yx..-..NW7i}...........XA.Z...m......>..W.P.)...6.....-..Y ..0V.!|F...2
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .......5....2..v.K.*].`.<vs.i.p86...$.$.>9
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:04 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:04 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384226] [UPLOAD] 数据包: {"温度": "27.9℃", "湿度": "56.0%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............=WM.r.......Nf.?..Y.
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............>.....gC._%9w......
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....).......?..A..."e:.OS.?zX.G.9..".....'....
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............@.6.... K.A..5...4.03..-[$......pL....y..42..3.$.7...3...#..KjW..]..R....._..vS.l.j.
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ...V..,......H.....A.......6......q5$B.9..
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:05 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:05 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:57:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:06 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:06 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384228] [UPLOAD] 数据包: {"温度": "27.9℃", "湿度": "55.9%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............A<o.e*...o.t:....|3.
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............B.\.s.%b7..q.+|7...
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....).......C..:.Ymt.....F.N.I)..... (.2.h.&..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............D.E.rn.dh?....P.h.k..Y.Xs...1...n....;h0h.../....+z..,f......Rk..D..p..G......f.....
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .U....V.T.....?b.......^.D..eh...CC8W..i..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:07 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:07 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:57:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:08 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:08 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384230] [UPLOAD] 数据包: {"温度": "27.9℃", "湿度": "55.9%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:57:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............E"......N..(h4..52..
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............F.."S....._.H9C...q
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....).......G.9...'& 6{..{|"..2.>.N.W..k..W.l.
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............H#&.p.`IC..%......C....`....F.o.s..n k...1:)a..2(W'....#.!..fd2.}M..0.......u.....>.
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: .&.......^b?..G...=...E~...J_.......G.qPK.
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:09 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:09 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:57:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:10 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:10 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384232] [UPLOAD] 数据包: {"温度": "27.8℃", "湿度": "55.9%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:57:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:57:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............I....4]....5bPMy.4LY
2026-07-03 08:57:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............Js&..;.....^.aJ...e
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....).......K..&..........w.....b,...S..dg....
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............LAlP.o.B.^..L.T...8.....Q&.g..c._Ef.c....A......N.3.6.................{.C....h.)5.BW
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: 7.)V...95....[_p".2..5..<...X..U..i@c....I
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:11 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:11 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:57:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:12 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:12 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
2026-07-03 08:57:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:12 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:12 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516
[836384234] [UPLOAD] 数据包: {"温度": "27.8℃", "湿度": "55.9%", "状态": "正常", "GPS定位": "定位中...", "速度": "0.0m/s"}
2026-07-03 08:57:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,32.
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............MFJ..3.t.S...dW...7m
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,31.
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............N~.].R...I..}.....'
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,46.
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ....).......O....Ra..s....-#.e..I...-%....P$..
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QISEND=0,138.
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: >
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: ............P-.n.m...I...{..R....-0.R.'..1.C..$2?.\.Y.l....>ss....:...;.#.C...S..Ug+.H.7.......s
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: K....e=!....g5.%f..[.3..|$.D..j.p.....A...
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline:  ..
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: SEND OK..
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4560]		sendline: AT+QGPSLOC=2.
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: ..
2026-07-03 08:57:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2888]		recvline: +CME ERROR: 516..
2026-07-03 08:57:13 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4560]	execute command (AT+QGPSLOC=2) failed!
2026-07-03 08:57:13 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4560]	GNSS get location failed, error code: 516