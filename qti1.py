import RPi.GPIO as GPIO
import time


pin=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.IN, GPIO.PUD_DOWN)

prev=False
curr=False

while True:
    time.sleep(0.10)
    prev=curr
    curr=GPIO.input(pin)
    if curr != prev:
        new='HIGH' if curr else 'LOW'
        print pin, new
    print curr, 'has failed'
    
