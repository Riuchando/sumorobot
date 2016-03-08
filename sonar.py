import RPi.GPIO as GPIO
import time
def takeMeasurement():
    GPIO.setmode(GPIO.BOARD)

    TRIG=11
    ECHO=13

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.output(TRIG,0)

    GPIO.setup(ECHO,GPIO.IN)
    time.sleep(0.12)
    #print 'Starting measurements...'
    GPIO.output(TRIG,1)
    time.sleep(0.00001)
    GPIO.output(TRIG,0)
    while GPIO.input(ECHO) == 0:
        #print 'infinite loop here'
        pass
    start=time.time()
    while GPIO.input(ECHO) ==1:
        pass
    stop=time.time()
    print (stop - start ) * 17000

def main():
    try:
        while True:
            takeMeasurement()
    finally:
        GPIO.cleanup()
main()
