import time
from movement import *
#from qtiLineSensor import *
from qtilClass import *
from sonar import takeMeasurement

def init():
    time.sleep(5)
    initQTI(2)

#test to make sure it can find an object run into it push it out until a trigger then stop
def allSensorsTest():
    #rotate for a little bit
    #NOTE that SPEED refers to top speed
    #I should add in accelleration
    turnLeft(speed=255, sharpness= 1, untilStop=True )
    #initialize the take measurements
    tm=takeMeasurement()
    #there gets some errors when it gets too close
    while (tm - 3)>0:
        print 'wait'
        tm=takeMeasurement()

    
    stop(speed=255)
    forward(speed=255)
    #check the front two pins
    while RCTime(pin=11) and RCTime(pin=13):
        print 'wait'
    stop(speed=50)
    back(speed=10)
    stop(speed=10)
    turnRight(speed =1, angle=180,sharpness=50)
    stop(speed=20)

#move forward 
def handTest():
    forward()
    tm=takeMeasurement()
    #there gets some errors when it gets too close
    while (tm - 3)>0:
        print 'wait'
        tm=takeMeasurement()
    stop(speed=255, accel=10)
    
def lineTest():
    forward()
    possiblePins=[11,13,16,18]
    #for possible in possiblePins:
    #    print 'pin ', str(possible), ' : ' , RCTime(possible)
    #print 'pin 11 : ' , RCTime(11), ' pin 13 : ', RCTime(13)
    t=qtiWrapper()
    
    
    for possible in possiblePins:
        print 'pin ', str(possible), ' : ' , t.detect(n)
    time.sleep(0.1)
    #    pass

    print 'testing with motors on'
    forward()
    #busy wait until the sensors detect something
    while t.detectList(possiblePins):
        pass
    
    stop()
    time.sleep(0.5)

try:
    wiring=True
    #note that this is depricated
    #initQTI(wiring)
    lineTest()
    movementTest()
    #print 'test'
finally:
    stop()
