#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

mh = Adafruit_MotorHat(addr=0x60) #note stopping this program DOES NOT stop the motor
#we COULD make this an array but for programming simplicity, have 4 variables
upperLeft=mh.getMotor(1)
upperRight=mh.getMotor(2)
lowerLeft=mh.getMotor(3)
lowerRight=mh.getMotor(4)
def forward(speed =50):
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
  for i in range(speed):
    upperLeft.setSpeed(i)
    upperRight.setSpeed(i)
    lowerLeft.setSpeed(i)
    lowerRight.setSpeed(i)
    time.sleep(0.05) # this makes the acceleration slower/faster, debug to find a good amount of time
  #note that we don't have a manual stop in here    

  
  

def turnLeft(speed =5, angle=30, sharpness = 0):
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
  stop()
  pass

def turnRight(speed =5, angle=30):
  #same as turn left, figure out Radians or Degrees
  if speed > 255 or speed < 0:
    return # do nothing for now, write error message at some point
  upperLeft.run(Adafruit_MotorHAT.FORWARD)
  upperRight.run(Adafruit_MotorHAT.BACKWARD)
  lowerLeft.run(Adafruit_MotorHAT.FORWARD)
  lowerRight.run(Adafruit_MotorHAT.BACKWARD)
  stop()
  pass


def back(speed =5):
  #the same with the forward
  #need to set up the detection on seeing if the motors can be run in parellel
  if speed > 255 or speed < 0:
    return # do nothing for now, write error message at some point
  upperLeft.run(Adafruit_MotorHAT.BACKWARD)
  upperRight.run(Adafruit_MotorHAT.)
  lowerLeft.run(Adafruit_MotorHAT.FORWARD)
  lowerRight.run(Adafruit_MotorHAT.FORWARD)
  pass

def stop():
  #does the obvious
  upperLeft.run(Adafruit_MotorHAT.RELEASE)
  upperRight.run(Adafruit_MotorHAT.RELEASE)
  lowerLeft.run(Adafruit_MotorHAT.RELEASE)
  lowerRight.run(Adafruit_MotorHAT.RELEASE)
  # optional sleep to make reduce jerkiness
  time.sleep(1.0)
