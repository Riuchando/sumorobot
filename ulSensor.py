import RPi.GPIO as GPIO
import time
from datetime import datetime

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
TRIG=16
#TRIG=23
GPIO.setup(TRIG,GPIO.OUT)
ECHO=18
#ECHO=24
GPIO.setup(ECHO,GPIO.IN)
'''
GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,0)

GPIO.setup(ECHO,GPIO.IN)
time.sleep(0.12)
print 'Starting measurements...'
GPIO.output(TRIG,1)
time.sleep(0.00001)
GPIO.output(TRIG,0)
while GPIO.input(ECHO) == 0:
    print 'infinite loop here'
    pass
start=time.time()
while GPIO.input(ECHO) ==1:
    pass
stop=time.time()
print (stop - start ) * 17000

GPIO.cleanup()
'''
def read_distance():
        GPIO.output(TRIG,True)
        time.sleep(0.01)
        GPIO.output(TRIG,False)
        #signaloff=0
        while GPIO.input(ECHO)==0:
            #print 'no dammit'
            pass
        #start=datetime.now().microsecond
        start=time.time()
        while GPIO.input(ECHO)==1:
            #   signalon=time.time()
            pass
        #stop=datetime.now().microsecond
        stop=time.time()
        distance=(stop-start)*17000
        print 'start : ', start, ' end : ', stop, ' subtracted : ', stop-start 
        
        return distance
        
try:
    i=0
    #while i<100:
    #    print read_distance()
    #    time.sleep(0.5)
    #    i+=1
    print read_distance()
    GPIO.cleanup()
except KeyboardInterrupt:
    print 'cleanup : '
    GPIO.cleanup()
