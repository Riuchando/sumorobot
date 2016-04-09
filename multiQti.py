from multiprocessing import Pipe,Process
from qtilClass import *
#from sonar import takeMeasurement
from sonarClass import *
from moveClass import *
import RPi.GPIO as GPIO 
import time


def toMain(toMainPipe,fromMainPipe):
    #just seeing if this will work
    x=qtiWrapper(wiring=False)
    pins=[11,13,16,18]
    while True:
      #interrupt signal
      #if fromMainPipe == True:
      #    return
      for pin in pins:
        #sends detection signal to main
        if x.detect(pin, wiring=False) == True:
          toMainPipe.send(pin)


def main():
    send, recv=Pipe()
    p= Process(target=toMain, args=(send,recv))
    p.start()
    while True:
      #try:
      msg=recv.recv()
      print msg
      #if msg == 13 or msg==16:
      #    break
      #except EOFError:
      #    break
    p.join()
    send.close()
    recv.close()

#parallel processing qti sensor
def eachSensor(pipe,pin,qtiref):
    toMainPipe, fromMainPipe= pipe
    #qtiref=qtiWrapper(wiring=False)
    while True:
      if qtiref.detect(pin, wiring=False)==True:
          toMainPipe.send(pin)


def sonarMulti(pipe,sonarRef):
    toMainPipe, fromMainPipe= pipe
    while True:
	tm=sonarRef.takeMeasurement()
    	#print tm
        if tm <30:
           toMainPipe.send(tm)


def multiMain():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7,GPIO.IN)
   

    while GPIO.input(7)==0:
	print 'wait'

    time.sleep(5) 
    send, recv=Pipe()
    pins=[11,13,16,18]
    #pool=Pool=(processes=4)
    m=motors()
    
        
    #m.turnLeft(speed=100)
    qtiref=qtiWrapper(wiring=False)
    workers=[Process(target=eachSensor, args=((send,recv),pin, qtiref) )  for pin in pins]

    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(7,GPIO.IN)
    #for worker in workers:
    #    worker.start()
    #while GPIO.input(7) == 0:
    #    print 'wait'
    # 	pass
    
    #time.sleep(5)
    for worker in workers:
	worker.start()
    m.turnLeft(speed=100,accel=-1)
    sonarRef=sonarWrapper()
    sonar=Process(target=sonarMulti,args=((send,recv),sonarRef))
    sonar.start()
    
    prev=-1
    while True:
	    msg=recv.recv()
	    #print msg
            if isinstance(msg ,float):
		#this means that it is from the sonar instead of from the qti
		#stop()
		if prev> msg:
		    m.forward(speed=100,driftRatio=1.2)
		else:
		    m.forward(speed=250)
		prev=msg
            #interrupt signal, make sure that this is accurrate
            if msg==13 or msg ==11:
		stop()
                break
	    

    
    #close Program
    for worker in workers:
	    worker.join()

    sonar.join()
    send.close()
    recv.close()

def sonarMain():
    send, recv=Pipe()
    sonar=Process(target=sonarMulti,args=((send,recv),))
    sonar.start()
    while True:
        msg=recv.recv()
        print msg

    sonar.join()
    recv.close()




#sonarMain()
multiMain()
#main()
