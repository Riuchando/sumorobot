#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time

class motors():
  def __init__(self):
    self.mh = Adafruit_MotorHAT(addr=0x70) #note stopping this program DOES NOT stop the motor
    #we COULD make this an array but for programming simplicity, have 4 variables
    self.upperLeft=self.mh.getMotor(1)
    self.upperRight=self.mh.getMotor(2)
    self.lowerLeft=self.mh.getMotor(3)
    self.lowerRight=self.mh.getMotor(4)
    self.motorSpeed=[0,0,0,0]
  #might have it work similarly to forward
  def back(self,speed =100,accel=20):
    #there is a built in library 0 255
    #essentially follow the model
    #note might need to do some fancy math to error correct for the difference in the motors
    if speed > 255 or speed < 0:
      return # do nothing for now, write error message at some point
    #initialize the direction of the motors
    self.upperLeft.run(Adafruit_MotorHAT.FORWARD)
    self.upperRight.run(Adafruit_MotorHAT.FORWARD)
    self.lowerLeft.run(Adafruit_MotorHAT.FORWARD)
    self.lowerRight.run(Adafruit_MotorHAT.FORWARD)
    #slowly accellerate the motors so they aren't jerky,
    #think of someone constantly stopping and starting car
    for i in range(speed)[::accel]:
      self.upperLeft.setSpeed(i)
      self.upperRight.setSpeed(i)
      self.lowerLeft.setSpeed(i)
      self.lowerRight.setSpeed(i)



  #these are assumed to be at a full stop
  def turnRight(self,speed =5, angle=30, accel=20):
    #depending on the output for compass sensor,
    #figure out Radians or Degrees
    #also write some simple algos to have the ultra sonic sensor help where the thing is
    if speed > 255 or speed < 0:
      return # do nothing for now, write error message at some point
    self.upperLeft.run(Adafruit_MotorHAT.BACKWARD)
    self.upperRight.run(Adafruit_MotorHAT.FORWARD)
    self.lowerLeft.run(Adafruit_MotorHAT.BACKWARD)
    self.lowerRight.run(Adafruit_MotorHAT.FORWARD)
    #make sure the library is imported from the compass
    #while abs(compass.reading()- 10) <= angle:
    # keep moving...
    #stop()
    for i in range(speed)[::accel]:
      self.upperLeft.setSpeed(i)
      self.upperRight.setSpeed(i)
      self.lowerLeft.setSpeed(i)
      self.lowerRight.setSpeed(i)
      #if getRC(3) or getRC(4):
      #  stop(0)
      #  forward(speed)
      #time.sleep(0.05) # this makes the acceleration sself.lower/faster, debug to find a good amount of time
    #pass

  def turnLeft(self,speed =5, angle=30,sharpness = 0,untilStop=False,accel=10):
    #same as turn left, figure out Radians or Degrees
    if speed > 255 or speed < 0:
      return # do nothing for now, write error message at some point
    self.upperLeft.run(Adafruit_MotorHAT.FORWARD)
    self.upperRight.run(Adafruit_MotorHAT.BACKWARD)
    self.lowerLeft.run(Adafruit_MotorHAT.FORWARD)
    self.lowerRight.run(Adafruit_MotorHAT.BACKWARD)
    if accel != -1:
      for i in range(speed)[::accel]:
        self.upperLeft.setSpeed(i)
        self.upperRight.setSpeed(i)
        self.lowerLeft.setSpeed(i)
        self.lowerRight.setSpeed(i)
    else:
      self.upperLeft.setSpeed(speed)
      self.upperRight.setSpeed(speed)
      self.lowerLeft.setSpeed(speed)
      self.lowerRight.setSpeed(speed)
    #time.sleep(0.05) # this makes the acceleration sself.lower/faster, debug to find a good amount of time


  def forward(self,speed =255,accel=10,driftRatio=1):
    #the same with the forward
    #need to set up the detection on seeing if the motors can be run in parellel
    if speed > 255 or speed < 0:
        return # do nothing for now, write error message at some point
      self.upperLeft.run(Adafruit_MotorHAT.BACKWARD)
      self.upperRight.run(Adafruit_MotorHAT.BACKWARD)
      self.lowerLeft.run(Adafruit_MotorHAT.BACKWARD)
      self.lowerRight.run(Adafruit_MotorHAT.BACKWARD)
    if driftRatio ==1:
      for i in range(motorSpeed[0],speed*driftRatio)[::accel]:
        self.upperRight.setSpeed(i)
        self.lowerRight.setSpeed(i)
      for i in range(motorSpeed[1],speed)[::accel]:
        self.upperLeft.setSpeed(i)
        self.lowerLeft.setSpeed(i)
      #for now, just for left/right control
      self.motorSpeed=[speed,speed]
    else:
      #make sure values are valid
      if speed*driftRatio > 255:
         return
      #hacky solution

      for i in range(motorSpeed[0],speed*driftRatio)[::accel]:
        self.upperRight.setSpeed(i)
        self.lowerRight.setSpeed(i)
      for i in range(motorSpeed[1],speed)[::accel]:
        self.upperLeft.setSpeed(i)
        self.lowerLeft.setSpeed(i)
      self.motorSpeed=[speed*driftRatio,speed]



  def stop(self,speed=0):
    #decellerates, then stops
    for i in range(speed)[::-1]:
      self.upperLeft.setSpeed(i)
      self.upperRight.setSpeed(i)
      self.lowerLeft.setSpeed(i)
      self.lowerRight.setSpeed(i)
    self.upperLeft.run(Adafruit_MotorHAT.RELEASE)
    self.upperRight.run(Adafruit_MotorHAT.RELEASE)
    self.lowerLeft.run(Adafruit_MotorHAT.RELEASE)
    self.lowerRight.run(Adafruit_MotorHAT.RELEASE)
    # optional sleep to make reduce jerkiness
    #time.sleep(1.0)

  def redirect(self,direction):
    # quick 90 degree turn (will need some code to figure out which one) need to enable sensors for detection
    # back max speed (unless a collision
    # another quick 90 degree Turn  to rorganise then zoom past to get behind it
    self.turnRight(speed=50, angle=90)
    self.back(speed=90)
    self.turnRight(speed=50, angle=90)
    self.forward(speed=50)
  def movementTest():
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
      #time.sleep(1)
      #stop()
    finally:
      stop()
  #movementTest()
