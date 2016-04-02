import time
from movement import *
from qtitest import RCtime
from sonar import takeMeasurement

def linetest():
	while RCtime < 20:
		print RCtime

	back(speed=70,accel=10)
	stop()
try:

	linetest()
finally:

	stop()

