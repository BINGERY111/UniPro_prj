MPY: sync filesystems
MPY: soft reboot
[836346467] [SYSTEM] ==================================================
[836346467] [SYSTEM] 智能骑行头盔系统 v1.0 启动
[836346467] [SYSTEM] ==================================================
[836346467] [I2C] I2C 总线初始化完成，频率 400000Hz
[836346467] [LIS2DH12] 加速度计初始化完成
[836346467] [AHT20] 温湿度传感器初始化完成
[836346467] [ADC] 光敏电阻 ADC 初始化完成，引脚 C5
[836346467] [I2C] 扫描到设备: ['0x19', '0x38']
[836346467] [GNSS] GNSS 模块对象创建成功
2026-07-02 22:27:45 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPS=1.
2026-07-02 22:27:45 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:45 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: OK..
[836346467] [GNSS] 定位模块启动成功，等待卫星信号...
2026-07-02 22:27:45 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ATI.
2026-07-02 22:27:45 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:45 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: Quectel..
2026-07-02 22:27:45 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: EC200U..
2026-07-02 22:27:45 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: Revision: EC200UCNAAR03A15M08..
2026-07-02 22:27:45 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:45 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: OK..
2026-07-02 22:27:45 [INFO ]  [ql_module_compat.c]	[ql_set_module_model():72][4696]	model = EC200U
Network initialized
[836346467] [NET] 4G 模块初始化完成
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+CPIN?.
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CPIN: READY..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: OK..
2026-07-02 22:27:46 [INFO ]  [ql_net.c  ]	[ql_net_query_sim_state():100][4696]	SIM card detected successfully
[836346467] [NET] SIM 卡状态: True
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+CREG?.
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CREG: 0,1..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: OK..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+CEREG?.
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CEREG: 0,1..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: OK..
2026-07-02 22:27:46 [INFO ]  [ql_net.c  ]	[ql_net_query_register_status():214][4696]	Network registration successful
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QIACT?.
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +QIACT: 1,1,3,"10.28.33.36","2409:8D1E:750C:DFA4::1"..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: OK..
2026-07-02 22:27:46 [INFO ]  [ql_net.c  ]	[ql_net_query_actice_state():245][4696]	device IP address: 10.28.33.36
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QNTP=1,"ntp.aliyun.com".
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: OK..
[836346467] [NET] 4G 网络附着完成
[836346467] [TLS] 成功读取证书文件: /flash/connectlab_rsa_ca.cer
[836346467] [TLS] 成功读取证书文件: /flash/connectlab_rsa_client_tmp.cer
[836346467] [TLS] 成功读取证书文件: /flash/connectlab_rsa_client_tmp.key
[836346467] [TLS] SSL 上下文配置成功
[836346467] [MQTT] 配置: 172.188.83.251:43719  TLS  user=quectel
[836346467] [MQTT] 正在连接 172.188.83.251:43719...
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QIDNSGIP=1,"172.188.83.251".
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: OK..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +QIURC: "dnsgip",0,1,0..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +QIURC: "dnsgip","172.188.83.251"..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QIOPEN=1,0,"TCP","172.188.83.251",43719,0,1.
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: OK..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +QIOPEN: 0,0..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,147.
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ...........1..d........f..O.w<.. .k.......l..&.,.0.$.(.....+./.#.'.......=.5...<./.....;........
2026-07-02 22:27:46 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .172.188.83.251....................................
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +QIURC: "recv",0,1500..
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +QIURC: "recv",0,1001..
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,823.
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....2......+..(0..$0.....C........A8..T.\....0...*.H........0b1.0...U....XX1.0...U....XX1.0...U.
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ...XX1.0...U....Test1.0...U....Test1.0...U....ConnectLab Test CA0...260317064112Z..360314064112Z
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: 0;1.0...U....connectlab_client_test1.0...U....ConnectLab Test0.."0...*.H.............0.........5
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: $.V.'.....s...T.2...J.F....=f....|...W..Ja.pg.~.......l..3Qh..#...........}T...5.%.?.s.*..x.NT..
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .=....b...=..C...DI.0...E..Z..YK...P..>......m...'.De..nd.....@W....r.6^u|...1+..)...?.=.Dm.MB~.
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ..n....k'W~7.I.0..Z)..;w.......b.1.0".......3.w.\....U..P..W.;.....0...*.H................e.....
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: r..+..hZB..V....y.P....s..t._hL.....#\..c.Z......P..l:.L..#X17K{.l......K...~..........m...l.]f.
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ...O&..........N:./.....*....;.l....,;}.aN.J).=..Q.QO..?S.c!vpS...>N|8.U.yY@G....sA......../3H..
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .p.p.......O,y.a.)......^..|.?W.t..8.u\.......*.u.-..w.
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:47 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +QGPS: "firmware",0,0..
2026-07-02 22:27:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,75.
2026-07-02 22:27:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....F...BA........cg.D._....i...F.8.....2.k.i."..,.u....P.......3l..ayD..6.
2026-07-02 22:27:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:50 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +QNTP: 0,"2026/07/02,14:27:52+32"..
Setting RTC: 2026-07-02 22:27:52
2026-07-02 22:27:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,269.
2026-07-02 22:27:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:52 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .............2.)v....h....kt..../.#5.......\.dm...."....).....X*).4.v.f..w\0..t...G%.....b...E#J
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ..R.a...O.2.XQ..................N..=2..tW..LA.....x....f\``?......E.O.3..i.Hw..t..F...i..6.o.j..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ..g...Xs[.&.....9.H^^3...KF.....q.%.$....N..)W...<....N...)... .W.oN.9 ...#..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,6.
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ......
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,45.
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....(.........<%Q......@H8...............j...
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +QIURC: "recv",0,51..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,32.
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....................&y.......*tg
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,38.
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....!............7...._.......=.#.....
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ..............c.~B.(.2:.......w
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,42.
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....%................3rU7.OV...E*....l+.t.
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ................g.......ZE.]...
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:53 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,36.
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ..............$0Z.@...9...c.F.......
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ...............pHG....(..Z..IFP
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,37.
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .... .........+.D.#...5A._.j:........
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +QIURC: "recv",0,33..
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
[836346474] [MQTT] MQTT 连接成功！
[836346474] [SYSTEM] 系统主循环开始运行
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:54 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:27:54 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:27:55 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346474] [GNSS] 定位中... 已运行 836346474s
[836346474] [UPLOAD] 传感器数据: {"acc_x": 0.077, "acc_y": -0.077, "acc_z": 9.425, "acc_total_g": 0.96, "temp": 25.9, "humidity": 52.8, "light_v": 1.393, "lat": 0.0, "lon": 0.0, "speed": 0.0, "timestamp": 836346474}
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,32.
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ..............'....+.J.....~96@.
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ...............g.8..~...5gV....
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....)........"..=.v../~...{.x......R.6.d....K^
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,211.
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ...............5U..Cs<b.o.UJ.....4...q...V..P..=........e.....0&...+V.R..J8....K.........K....p.
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .!.{...`f.w.......+d........n2.w:.c...#..pn...i.........#..?.4<E..O.U....`..7.........K...4..&..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: #..m.?...*....OMy|.
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
[836346475] [HEARTBEAT] 心跳包: {"type": "heartbeat", "lat": 0.0, "lon": 0.0, "speed": 0.0, "gps_valid": false, "timestamp": 836346475}
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ..............b..7...JZ...;...x
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .............|}...$...(,...IL:.
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....).........V.........>?s.X.=...$..a ..qK...
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,132.
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .............H..A.8.ff.....)o...U.......;<...V..f$......W..........G/L..Zj..)l..[....(0<.}...M..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ..R.lB.S...Q.8.~[%[P...Xf}..6..0O.|1
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:55 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:27:56 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:27:56 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346475] [GNSS] 定位中... 已运行 836346475s
[0;37m2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:27:56 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:27:56 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346476] [GNSS] 定位中... 已运行 836346476s
[836346476] [UPLOAD] 传感器数据: {"acc_x": 0.096, "acc_y": -0.134, "acc_z": 9.425, "acc_total_g": 0.96, "temp": 25.8, "humidity": 52.8, "light_v": 1.363, "lat": 0.0, "lon": 0.0, "speed": 0.0, "timestamp": 836346476}
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,32.
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ..................-..#.....y".M.
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .................Z.HZ}9...!....
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....)....................a...6...?F....P0.Q...
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,211.
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .............k4.U....M.n5..r....'....]..;.]..o...Sl.......(.PQ..-.3..X.9n.3..Q.G.-.r...2..!.....
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ........c.2Z....#e...#X..e&]`..}....z..x...4ag.j..C.j....2x...[7./...]x.,.!Xcx%,....6..0.....i..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: F..2.6.)..p.cp.....
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:56 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:27:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:57 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:27:57 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:27:57 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346477] [GNSS] 定位中... 已运行 836346477s
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:27:58 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:27:58 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346478] [GNSS] 定位中... 已运行 836346478s
[836346478] [UPLOAD] 传感器数据: {"acc_x": 0.096, "acc_y": -0.057, "acc_z": 9.444, "acc_total_g": 0.96, "temp": 25.9, "humidity": 52.7, "light_v": 1.264, "lat": 0.0, "lon": 0.0, "speed": 0.0, "timestamp": 836346478}
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,32.
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ..............K..g[...Q...0.4..>
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .............,.6..../.Ks.AO.%).
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....)..............A......j/.......v...w. .*..
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,211.
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ..............V2.o..=..M..7...U...tX..."..L.5.....)....R\.$....}\D7e....j.X..UQo>s5Cbm...B.....p
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ...I..R|.i....w.H..l..m..;A'...J.2...5-...2C......F..Q(0.R..7mM=2.6=m-d+..`c.......[..Ls<J..@0Ox
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: s.../......P.....t-
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:27:58 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:27:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:27:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:27:59 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:27:59 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:27:59 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346479] [GNSS] 定位中... 已运行 836346479s
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:00 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:00 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346480] [GNSS] 定位中... 已运行 836346480s
[836346480] [UPLOAD] 传感器数据: {"acc_x": 0.096, "acc_y": -0.115, "acc_z": 9.444, "acc_total_g": 0.96, "temp": 25.9, "humidity": 52.8, "light_v": 1.3, "lat": 0.0, "lon": 0.0, "speed": 0.0, "timestamp": 836346480}
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,32.
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .....................vWVp3.....>
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ..............._..&.q..{.:5.\.>
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....).........(L.N.h....@......+SH8.%..T.....f
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,209.
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .............6..z..v.[.<.....]..e....w.D...G..s}.=..[-S.~......-.:.c.'.K..W.OJ....L..sF..a../)8.
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .$..h..xQ8d..+.C.../......X........~8.1....@M..xQ/@...'.......GG.....i`J.CX....O.2@...!=".J....1
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: G#..j..f-..}k..S.
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:00 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:01 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:01 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:01 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346481] [GNSS] 定位中... 已运行 836346481s
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:02 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:02 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346482] [GNSS] 定位中... 已运行 836346482s
[836346482] [UPLOAD] 传感器数据: {"acc_x": 0.057, "acc_y": -0.057, "acc_z": 9.425, "acc_total_g": 0.96, "temp": 25.9, "humidity": 52.8, "light_v": 1.352, "lat": 0.0, "lon": 0.0, "speed": 0.0, "timestamp": 836346482}
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,32.
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .............&f.......i`I.b.L...
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....................9..m.=<`4.j
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....)........s......[R....r8H...-...V=...dn...
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,211.
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............ "G.W#..x4MI...Gpz#{l.t....|..i2w....2.._4C.....-0...........m...>.3..U.loLJZ...C...
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ...~[.A:...}.~..6.RA...*.x..3..O.......,$.......nyq.@.p&.F....gA... .ey.8....{/ O......G..o.X.. 
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: j/.%i>..@...@......
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:02 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:03 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:03 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:03 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346483] [GNSS] 定位中... 已运行 836346483s
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:04 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:04 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346484] [GNSS] 定位中... 已运行 836346484s
[836346484] [UPLOAD] 传感器数据: {"acc_x": 0.057, "acc_y": -0.153, "acc_z": 9.464, "acc_total_g": 0.97, "temp": 25.9, "humidity": 52.8, "light_v": 1.26, "lat": 0.0, "lon": 0.0, "speed": 0.0, "timestamp": 836346484}
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,32.
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............!E..=:.}.Y@.V.8r....
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............"...p:...{...9.Ja..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....).......#7....Vr.....8.f.p...'.S..........
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,210.
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............$C.{.........~..wB...!....=......x....lJ.%q.q...#.i.9H....DH.<.........-...W8.7....r
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: z.....f........A...u4......{O.&.vJ..Y....a......@h?..P....x.u..#.'}b.?$gd|..(.....C....;..rn..)i
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: $.....JXu}/.r.....
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
[836346484] [HEARTBEAT] 心跳包: {"type": "heartbeat", "lat": 0.0, "lon": 0.0, "speed": 0.0, "gps_valid": false, "timestamp": 836346484}
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............%.VXj..."...b...D..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............&...r)....N.SKF?.@5
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....).......'.4.6..."......L.W!.&...n..F......
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,132.
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:04 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............(@?.......(O9C.c..S.?Z..[.....n.......$.gT...J*.c5...bK..:..V....Q....x..%T.1=..<...
2026-07-02 22:28:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ...s...3.._.......C.|...J....k.^\...
2026-07-02 22:28:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:05 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:05 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346485] [GNSS] 定位中... 已运行 836346485s
2026-07-02 22:28:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:05 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:05 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:06 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346486] [GNSS] 定位中... 已运行 836346486s
[836346486] [UPLOAD] 传感器数据: {"acc_x": 0.0, "acc_y": -0.077, "acc_z": 9.502, "acc_total_g": 0.97, "temp": 25.9, "humidity": 52.8, "light_v": 1.266, "lat": 0.0, "lon": 0.0, "speed": 0.0, "timestamp": 836346486}
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,32.
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............)Yz,....E.#x.7U...#.
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............*[Pd......a.4..*XP^
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....).......+j.E.&....x.8f^..F..{.^G./......'.
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,209.
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............,.%s....c15y..BaB.U1.vA?3..v.i..5C..,oE.[.5R.M..3...r?w..H..b.N......&}u..yh.!..o.*.
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....)._.v...........3.ZCd.u,.. ...C<............Y.[r.s9>%a.......Mk...Y....H.[..M......<.9...@T.
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: . .;Fq`..$.....;.
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:06 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:06 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:06 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346487] [GNSS] 定位中... 已运行 836346487s
2026-07-02 22:28:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:07 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:07 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:07 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346488] [GNSS] 定位中... 已运行 836346488s
[836346488] [UPLOAD] 传感器数据: {"acc_x": 0.019, "acc_y": -0.115, "acc_z": 9.464, "acc_total_g": 0.97, "temp": 25.9, "humidity": 52.8, "light_v": 1.384, "lat": 0.0, "lon": 0.0, "speed": 0.0, "timestamp": 836346488}
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,32.
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............-Q%t.....<......D%..
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .............'...+i.kf.[.....4.
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....)......./*.....1.=.l.J...[...Jw....V..!.;n
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,211.
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............0.i....J.c.H#.gd~...Ho.ku.....9J.p..H(.....mAaL.....'..&..7.A{.p......<.4..m..u.....
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: u5..Yp...G.a..K.......u).p..$..6.1..k.7...SN..M(.uau..u..6.<..'...e..*q..W..Q.......Z...d..J..r.
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....i.."..7v.......
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:08 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:08 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:08 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346489] [GNSS] 定位中... 已运行 836346489s
2026-07-02 22:28:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:09 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:09 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346490] [GNSS] 定位中... 已运行 836346490s
[836346490] [UPLOAD] 传感器数据: {"acc_x": 0.057, "acc_y": -0.115, "acc_z": 9.521, "acc_total_g": 0.97, "temp": 25.9, "humidity": 52.8, "light_v": 1.28, "lat": 0.0, "lon": 0.0, "speed": 0.0, "timestamp": 836346490}
2026-07-02 22:28:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,32.
2026-07-02 22:28:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............1..mus..O$.......y.3
2026-07-02 22:28:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:09 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............2K........`.f..V...
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....).......3.....}+...G.W..}.....0./S.di....`
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,210.
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............4.5..c1O.rg...p...{25.u.ys..Y.t.....8.$n....f.t......V6...U.."s2...^.Y..0.4..!.....u
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....A.%j...H...h........P.neF.& ...~....._/./4.. .?..6..1..0p..*.q..L.q.(...N...Pf....&...9V....
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: \"jqCB.@..\Sz..L..
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:10 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:10 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:10 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346491] [GNSS] 定位中... 已运行 836346491s
2026-07-02 22:28:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:11 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:11 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346492] [GNSS] 定位中... 已运行 836346492s
[836346492] [UPLOAD] 传感器数据: {"acc_x": -0.019, "acc_y": -0.134, "acc_z": 9.502, "acc_total_g": 0.97, "temp": 25.9, "humidity": 52.8, "light_v": 1.322, "lat": 0.0, "lon": 0.0, "speed": 0.0, "timestamp": 836346492}
2026-07-02 22:28:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,32.
2026-07-02 22:28:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............5..i.8?..........='r
2026-07-02 22:28:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:11 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............6`..w^.y....X......
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....).......7.!..h6..}.9...S..u,F......=F.RI..
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,212.
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............8.z...;...g'....*...M..qO....t..~."[CJ.9...|..i......5.w...}..R.`....t........z.r...
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: M...z..*t9M/mZ..a.....(.gm..b.rW......G....n._C.Q..Z....;.'q.bb..j..)ap...1.,}e....|.<..J.1c..O.
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ...!O.s...=... y.x..
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:12 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:12 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:12 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346493] [GNSS] 定位中... 已运行 836346493s
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:13 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:13 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346494] [GNSS] 定位中... 已运行 836346494s
[836346494] [UPLOAD] 传感器数据: {"acc_x": 0.096, "acc_y": -0.077, "acc_z": 9.406, "acc_total_g": 0.96, "temp": 25.9, "humidity": 52.8, "light_v": 1.28, "lat": 0.0, "lon": 0.0, "speed": 0.0, "timestamp": 836346494}
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,32.
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............9l...g.....-..`.FA|!
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............:..Wa.-S1x.f.N;....
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....).......;9.......T....~...,1...ip.$.z.....
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:13 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,210.
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............<..I...wI.Q..s.?.hWX.}.F.wY..?.TJ.....3'j0..d.Q`$..,&J.'.9.G.7.m...U.)N.Y.5..EE.1.f]
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: 6..~.)....C...A.EjB.r{...... |&...?..NH..8............0y..{H.......;.X:..C...$.kDB..OF.+....mT..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: .[.y..g...P;.PfF5E
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
[836346494] [HEARTBEAT] 心跳包: {"type": "heartbeat", "lat": 0.0, "lon": 0.0, "speed": 0.0, "gps_valid": false, "timestamp": 836346494}
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............=.H>....O.X}j2..}W.
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............>;.=....8.*.>>.....
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....).......?JN.R...9B...Pp.....,...eF^......(
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,132.
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............@..!^.U...(.XH..&.....*.w..Mjo..}......_I...6...N....?.,<...?."L..p....vC....(..?...
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: Q..5../0..;...=<......)............k
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:14 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +CME ERROR: 516..
2026-07-02 22:28:14 [WARN ]  [at_client.c]	[at_obj_exec_cmd():414][4696]	execute command (AT+QGPSLOC=2) failed!
2026-07-02 22:28:14 [WARN ]  [mp_gnss.c ]	[quectel_gnss_get_location():82][4696]	GNSS get location failed, error code: 516
[836346495] [GNSS] 定位中... 已运行 836346495s
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +QGPSLOC: 142815.000,31.26288,121.64655,2.5,66.2,3,000.00,0.0,0.0,020726,07..
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: OK..
[836346496] [GNSS] 定位有效: 纬度:31.26288  经度:121.64655  速度:0.0km/h
[836346496] [UPLOAD] 传感器数据: {"acc_x": 0.057, "acc_y": -0.134, "acc_z": 9.502, "acc_total_g": 0.97, "temp": 26.0, "humidity": 52.8, "light_v": 1.254, "lat": 31.26288, "lon": 121.64655, "speed": 0.0, "timestamp": 836346496}
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,32.
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............A...'....B..}...~N.n
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,31.
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............B.+.[..g....8.?FI..
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,46.
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ....).......C.:.(......o..O.N[.KqTS..a...)0...
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QISEND=0,222.
2026-07-02 22:28:15 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:16 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: >
2026-07-02 22:28:16 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ............D..b...]......L.......(.......vB.x.he9..^.Q8....8h..U>..+.Z8.~.{.Kd.r......>.'4.EY..
2026-07-02 22:28:16 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: ..b...s.........&[.....jE.#.y7]..c...M.3....\.\'S..y.kR..<n|.J=....k/.H...(..x{m5!0..2'^..*N....
2026-07-02 22:28:16 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: `...,o(.S...'e...py{..I.bP...x
2026-07-02 22:28:16 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline:  ..
2026-07-02 22:28:16 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: SEND OK..
2026-07-02 22:28:16 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][4696]		sendline: AT+QGPSLOC=2.
2026-07-02 22:28:16 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:16 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: +QGPSLOC: 142816.000,31.26286,121.64644,2.5,51.7,3,000.00,0.7,0.4,020726,07..
2026-07-02 22:28:16 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: ..
2026-07-02 22:28:16 [DEBUG]  [at_utils.c]	[at_print_raw_cmd():51][2880]		recvline: OK..
[836346497] [GNSS] 定位有效: 纬度:31.26286  经度:121.64644  速度:0.0km/h