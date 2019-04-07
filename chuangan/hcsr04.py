#!/home/pi/Desktop python
#encoding:utf-8
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

gpio_trig=18
gpio_echo=16
gpio.setup(gpio_trig,gpio.OUT)
gpio.output(gpio_trig,gpio.LOW)
gpio.setup(gpio_echo,gpio.IN)
def hcsr04(): # 测距函数
    gpio.output(gpio_trig,gpio.HIGH) # 需要10μs以上
    time.sleep(0.00015)
    gpio.output(gpio_trig,gpio.LOW)
    while gpio.input(gpio_echo)==0:
        continue
    t1=time.time()
    while gpio.input(gpio_echo)==1:
        continue
    t2=time.time()
    distance=(t2-t1)*340/2*100
    return distance
#while True:
#     print (hcsr04())
#     time.sleep(1)
