#encoding:utf-8
import serial  
import time  
  
ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=1)  
#ser = serial.Serial('COM3', 9600, timeout=1)  
print (ser.isOpen())  
words1="#1P1100T1000\n\r"
words2="#1P1800T1000\n\r"
words3="#1P1100T1000\n\r"
words4="#1P1800T1000\n\r"

print(type(words1))
while (1):
        print(works1)
        ser.write(words1.encode('utf-8'))
        time.sleep(1.1)
        ser.write(words2.encode('utf-8'))
        time.sleep(1.1)
        ser.write(words3.encode('utf-8'))
        time.sleep(1.1)
        ser.write(words4.encode('utf-8'))
        time.sleep(1.1)
        print('jieshu')  
ser.close() 
