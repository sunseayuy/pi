import sys
sys.path.append('/home/pi/fail/adxl345-python')
from adxl345 import ADXL345
import IC2

adxl345 = ADXL345()
axes = adxl345.getAxes(True)
print ("ADXL345 on address 0x%x:" %adxl345.address)
print( "   x = %.3fG" % axes['x'] )
print( "   y = %.3fG" % axes['y'] )
print( "   z = %.3fG" % axes['z'] )
