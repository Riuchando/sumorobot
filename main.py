#import RPi.GPIO as GPIO, time
#from  qtitest import RCtime
#import RPI.GPIO as GPIO, time
import time
from movement import *
#from qtiLineSensor import *
from qtilClass import *
from sonar import takeMeasurement
#import qtites
def init():
    time.sleep(115)
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

    
    stop(speed=50)
    forward(speed=5)
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
    back(speed=100,accel=15)
    tm=takeMeasurement()
    print tm
    #there gets some errors when it gets too close
    while tm > 5:
        print tm
        tm=takeMeasurement()
    #forward(speed=255, )
    stop()    

def detectBoxTest():
    turnLeft(speed=250,accel=15)
    sonarDist=takeMeasurement()
    pins=[11,13,16,18]
    print sonarDist
    while sonarDist> 40:
	sonarDist=takeMeasurement()
	print sonarDist
    stop()
    forward(speed=100)    
    qtiPins=qtiWrapper(wiring=False)
    while qtiPins.detectList(pins[:2],wiring=False)==False:
	pass
    stop()
def linetest():
    
    pins=[11,13,16,18]
    forward(speed=50,accel=10) 
    t=qtiWrapper(wiring=False)    
    detect=t.detect(11,wiring=False)
    while t.detectList(pinList=pins,wiring=False)==False:
	#detect=t.detectList(pins,wiring=False)
	pass
    #back(speed=25)
    #busy wait until the sensors detect something
    # while (RCtime :wq

    #print "Passed white line"
    
    stop()
    time.sleep(0.5)

def turnSampleRate():
    sample=[]
    turnLeft(speed=70,accel=5)
    sonarDist=takeMeasurement()
    detected=False
    while detected==False:
        while sonarDist>30:
            sonarDist=takeMeasurement()
	    #I could bump it up to 32 and make it bit shifted but w/e
	    if len(sample)> 30:
	        mean=sum(sample)/30
	    else:
	        sample.append(sonarDist)
        #reorganise code into a class so that I can slow down rather than needing to stop
        stop()
        turnLeft(speed=50)
        newDist=takeMeasurement()
        if newDist < sonarDist:
	   forward(speed=100)
	   detected=True
    t=qtiWrapper(wiring=False)
    while newDist < sonarDist:
	forward(speed=70,driftRatio=1.5) 
        if t.detectList(pinList=pins,wiring=False)==False:
        #detect=t.detectList(pins,wiring=False)
            stop()
	    return
	newDist=sonarDist
	sonarDist=takeMeasurement
    
    stop()
    #else:
    #loop back to the above while loop, need to edit this as soon as I get home
    #stop()
try:
    #wiring=True
    #note that this is depricated
    #initQTI(wiring)
    #linetest()
    #turnSampleRate()
    #movementTest()
    detectBoxTest()
    #handTest()
    #print 'test'
	
finally:
    stop()
