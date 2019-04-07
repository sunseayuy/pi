import os
import time
def record(recordname):
	os.system("arecord --device=hw:1,0 --duration 5 --format S16_LE --rate 11025 -c1 /home/pi/Desktop/ASR/%s" % (recordname))#录制10秒录音
def record2(time,recordname):
	os.system("arecord --device=hw:1,0 --duration %d --format S16_LE --rate 11025 -c1 /home/pi/Desktop/ASR/%s" % (time,recordname))#录制10秒录音
#record2(3,'test.wav')
