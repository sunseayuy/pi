#!/home/pi/Desktop python
#encoding:utf-8
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

gpio_echo=7
gpio.setup(gpio_echo,gpio.IN)
def bizhang(): #避障函数
    if gpio.input(gpio_echo)==0:
        return True
    else:
        return False
#while True:
#    if bizhang():
#        print("1")
#    time.sleep(1)
