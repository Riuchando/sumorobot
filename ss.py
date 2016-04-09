from sonar import takeMeasurement
import time
tm=takeMeasurement()
while tm > 30:
    tm= takeMeasurement()
    print tm<30
    if tm< 30:
	break
    pass

time.sleep(5)

