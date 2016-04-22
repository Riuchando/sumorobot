import time
from movement import *
#from qtiLineSensor import *
from qtilClass import *
from sonar import takeMeasurement

#1. Turn left until it senses something with a sonar that is roughly 3 cm away
#2. Move forward at a slow speed until you see a white line
#3. Stop the turn right really quickly then stop
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

    #EVERY TIME THAT YOU MOVE AND WANT TO STOP THE MOTORS YOU MUST MANUALLY STOP
    stop(speed=50)
    forward(speed=5)
    #check the front two pins
    #keep the motors running
    while RCTime(pin=11) and RCTime(pin=13):
        print 'wait'
    #EVERY TIME THAT YOU MOVE AND WANT TO STOP THE MOTORS YOU MUST MANUALLY STOP
    stop(speed=50)
    #back up to prove that you can move backwards
    back(speed=10)
    #EVERY TIME THAT YOU MOVE AND WANT TO STOP THE MOTORS YOU MUST MANUALLY STOP
    stop(speed=10)
    #turn around, now this function can be put into a loop
    turnRight(speed =1, angle=180,sharpness=50)
    stop(speed=20)

#1. Move forward until you see a object that is roughly 5 cm away
def handTest():
    back(speed=255,accel=15)
    #this is the sonar sensor that will tell you how far it is away in cm
    tm=takeMeasurement()
    #print tm
    #there gets some errors when it gets too close
    while tm > 5:
        print tm
        tm=takeMeasurement()

    stop()

# 1. wait until the sonar gets a measurement
# 2. move forward move forward
def detectBoxTest():
    turnLeft(speed=250,accel=15)
    sonarDist=takeMeasurement()
    pins=[11,13,16,18]
    #print sonarDist
    while sonarDist> 40:
    	sonarDist=takeMeasurement()
  	#print sonarDist
    stop()
    forward(speed=255 )
    qtiPins=qtiWrapper(wiring=False)
    #note this is a horrible
    while True:
    	while qtiPins.detectList(pins[:2],wiring=False)==False:
        	forward(speed=250)
      #this redirects the robot
    	stop()
    	back(speed=250)
    	turnLeft(speed=250)
    	stop()
    	forward(speed=250)

# 1. Print out to screen to see all the line sensors
def linetest():

    pins=[11,13,16,18]
    forward(speed=255,accel=10)
    t=qtiWrapper(wiring=False)
    detect=t.detect(11,wiring=False)
    while t.detectList(pinList=pins,wiring=False)==False:
	    #detect=t.detectList(pins,wiring=False)
    	pass
    #back(speed=25)
    #busy wait until the sensors detect something
    #if the robot isn't connected to a screen test by seeing with motors
    stop()
    time.sleep(0.5)

try:
    #wiring=True
    #linetest()
    #movementTest()
    detectBoxTest()
    #handTest()

finally:
    stop()
