#!/home/pi/Desktop python
import sys
with open("first.txt") as f:
    line=f.readline()
    while line:
        print line
        line=f.readline
    f.close()
print 'hello world'     
