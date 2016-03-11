# -*- coding: utf-8 -*-
#using the gpio tutorial from parallax.com note that this is the python translation of the arduino code
#if you are someone else, you only need wiringpi2
#and if you are a beginner, that is sudo pip install wiringpi2
import wiringpi2 as wp
import RPi.GPIO as GPIO
import time

sample=[]
mu=0 # try to calculate mean only once
sd=0 #try to calculate sd only once
rightTail=0
def upMean():
    print sample
    mu=sum(sample)/len(sample)
    
    sd = (sum([ (s-mu)**2 for s in sample])/30.0)**(0.5)
    print sd
    rightTail=int(mu+2*sd)
    print rightTail
def initQTI(wiring=True):
    #pin = pinNum
    if wiring == True:
        wp.wiringPiSetup()
        wp.wiringPiSetupGpio()
        wp.wiringPiSetupPhys()
    else:
        GPIO.setmode(GPIO.BOARD)
    
def initRC(pin):    
    #make pin output
    wp.pinMode(pin,1)
    #set pin to high to discharge capacitor
    wp.digitalWrite(pin,1)
    #wait 1 ms
    #time.sleep(0.1)
    #make pin Input
    wp.pinMode(pin,0)    
    #turn off internal pullups
    #wp.digitalWrite(pin,0)
    
    
#this will get a singe reading, maybe need to figure out how threading works
#and try to make something clever if not put this in a while loop
def getRC(pin=11):
    return wp.digitalRead(pin)
        

#find a way to start up a thread that periodically checked this and stores it in a buffer
#then do some quick statistics to make sure a single bad readng doens't throw this off
    #ABANDON THIS
def RCTime(pin=11,wiring=True,short=False):
    duration=0    
    #not sure if the GPIO version of this translation works,
    #so keep using Wiringpi version
    if wiring==True:
        #initQTI()
        #make pin output
        wp.pinMode(pin,1)
        #set pin to high to discharge capacitor
        wp.digitalWrite(pin,1)
        #wait 1 ms
        time.sleep(0.001)
        #make pin Input
        wp.pinMode(pin,0)    
        #turn off internal pullups
        #wp.digitalWrite(pin,0)
        wp.pullUpDnControl(pin,1)
        if short == True:
            while wp.digitalRead(pin)==1 and duration < rightTail:
                #wait for the pin to go Low
                #print pin,    wp.digitalRead(pin)
                #print 'not yet'
                duration+=1
        else:
            while wp.digitalRead(pin)==1 :
                duration+=1
        #wp.pinMode(pin,1)
        #wp.digitalWrite(pin,1)
    else:
        GPIO.setup(pin,GPIO.OUT)
        #set pin to high to discharge capacitor
        
        GPIO.output(pin,1)
        #wait 1 ms
        time.sleep(0.1)
        #make pin Input
        #GPIO.setup(pin,GPIO.IN)
        GPIO.setup(pin,GPIO.IN,GPIO.PUD_DOWN)
        #turn off internal pullups
        while True:
            #wait for the pin to go Low
            print GPIO.input(sensorIn)
            duration+=1
    return duration
#this is just a test for the wiring, it prints out to the main screen
def main():
    try:
        #this refers to the wiring PI library which on the surface level
        #seems to be the exact same as the RPi.GPIO library
        #I have a problem with getting that library to work and am too lazy to debug it anymore
        #so for now just use the wiringpi2 library as seen here
        wiring=True
        initQTI(wiring)
        
        while True:
            #print '11 : ', RCTime(11,wiring)
            time.sleep(0.1)
            #print '13 : ',RCTime(13,wiring)
            #print '16 : ',RCTime(16,wiring)
            #print '18 : ',RCTime(18,wiring)
            if len(sample) < 30:
                print RCTime(16,wiring)
                
                sample.append(RCTime(pin=16,wiring=wiring, short =False))
            elif len(sample) == 30:
                sample.append(RCTime(pin=16,wiring=wiring, short =False))
                upMean()
            else:
                if RCTime(16,wiring=wiring,short=True) == rightTail:
                    print 'possible detection', rightTail
                    
            
    finally:
        if wiring == False:
            GPIO.cleanup()

main()
