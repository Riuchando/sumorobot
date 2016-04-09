# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import math
class sonarWrapper():
  #will need to start a thread that has this in a while loop and stores the data in a buffer
  #do some quick statistics to make sure the data is good,
  #note that this is giving data in seconds that should be in a degree of 10**-4
  #might write a coroutine that if enabled, will interrupt this process
  def __init__(self):
      #GPIO.setmode(GPIO.BOARD)
      #pin numbers
      self.TRIG=29
      self.ECHO=31
      #sample statistics
      self.sample=[]
      self.sampleSize=32
      #in cm, what is a default, there might be a thing there
      self.goodReading=30
      self.mean=0
      self.sd=0
      self.rightTail=0
      #set to false, need to have test
      self.detected=False
      #set to junk value, will be used to have it follow hand movements
      self.detectDist=-1


  def takeMeasurement(self):
      self.TRIG=29
      self.ECHO=31
      GPIO.setup(self.TRIG,GPIO.OUT)
      GPIO.output(self.TRIG,0)

      GPIO.setup(self.ECHO,GPIO.IN)
      time.sleep(0.12)
      #print 'Starting measurements...'
      #seems to send out a sound that lasts like a micro second
      GPIO.output(self.TRIG,1)
      time.sleep(0.00001)
      GPIO.output(self.TRIG,0)
      #waits for a response for the sound, should be given in seconds (like fractions of a second)
      while GPIO.input(self.ECHO) == 0:
          #print 'infinite loop here'
          pass
      #normally the start and end time were in the loop but I THINK that is proccesor intensive, so keep here
      start=time.time()
      #this is another busy wait in here
      while GPIO.input(self.ECHO) ==1:
          pass
      stop=time.time()
      #print stop - start
      return (stop - start ) * 17000

  def sonarLoop(self):
      if self.detected==False:
        if len(sampleSize)<32: # assume that it is not facing the robot
          while len(self.sample) < self.sampleSize:
            sonarDist=self.takeMeasurement()
            self.sample.append(sonarDist)
            if sonarDist < self.goodReading:
              self.detected =True
              self.sonarLoop() #exit this
          #when I have enough samples
          self.mean=sum(self.sample)/self.sampleSize
          self.sd=math.sqrt(sum([ (x - self.mean)**2 for x in self.sample])/self.sampleSize)
          #this is a crude hacky way to do hypothesis testing, essentially
          self.rightTail=self.mean-self.sd*2
        #sonarDist= self.takeMeasurement()
        #assume that a good reading is more accurate for now
        while True:
          sonarDist= self.takeMeasurement()
          if sonarDist < self.goodReading:
              self.detected =True
              self.sonarLoop() #exit this

      else: # the item is detected
        sonarDist=self.takeMeasurement()
        #might use statistics, I dunno
        if sonarDist> self.goodReading :
          self.detected=False
          return
        while self.takeMeasurement() < self.goodReading:
          pass


  def main():
      try:
          while True:
              self.takeMeasurement()
      finally:
          GPIO.cleanup()
  #main()

