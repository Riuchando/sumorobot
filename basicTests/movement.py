#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
mh = Adafruit_MotorHAT(addr=0x70) #note stopping this program DOES NOT stop the motor
#we COULD make this an array but for programming simplicity, have 4 variables
upperLeft=mh.getMotor(1)
upperRight=mh.getMotor(2)
lowerLeft=mh.getMotor(3)
lowerRight=mh.getMotor(4)


def back(speed =100,accel=20):
  '''
  Input:
    speed: a number from 1-255 which sends a signal to the motor hat to the DC motor to a certain speed
    accel: how fast do you want to reach the max speed
  Output:
    The motors move that speed
  '''
  if speed > 255 or speed < 0:
    return # do nothing for now, write error message at some point
  #initialize the direction of the motors, in our case it was backwards
  upperLeft.run(Adafruit_MotorHAT.FORWARD)
  upperRight.run(Adafruit_MotorHAT.FORWARD)
  lowerLeft.run(Adafruit_MotorHAT.FORWARD)
  lowerRight.run(Adafruit_MotorHAT.FORWARD)
  #slowly accellerate the motors so they aren't jerky,
  #think of someone constantly stopping and starting car

  for i in range(speed)[::accel]:
    upperLeft.setSpeed(i)
    upperRight.setSpeed(i)
    lowerLeft.setSpeed(i)
    lowerRight.setSpeed(i)

def turnRight(speed =5, accel=20):
    '''
  Input:
    speed: a number from 1-255 which sends a signal to the motor hat to the DC motor to a certain speed
    accel: how fast do you want to reach the max speed
  Output:
    The motors move that speed
  '''

  #depending on the output for compass sensor,
  #figure out Radians or Degrees
  #also write some simple algos to have the ultra sonic sensor help where the thing is
  if speed > 255 or speed < 0:
    return # do nothing for now, write error message at some point
  upperLeft.run(Adafruit_MotorHAT.BACKWARD)
  upperRight.run(Adafruit_MotorHAT.FORWARD)
  lowerLeft.run(Adafruit_MotorHAT.BACKWARD)
  lowerRight.run(Adafruit_MotorHAT.FORWARD)
  for i in range(speed)[::accel]:
    upperLeft.setSpeed(i)
    upperRight.setSpeed(i)
    lowerLeft.setSpeed(i)
    lowerRight.setSpeed(i)

def turnLeft(speed =5,accel=10):
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

#this is a test to make each wheel is working, used for debugging if the wheels are put on correctly, if not, change the functions FORWARD to BACKWARD
#the order is upperLeft, upperRight, lowerLeft, lowerRight
def oneWheelTime(speed=255, accel=10):
    '''
  Input:
    speed: a number from 1-255 which sends a signal to the motor hat to the DC motor to a certain speed
    accel: how fast do you want to reach the max speed
  Output:
    The motors move that speed
  '''
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


def forward(speed =255,accel=10):
    '''
  Input:
    speed: a number from 1-255 which sends a signal to the motor hat to the DC motor to a certain speed
    accel: how fast do you want to reach the max speed
  Output:
    The motors move that speed
  '''
  #need to set up the detection on seeing if the motors can be run in parellel
  if speed > 255 or speed < 0:
    return # do nothing for now, write error message at some point
  upperLeft.run(Adafruit_MotorHAT.BACKWARD)
  upperRight.run(Adafruit_MotorHAT.BACKWARD)
  lowerLeft.run(Adafruit_MotorHAT.BACKWARD)
  lowerRight.run(Adafruit_MotorHAT.BACKWARD)
  for i in range(speed)[::accel]:
    #print i
    upperLeft.setSpeed(i)
    upperRight.setSpeed(i*driftRatio)
    lowerLeft.setSpeed(i)
    lowerRight.setSpeed(i*driftRatio)

    #time.sleep(0.05) # this makes the acceleration slower/faster, debug to find a good amount of time

def stop(speed=0):
  #decellerates, then stops
    '''
  Input:
    speed: a number from 1-255 which sends a signal to the motor hat to the DC motor to a certain speed, in this case it tries to decellerate
  Output:
    The motors stop
  '''
  for i in range(speed)[::-1]:
    upperLeft.setSpeed(i)
    upperRight.setSpeed(i)
    lowerLeft.setSpeed(i)
    lowerRight.setSpeed(i)
  #this is in the code to allow for the wheels to be "free"
  upperLeft.run(Adafruit_MotorHAT.RELEASE)
  upperRight.run(Adafruit_MotorHAT.RELEASE)
  lowerLeft.run(Adafruit_MotorHAT.RELEASE)
  lowerRight.run(Adafruit_MotorHAT.RELEASE)

#this was a playground to make sure the movement worked as expected
def movementTest():
  try:
    forward(75)
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
#uncomment the movement test to run the program from the commandline as python movement.py
#movementTest()
