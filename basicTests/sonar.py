#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
#will need to start a thread that has this in a while loop and stores the data in a buffer
#do some quick statistics to make sure the data is good,
#note that this is giving data in seconds that should be in a degree of 10**-4
#might write a coroutine that if enabled, will interrupt this process

def init():
    '''
      Input:
      Output:
        set up all the Pins
    '''
    GPIO.setmode(GPIO.BOARD)

    TRIG=29
    ECHO=31

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.output(TRIG,0)

    GPIO.setup(ECHO,GPIO.IN)
#use the speed of sound to find the distance between sensor and bot
def takeMeasurement():
    GPIO.setmode(GPIO.BOARD)

    TRIG=29
    ECHO=31

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.output(TRIG,0)

    GPIO.setup(ECHO,GPIO.IN)
    time.sleep(0.12)
    #print 'Starting measurements...'
    #seems to send out a sound that lasts like a micro second
    GPIO.output(TRIG,1)
    time.sleep(0.00001)
    GPIO.output(TRIG,0)
    #waits for a response for the sound, should be given in seconds (like fractions of a second)
    while GPIO.input(ECHO) == 0:
        #print 'infinite loop here'
        pass
    #normally the start and end time were in the loop but I THINK that is proccesor intensive, so keep here
    start=time.time()
    #this is another busy wait in here
    while GPIO.input(ECHO) ==1:
        pass
    stop=time.time()
    #print stop - start
    return (stop - start ) * 17000

def main():
    init()
    try:
        while True:
            print takeMeasurement()
    finally:
        GPIO.cleanup()
#main()

