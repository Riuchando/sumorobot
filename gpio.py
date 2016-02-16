#http://raspi.tv/2013/rpi-gpio-basics-5-setting-up-and-using-outputs-with-rpi-gpio
#https://solarbotics.com/download.php?file=514


#LineSnsrPwr CON 10 ' line sensor power
#LineSnsrIn CON 9 ' line sensor input
#ClrEOL CON 11 ' clear to end of line (DEBUG)
#Sense VAR Word ' sensor raw reading
#HIGH LineSnsrPwr ' activate sensor
#HIGH LineSnsrIn ' discharge QTI cap
#PAUSE 1
#RCTIME LineSnsrIn, 1, Sense ' read sensor value
#LOW LineSnsrPwr ' deactivate sensor
#DEBUG Home
#DEBUG "Sensor ", CR
#DEBUG "-----", CR
#DEBUG DEC Sense, ClrEOL
#PAUSE 100
#GOTO Read_Sensor


import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep             # lets us have a delay
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD
GPIO.setup(10, GPIO.OUT)           # set GPIO24 as an output

try:
    while True:
        GPIO.output(10, 1)         # set GPIO24 to 1/GPIO.HIGH/True
        sleep(0.5)                 # wait half a second
        if GPIO.input(9):
            print "Line Sensed"
        GPIO.output(24, 0)         # set GPIO24 to 0/GPIO.LOW/False
        sleep(0.5)                 # wait half a second
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()                 # resets all GPIO ports used by this program
