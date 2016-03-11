#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
mh = Adafruit_MotorHAT(addr=0x70) #note stopping this program DOES NOT stop the motor
#we COULD make this an array but for programming simplicity, have 4 variables
upperLeft=mh.getMotor(1)
upperRight=mh.getMotor(2)
lowerLeft=mh.getMotor(3)
lowerRight=mh.getMotor(4)
def forward(speed =50, timeout=5):
  #there is a built in library 0 255
  #essentially follow the model
  #note might need to do some fancy math to error correct for the difference in the motors
  if speed > 255 or speed < 0:
    return # do nothing for now, write error message at some point
  #initialize the direction of the motors
  upperLeft.run(Adafruit_MotorHAT.FORWARD)
  upperRight.run(Adafruit_MotorHAT.FORWARD)
  lowerLeft.run(Adafruit_MotorHAT.FORWARD)
  lowerRight.run(Adafruit_MotorHAT.FORWARD)
  #slowly accellerate the motors so they aren't jerky,
  #think of someone constantly stopping and starting car
  
  for i in range(speed)[::2]:
    upperLeft.setSpeed(i)
    upperRight.setSpeed(i)
    lowerLeft.setSpeed(i)
    lowerRight.setSpeed(i)
    #print 'here'
    #if the upper right sensor detects the line
  
  #  if getRC(3):
  #   stop(0)
  #    turnLeft(speed=speed, angle=90, sharpness=90)
  #  #if the upper left sensor detects the line
  #  elif getRC(4):
  #    stop(0)
  #    turnRight(speed=speed, angle=90, sharpness=90)
  #  time.sleep(0.05) # this makes the acceleration slower/faster, debug to find a good amount of time
  #note that we don't have a manual stop in here    
  
  
  

def turnLeft(speed =5, angle=30, sharpness = 0,untilStop=False):
  #depending on the output for compass sensor,
  #figure out Radians or Degrees
  #also write some simple algos to have the ultra sonic sensor help where the thing is
  if speed > 255 or speed < 0:
    return # do nothing for now, write error message at some point
  upperLeft.run(Adafruit_MotorHAT.BACKWARD)
  upperRight.run(Adafruit_MotorHAT.FORWARD)
  lowerLeft.run(Adafruit_MotorHAT.BACKWARD)
  lowerRight.run(Adafruit_MotorHAT.FORWARD)
  #make sure the library is imported from the compass
  #while abs(compass.reading()- 10) <= angle:
  # keep moving...
  #stop()
  for i in range(speed):
    upperLeft.setSpeed(i)
    upperRight.setSpeed(i)
    lowerLeft.setSpeed(i)
    lowerRight.setSpeed(i)
    if getRC(3) or getRC(4):
      stop(0)
      forward(speed)
    time.sleep(0.05) # this makes the acceleration slower/faster, debug to find a good amount of time
  #pass

def turnRight(speed =5, angle=30,sharpness = 0,untilStop=False,accel=10):
  #same as turn left, figure out Radians or Degrees
  if speed > 255 or speed < 0:
    return # do nothing for now, write error message at some point
  upperLeft.run(Adafruit_MotorHAT.FORWARD)
  upperRight.run(Adafruit_MotorHAT.BACKWARD)
  lowerLeft.run(Adafruit_MotorHAT.FORWARD)
  lowerRight.run(Adafruit_MotorHAT.BACKWARD)
  if accel != -1:
    for i in range(speed)[::accel]:
      upperLeft.setSpeed(i)
      upperRight.setSpeed(i)
      lowerLeft.setSpeed(i)
      lowerRight.setSpeed(i)
  else:
    upperLeft.setSpeed(speed)
    upperRight.setSpeed(speed)
    lowerLeft.setSpeed(speed)
    lowerRight.setSpeed(speed)
  #time.sleep(0.05) # this makes the acceleration slower/faster, debug to find a good amount of time
  if untilStop == True:
    stop()
  
def oneWheelTime(speed=255, accel=10):
  upperLeft.run(Adafruit_MotorHAT.FORWARD)
  upperRight.run(Adafruit_MotorHAT.FORWARD)# the polarity is mixed up
  lowerLeft.run(Adafruit_MotorHAT.BACKWARD)# the polarity is mixed up
  lowerRight.run(Adafruit_MotorHAT.FORWARD)# the polarity is mixed up
  for i in range(speed)[::accel]:
      upperLeft.setSpeed(i)
  time.sleep(1)
  #stop()
  for i in range(speed)[::accel]:
    upperRight.setSpeed(i)
  time.sleep(1)
  #stop()
  for i in range(speed)[::accel]:
    lowerLeft.setSpeed(i)
  time.sleep(1)
  #stop()
  for i in range(speed)[::accel]:
    lowerRight.setSpeed(i)
  time.sleep(1)
  #stop()
      
      
def back(speed =255,accel=10):
  #the same with the forward
  #need to set up the detection on seeing if the motors can be run in parellel
  if speed > 255 or speed < 0:
    return # do nothing for now, write error message at some point
  upperLeft.run(Adafruit_MotorHAT.BACKWARD)
  upperRight.run(Adafruit_MotorHAT.BACKWARD)
  lowerLeft.run(Adafruit_MotorHAT.BACKWARD)
  lowerRight.run(Adafruit_MotorHAT.BACKWARD)
  for i in range(speed)[::accel]:
    print i
    upperLeft.setSpeed(i)
    upperRight.setSpeed(i)
    lowerLeft.setSpeed(i)
    lowerRight.setSpeed(i)
   # if 
    time.sleep(0.05) # this makes the acceleration slower/faster, debug to find a good amount of time

def stop(speed=0):
  #decellerates, then stops
  for i in range(speed)[::-1]:
    upperLeft.setSpeed(i)
    upperRight.setSpeed(i)
    lowerLeft.setSpeed(i)
    lowerRight.setSpeed(i)
  upperLeft.run(Adafruit_MotorHAT.RELEASE)
  upperRight.run(Adafruit_MotorHAT.RELEASE)
  lowerLeft.run(Adafruit_MotorHAT.RELEASE)
  lowerRight.run(Adafruit_MotorHAT.RELEASE)
  # optional sleep to make reduce jerkiness
  time.sleep(1.0)
  
def redirect(direction):
  # quick 90 degree turn (will need some code to figure out which one) need to enable sensors for detection
  # back max speed (unless a collision
  # another quick 90 degree Turn  to rorganise then zoom past to get behind it
  turnRight(speed=50, angle=90,sharpness=90)
  back(speed=90)
  turnRight(speed=50, angle=90,sharpness=90)
  turnLeft(sharpness=20,untilStop=True)
  forward(speed=50)
def mainTest():
  try:
    forward(25)
    time.sleep(1)
    stop()
    #back(255)
    #stop()
    #turnLeft(255)
    #stop()
    #slow and smooth
    #turnRight(speed=255, accel=1)
    #fast and jerky
    #turnRight(speed=255, accel=-1)
    #oneWheelTime(speed=255, accel=10)
    time.sleep(1)
    #stop()
  finally:
    stop()
#mainTest()
