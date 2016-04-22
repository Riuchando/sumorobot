# -*- coding: utf-8 -*-
#THIS IS THE NEW VERSION THAT WILL HAVE MAJOR PARTS REMOVED
#using the gpio tutorial from parallax.com note that this is the python translation of the arduino code
#if you are someone else, you only need wiringpi2
#and if you are a beginner, that is sudo pip install wiringpi2

import RPi.GPIO as GPIO
import time
class qtiWrapper:
    #this will store statistics, for now it is using simple knowledge of standard deviation to avoid taking too much time on the clock
    def __init__(self):
        '''
          Input:
          Output:
            Everything is set up, un comment for it to begin taking samples of ground
        '''
        self.sample=[]
        self.mu=0 # try to calculate mean only once
        self.sd=0 #try to calculate sd only once
        #self.pin=pin
        self.rightTail=0
        self.cap=30
        self.maxSampleSize=30
        #might put initQTI here
  	    GPIO.setmode(GPIO.BOARD)
        #self.gatherSample(pin=18,wiring=wiring)


    #update the mean value of the sensor
    def upMean(self):
        '''
          Input:
          Output:
            The Mean and standard deviation are saved locally
        '''

        #print self.sample
        self.mu=sum(self.sample)/len(self.sample)
        self.sd = (sum([ (s-self.mu)**2 for s in self.sample])/30.0)**(0.5)
        self.rightTail=int(self.mu+2*self.sd)



    def RCTime(self,pin=11):
        '''
          Input:
            might change this so that Pin is tied to the class to reduce verbosity
            pin: the pin to take calculations from
          Output:
            The Mean and standard deviation are saved locally
        '''
        duration=0
        #not sure if the GPIO version of this translation works,
        GPIO.setup(pin,GPIO.OUT)
        #set pin to high to discharge capacitor
        GPIO.output(pin,GPIO.LOW)
        #wait 1 ms
        time.sleep(0.1)
        #make pin Input
        GPIO.setup(pin,GPIO.IN)
        #GPIO.setup(pin,GPIO.IN,GPIO.PUD_DOWN)
        #turn off internal pullups
        while GPIO.input(pin)== GPIO.LOW:
            #wait for the pin to go Low
            #print GPIO.input(sensorIn)
            duration+=1
        return duration


    #note that the variagble of wiring might be put everywhere
    #at this point, I think I'll stick to wiringpi2 over GPIO, but I won't know
    def gatherSample(self,pin=16):
        '''
          Input:
            might change this so that Pin is tied to the class to reduce verbosity
            pin: the pin to take calculations from
          Output:
            this gathers about 30 samples of the ground then updates the Mean and standard deviation
            so that when it comes to calculate later it can know if a value is strange or not
        '''

        while len(self.sample)< self.maxSampleSize:
            self.sample.append(self.RCTime(pin=pin))
        self.upMean()

    #this will probably be the one for the actual data gathering from other
    #can't decide if this should have it's own infinite loop and be a separate process
    #or should be a single bool that takes appx 776 ns to calculate
    #changing this to allow for testing with dark background with light
    def detect(self,pin):
      '''
        Input:
          pin: the pin to calculations from
        Output:
            True or false that says if the pin connections is good
      '''
			return self.RCTime(pin=pin,wiring=wiring,short=short)>=self.cap

    def detectList(self,pinList ):
      '''
        Input:
          pinlist : a list of pins to take calculations from
        Output:
            True or false that says if any of the pins detected something
      '''
      for pin in pinList:
        if self.detect(pin) == True:
          return True
      return False

#x=qtiWrapper()
#x.main()
#x.getAllTest()
