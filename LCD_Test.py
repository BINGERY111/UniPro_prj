# -*- coding: utf-8 -*-
"""
============================================================================
 智能骑行头盔系统 - 现代极简卡片式UI大盘 (v4.2 终极重构版)
 修复：引入居中对齐算法消除错位乱码，采用色块分区榨干屏幕每一像素，拒绝空洞风
 适配：ST7735 LCD (160x80) 原生 show_string 接口
============================================================================
"""

import machine
import time
from st7735 import LCD

# ====================================================================
# 硬件与全局引脚配置
# ====================================================================
SPI_BUS = 1
SPI_BAUDRATE = 20000000
LCD_DC_PIN = 'F12'
LCD_CS_PIN = 'D14'

def log(tag, message):
    print('[{}] [{}] {}'.format(int(time.time()), tag, message))


# ====================================================================
# 核心UI渲染引擎（高密度卡片式排版）
# ====================================================================
class LcdHandler:
    """
    LCD 极致重构渲染引擎
    内置动态字符居中算法，采用高级多调色块进行卡片化分区，呈现高度饱满的现代科技质感
    """

    def __init__(self):
        self.lcd = None
        # 预设高端色彩（16位RGB565高雅色系）
        self.DARK_NAVY = 0x012B  # 玄青蓝
        self.CARD_BG   = 0x18E3  # 灰墨蓝卡片背景
        self.CARD_ACC  = 0x2A65  # 钛金蓝卡片背景
        self.TEXT_GRAY = 0xA714  # 极客低调灰
        
        try:
            spi = machine.SPI(SPI_BUS, baudrate=SPI_BAUDRATE, polarity=0, phase=0)
            self.lcd = LCD(spi, dc_pin=LCD_DC_PIN, cs_pin=LCD_CS_PIN)
            self.lcd.set_rotation(1)  # 横屏模式
            
            # 使用高奢玄青作为底层铺色，替代死板的纯黑
            self.lcd.fill_screen(self.DARK_NAVY)
            self.lcd.flush()
            log('LCD_CORE', '高级卡片化多级UI渲染模块重构成功.')
        except Exception as e:
            log('LCD_CORE', 'LCD 初始化失败: {}'.format(e))

    def center_x(self, text, font_width=8):
        """核心算法：根据字符长度，自动计算横向绝对居中坐标，消除左靠工业风及假乱码"""
        screen_width = 160
        text_width = len(text) * font_width
        return max(0, (screen_width - text_width) // 2)

    def draw_window(self, title, theme_color=0x197F):
        """渲染带半通透边框的全面屏顶部高级标题栏"""
        if not self.lcd: return
        self.lcd.fill_rectangle(0, 0, 160, 14, theme_color)
        cx = self.center_x(title)
        self.lcd.show_string(cx, 1, title, self.lcd.WHITE, theme_color)
        # 右侧科技状态标识点
        self.lcd.fill_rectangle(146, 4, 8, 6, self.lcd.GREEN)

    def show_boot(self, version):
        """[第0级：开机层] 居中对齐、上下紧凑包围式极简科技片头"""
        if not self.lcd: return
        try:
            # 纯黑底突出质感
            self.lcd.fill_screen(self.lcd.BLACK)
            
            # 计算每行文本的精确居中位置
            t1 = "SMART HELMET"
            t2 = "SYSTEM OS"
            t3 = version
            
            self.lcd.show_string(self.center_x(t1), 18, t1, self.lcd.CYAN, self.lcd.BLACK)
            self.lcd.show_string(self.center_x(t2), 38, t2, self.lcd.WHITE, self.lcd.BLACK)
            self.lcd.show_string(self.center_x(t3), 58, t3, self.TEXT_GRAY, self.lcd.BLACK)
            
            self.lcd.flush()
        except Exception as e:
            log('UI_ERR', '渲染开机画面异常: {}'.format(e))

    def show_normal(self, temp, humidity, gps_valid, speed):
        """[第1级：主仪表盘] 告别空白！双卡片矩阵微格大盘，视觉信息饱满丰盈"""
        if not self.lcd: return
        try:
            # 用深底打底
            self.lcd.fill_screen(self.DARK_NAVY)
            self.draw_window("HELMET MONITOR")

            # ===== 左卡片：环境仓（高:58px，宽:74px），自带独立背景块，拒绝空洞空白 =====
            self.lcd.fill_rectangle(4, 18, 74, 58, self.CARD_BG)
            self.lcd.show_string(8, 22, "ENV.DATA", 0x7BEF, self.CARD_BG)
            self.lcd.show_rectangle(4, 18, 74, 58, 0x3186) # 精致细微边框
            self.lcd.show_string(8, 38, "T:{:.1f}C".format(temp), self.lcd.WHITE, self.CARD_BG)
            self.lcd.show_string(8, 54, "H:{:.1f}%".format(humidity), self.lcd.WHITE, self.CARD_BG)

            # ===== 右卡片：运动仓（高:58px，宽:74px），卡片底色对比升华 =====
            self.lcd.fill_rectangle(82, 18, 74, 58, self.CARD_ACC)
            self.lcd.show_string(86, 22, "GNSS.MOV", 0x7BEF, self.CARD_ACC)
            self.lcd.show_rectangle(82, 18, 74, 58, 0x4A49)
            
            if gps_valid:
                self.lcd.show_string(86, 38, "FIXED", self.lcd.GREEN, self.CARD_ACC)
                self.lcd.show_string(86, 54, "{:.1f} m/s".format(speed), self.lcd.WHITE, self.CARD_ACC)
            else:
                self.lcd.show_string(86, 38, "SEARCHING", self.lcd.RED, self.CARD_ACC)
                self.lcd.show_string(86, 54, "SPD: --", self.TEXT_GRAY, self.CARD_ACC)

            self.lcd.flush()
        except Exception as e:
            log('UI_ERR', '渲染主仪表盘异常: {}'.format(e))

    def show_gps_info(self, lat, lon, satellites):
        """[第2级：详情层] 大文本环绕式卡片，全面榨干屏幕留白空间"""
        if not self.lcd: return
        try:
            self.lcd.fill_screen(self.DARK_NAVY)
            self.draw_window("GNSS NMEA DETAIL", bg_color=0x020F) 

            # 大面积中央详情卡片槽填充
            self.lcd.fill_rectangle(4, 18, 152, 58, self.CARD_BG)
            self.lcd.show_rectangle(4, 18, 152, 58, 0x3186)

            # 数据在卡片内精细对齐排列
            self.lcd.show_string(10, 24, "LAT: {:.5f}".format(lat), self.lcd.CYAN, self.CARD_BG)
            self.lcd.show_string(10, 41, "LON: {:.5f}".format(lon), self.lcd.CYAN, self.CARD_BG)
            self.lcd.show_string(10, 58, "SATS TRACKED: {:02d}".format(satellites), self.lcd.WHITE, self.CARD_BG)
            
            self.lcd.flush()
        except Exception as e:
            log('UI_ERR', '渲染GPS详情页异常: {}'.format(e))

    def show_countdown(self, seconds):
        """[异常事件级] 全屏无留白反色预警，高亮卡片包围突出倒计时数据"""
        if not self.lcd: return
        try:
            if seconds > 0:
                self.lcd.fill_screen(self.lcd.BLACK)
                # 奢华血红危急置顶通栏
                self.lcd.fill_rectangle(0, 0, 160, 16, self.lcd.RED)
                header_text = "CRITICAL WARNING"
                self.lcd.show_string(self.center_x(header_text), 1, header_text, self.lcd.WHITE, self.lcd.RED)

                # 报警文字自动横向居中，消除乱码假象
                str1 = "CRASH DETECTED"
                str2 = "SOS IN: {:02d} SEC".format(seconds)
                self.lcd.show_string(self.center_x(str1), 26, str1, self.lcd.RED, self.lcd.BLACK)
                self.lcd.show_string(self.center_x(str2), 46, str2, self.lcd.WHITE, self.lcd.BLACK)
                
                # 底部按钮底框交互区
                self.lcd.fill_rectangle(6, 66, 148, 13, 0x3186)
                btn_text = "PRESS KEY TO CANCEL"
                self.lcd.show_string(self.center_x(btn_text), 67, btn_text, self.lcd.WHITE, 0x3186)
            else:
                # 危机落地，无视留白，大字全屏极速跳变反闪
                flash_toggle = (int(time.ticks_ms()) // 300) % 2
                bg = self.lcd.RED if flash_toggle else self.lcd.BLACK
                fg = self.lcd.WHITE if flash_toggle else self.lcd.RED
                
                self.lcd.fill_screen(bg)
                s1 = "EMERGENCY"
                s2 = "SOS SENT"
                self.lcd.show_string(self.center_x(s1), 24, s1, fg, bg)
                self.lcd.show_string(self.center_x(s2), 44, s2, fg, bg)
                
            self.lcd.flush()
        except Exception as e:
            log('UI_ERR', '渲染倒计时突发异常: {}'.format(e))

    def show_sos_cancelled(self):
        """[交互过渡态] 全覆盖祖母绿安全回归确认框"""
        if not self.lcd: return
        try:
            # 优雅饱满的英国绿 (0x03E0) 带来极强安全视效
            self.lcd.fill_screen(0x03E0)
            text1 = "SYSTEM SAFE"
            text2 = "ALARM CANCELLED"
            self.lcd.show_string(self.center_x(text1), 25, text1, self.lcd.WHITE, 0x03E0)
            self.lcd.show_string(self.center_x(text2), 45, text2, self.lcd.WHITE, 0x03E0)
            self.lcd.flush()
            time.sleep(1.5)  # 留存展示，随后回弹监测大盘
        except Exception as e:
            log('UI_ERR', '渲染危机解除确认窗异常: {}'.format(e))


# ====================================================================
# 自动化模拟演练测试流水线
# ====================================================================
def run_ui_pipeline():
    print("====================================================")
    print(" 智能头盔 OS v4.2 现代卡片化 UI 测试集成大盘启动 ")
    print("====================================================")
    
    ui = LcdHandler()
    if not ui.lcd:
        print("[FATAL ERROR] 硬件屏初始化中断，退出。")
        return

    # [1] 开机层
    print("\n[STAGE 1] 渲染 -> 第0级：安全居中开机画面")
    ui.show_boot("HELMET OS v4.2")
    time.sleep(2.5)

    # [2] 主大盘（双卡片矩阵，无空白残留）
    print("\n[STAGE 2] 渲染 -> 第1级：高饱和双独立卡片监测大盘")
    ui.show_normal(temp=25.2, humidity=55.0, gps_valid=True, speed=6.2)
    time.sleep(3.5)

    # [3] NMEA 地理全要素详情
    print("\n[STAGE 3] 渲染 -> 第2级：高密度环绕卡片详情页")
    ui.show_gps_info(lat=31.26291, lon=121.46302, satellites=12)
    time.sleep(3.5)

    # [4] 异常坠落二级倒计时确认
    print("\n[STAGE 4] 突发状况 -> 切入异常高危倒计时全面屏")
    for remaining in range(5, 0, -1):
        ui.show_countdown(remaining)
        time.sleep(1.0)

    # [5] 警报触发闪烁
    print("\n[STAGE 5] 极限冲击 -> 倒计时归零，SOS 突发上报，全屏无边界高频反色闪烁")
    for _ in range(8):
        ui.show_countdown(0)
        time.sleep(0.25)

    # [6] 按键安全取消复位
    print("\n[STAGE 6] 交互中断 -> 解除报警，步入祖母绿安全过渡窗")
    ui.show_sos_cancelled()

    # [7] 状态回弹
    print("\n[STAGE 7] 状态回弹 -> 丝滑重置回第1级监测卡片大盘")
    ui.show_normal(temp=24.6, humidity=57.1, gps_valid=False, speed=0.0)
    
    print("\n====================================================")
    print(" OS v4.2 终极卡片排版演练全部圆满结束！ ")
    print("====================================================")

if __name__ == '__main__':
    run_ui_pipeline()