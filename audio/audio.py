from quectel import Audio
import time

# 确保 SD 卡已经挂载
# ...

audio = Audio()
audio.init()
audio.set_speaker_volume(5)

print("开始播放 /sd/你的音乐文件.wav")
audio.play_local("/sd/test1.wav")

time.sleep(10) # 根据你的音乐长度调整
audio.play_stop()
print("播放结束")