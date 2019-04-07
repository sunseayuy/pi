#encoding:utf-8
import sys
sys.path.append('/home/pi/DFRobot_ADS1115/RaspberryPi/Python')
import time
from DFRobot_ADS1115 import ADS1115
ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3
ADS1115_REG_CONFIG_PGA_4_096V        = 0x02 # 4.096V range = Gain 1
ADS1115_REG_CONFIG_PGA_2_048V        = 0x04 # 2.048V range = Gain 2 (default)
ADS1115_REG_CONFIG_PGA_1_024V        = 0x06 # 1.024V range = Gain 4
ADS1115_REG_CONFIG_PGA_0_512V        = 0x08 # 0.512V range = Gain 8
ADS1115_REG_CONFIG_PGA_0_256V        = 0x0A # 0.256V range = Gain 16
ads1115 = ADS1115()

def GP2D12():
    #Set the IIC address设置IIC地址
    ads1115.setAddr_ADS1115(0x48)
    #Sets the gain and input voltage range.设置增量和电压数值范围
    ads1115.setGain(ADS1115_REG_CONFIG_PGA_6_144V)
    #Get the Digital Value of Analog of selected channel 获取所选通道的模拟数字值
    adc0 = ads1115.readVoltage(0)
    time.sleep(0.2)
    print('A0:%dmV'%adc0['r'])
    a=adc0['r']/4.9
    distance=2547.8/(a*0.49-10.41)-0.42
    return distance
#while True:
#    print(GP2D12())
#    time.sleep(1)
