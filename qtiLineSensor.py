# -*- coding: utf-8 -*-
#using the gpio tutorial from parallax.com
import wiringpi2 as wp
import RPi.GPIO as GPIO
import time




def initQTI():
    #pin = pinNum
    #ser = serial.Serial("/dev/ttyAMA0",baudrate=9600,timeout=0.0)
    wp.wiringPiSetup()
    wp.wiringPiSetupGpio()
    wp.wiringPiSetupPhys()
    #GPIO.setmode(GPIO.BOARD)
    

    
def getRC(sensorIn=11):
    #make pin output
    wp.pinMode(sensorIn,1)
    #set pin to high to discharge capacitor
    wp.digitalWrite(sensorIn,1)
    #wait 1 ms
    time.sleep(0.01)
    #make pin Input
    wp.pinMode(sensorIn,0)
    #turn off internal pullups
    wp.digitalWrite(sensorIn,0)
    return wp.digitalRead(sensorIn)

def RCTime(pin=11,wiring=True):
    duration=0    
    
    if wiring==True:
        initQTI()
        #make pin output
        wp.pinMode(sensorIn,1)
        #set pin to high to discharge capacitor
        wp.digitalWrite(sensorIn,1)
        #wait 1 ms
        time.sleep(0.1)
        #make pin Input
        wp.pinMode(sensorIn,0)    
        #turn off internal pullups
        wp.digitalWrite(sensorIn,0)
        #t=wp.digitalRead(sensorIn)
        #print wp.digitalRead(sensorIn)
        while wp.digitalRead(sensorIn)==1:
            #wait for the pin to go Low
            #print 'not yet' 
            duration+=1
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
        #wp.digitalWrite(sensorIn,0)
        #GPIO.output(pin,0)

        while True:
            #wait for the pin to go Low
            print GPIO.input(sensorIn)
            duration+=1
    return duration
try:
    wiring=True
    while True:
        print RCTime(11,wiring)
        print RCTime(13,wiring)
        print RCTime(16,wiring)
        print RCTime(18,wiring)
finally:
    if wiring == False:
        GPIO.cleanup()
