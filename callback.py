import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG=23
GPIO.setup(TRIG,GPIO.OUT)

ECHO=24
GPIO.setup(ECHO,GPIO.IN)

def distanceCallback():
    if GPIO.input(ECHO):
        print 'rising edge'
    else :
        print 'falling edge'

t=time.time()
GPIO.add_event_detect(24,GPIO.RISING, callback=distanceCallback)
print (time.time()-t)*17000
try:
    time.sleep(30)
finally:
    GPIO.cleanup()
