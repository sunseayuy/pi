#encoding:utf-8
import serial  
import time 

def readDef(name):
	ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=1)  
	ser.isOpen()
	f = open(name) # 返回一个文件对象 
	line = f.readline() # 调用文件的 readline()方法 
	while line:
		print (line) # 在 Python 2中，后面跟 ',' 将忽略换行符
		test_str="".join(line)
		ser.write(test_str.encode('utf-8'))
		ser.write('\n\r'.encode('utf-8'))
		print("******")
		time.sleep(0.6) #print(line, end = '') # 在 Python 3中使用
		line = f.readline()
	f.close()
	endTime = time.time()  
	ser.close()
	

