import time
from movement import *
from qtiArduino import *
from i2c import *
def init():
    time.sleep(5)
    initQTI(2)

#test to make sure it can find an object run into it push it out until a trigger then stop
def simpleTest():
    #rotate
    turnLeft(speed=5, sharpness= 1, untilStop=True )
    while abs(bearing3599()-10)>0:
        print 'wait'
    stop(speed=5)
    forward(speed=50)
    #check the front two pins
    while getRC(2) and getRC(3):
        print 'wait'
    stop(speed=50)
    back(speed=10)
    stop(speed=10)
    turnRight(speed =1, angle=180,sharpness=50)
    stop(speed=20)


    
