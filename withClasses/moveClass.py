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
    self.motorSpeed=[0,0]
  #might have it work similarly to forward
  def back(self,speed =100,accel=20):
    '''
    Input:
      speed: a number from 1-255 which sends a signal to the motor hat to the DC motor to a certain speed
      accel: how fast do you want to reach the max speed
             NOTE: -1 is a special code that tells me that you want to get to maximum speed immediately, it was a hack
    Output:
      The motors move that speed
    '''
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
    '''
    Input:
      speed: a number from 1-255 which sends a signal to the motor hat to the DC motor to a certain speed
      accel: how fast do you want to reach the max speed
    Output:
        The motors move that speed
    '''
    if speed > 255 or speed < 0:
      return # do nothing for now, write error message at some point
    self.upperLeft.run(Adafruit_MotorHAT.BACKWARD)
    self.upperRight.run(Adafruit_MotorHAT.FORWARD)
    self.lowerLeft.run(Adafruit_MotorHAT.BACKWARD)
    self.lowerRight.run(Adafruit_MotorHAT.FORWARD)
    #make sure the library is imported from the compass
    for i in range(speed)[::accel]:
      self.upperLeft.setSpeed(i)
      self.upperRight.setSpeed(i)
      self.lowerLeft.setSpeed(i)
      self.lowerRight.setSpeed(i)

  def turnLeft(self,speed =5,accel=10):
    '''
    Input:
      speed: a number from 1-255 which sends a signal to the motor hat to the DC motor to a certain speed
      accel: how fast do you want to reach the max speed
             NOTE: -1 is a special code that tells me that you want to get to maximum speed immediately, it was a hack
    Output:
      The motors move that speed
    '''
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

  def forward(self,speed =255,accel=10,driftRatio=1):
    '''
    Input:
      speed: a number from 1-255 which sends a signal to the motor hat to the DC motor to a certain speed
      accel: how fast do you want to reach the max speed
             NOTE: -1 is a special code that tells me that you want to get to maximum speed immediately, it was a hack
      driftRatio: a number between 1 and 2, honestly it could be larger but the math is hacky that essentially says Move right motors faster than the others
    Output:
      The motors move that speed
    '''
    if speed > 255 or speed < 0:
        return # do nothing for now, write error message at some point
    self.upperLeft.run(Adafruit_MotorHAT.BACKWARD)
    self.upperRight.run(Adafruit_MotorHAT.BACKWARD)
    self.lowerLeft.run(Adafruit_MotorHAT.BACKWARD)
    self.lowerRight.run(Adafruit_MotorHAT.BACKWARD)
    if driftRatio ==1:
      #note that the Math
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
      #hacky solution, try to have one set of wheels accellerate slightly faster than the other wheels

      for i in range(motorSpeed[0],speed*driftRatio)[::accel]:
        self.upperRight.setSpeed(i)
        self.lowerRight.setSpeed(i)
      for i in range(motorSpeed[1],speed)[::accel]:
        self.upperLeft.setSpeed(i)
        self.lowerLeft.setSpeed(i)

      self.motorSpeed=[speed*driftRatio,speed]



  def stop(self,speed=0):
    '''
    Input:
      speed: a number from 1-255 which sends a signal to the motor hat to the DC motor to signify what speed it was moving
    Output:
      The motors stop
    '''
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
