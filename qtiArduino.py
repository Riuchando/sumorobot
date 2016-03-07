# -*- coding: utf-8 -*-
#using the gpio tutorial from parallax.com
import wiringpi2 as wp
import time


pin=10

def initQTI():
    #pin = pinNum
    #ser = serial.Serial("/dev/ttyAMA0",baudrate=9600,timeout=0.0)
    wp.wiringPiSetup()
    wp.wiringPiSetupGpio()
    wp.wiringPiSetupPhys()
    
def getRC(sensorIn=10):
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

def RCTime(sensorIn=10):
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
    duration=0
    while wp.digitalRead(sensorIn):
        #wait for the pin to go Low
        print wp.digitalRead(sensorIn)
        duration+=1
    return 0
initQTI()
print RCTime(pin)