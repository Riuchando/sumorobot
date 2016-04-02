
import RPi.GPIO as GPIO, time
from movement import *
import time

# Tell the GPIO library to use
# Broadcom GPIO references
GPIO.setmode(GPIO.BOARD)

# Define function to measure charge time
def RCtime (PiPin):
 
  measurement = 0
  # Discharge capacitor
  GPIO.setup(PiPin, GPIO.OUT)
  GPIO.output(PiPin, GPIO.LOW)
  time.sleep(0.1)

  GPIO.setup(PiPin, GPIO.IN)
  # Count loops until voltage across
  # capacitor reads high on GPIO
  while (GPIO.input(PiPin) == GPIO.LOW):
    measurement += 1

  return measurement

# Main program loop
#if  True:
back(speed=70)   
while True:
   pins=[11,13,16,18]
   GPIOS=[17,27,23,24]
   for pin in pins:
      if RCtime(pin)>30:
	stop()
	break
stop()
 # print RCtime(4) # Measure timing using GPI04
