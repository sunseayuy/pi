#!/home/pi/Desktop python
#encoding:utf-8
import serial  
import time 
ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=1)  
print (ser.isOpen()) 

def readDef(name):
	for line in open("first.txt"):
		print(line, end = '') # 在 Python 2中，后面跟 ',' 将忽略换行符
		ser.write(line.encode('utf-8'))
		print("******")
		time.sleep(1.1) #print(line, end = '') # 在 Python 3中使用
	endTime = time.time()  
	return
readDef("")

