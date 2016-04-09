#!/usr/bin/python
from multiprocessing import Pipe,Process
from qtilClass import *
#from sonar import takeMeasurement
from sonarClass import *
from moveClass import *
import RPi.GPIO as GPIO
import time
import Queue
import multiprocessing
def toMain(toMainPipe,fromMainPipe):
	#just seeing if this will work
    x=qtiWrapper(wiring=False)
    pins=[11,13,16,18]
    while True:
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
def eachSensor(q,pin,qtiref):
    #toMainPipe, fromMainPipe= pipe
    #qtiref=qtiWrapper(wiring=False)
    while True:
      if qtiref.detect(pin, wiring=False)==True:
          #toMainPipe.send(pin)
          print qtiref.RCTime(pin,wiring=False)
          q.put(pin)

def sonarMulti(q,sonarRef):
    #toMainPipe, fromMainPipe= pipe
    while True:
		tm=sonarRef.takeMeasurement()
		#print tm
		#with current calculations this is 100 cm
		if tm <100:
        	#q.send(tm)
			q.put(tm)

def multiMain(qtiref,sonarRef,m):
    #I read that pipe is faster, but the signal kill was too obtuse
    q=multiprocessing.Queue()
    sonarQ=multiprocessing.Queue()
    #time.sleep(5)
    #send, recv=Pipe()
    pins=[11,13,16,18]
    #pool=Pool=(processes=4)
    #m=motors()


    #m.turnLeft(speed=100)
    #qtiref=qtiWrapper(wiring=False)
    #workers=[Process(target=eachSensor, args=((send,recv),pin, qtiref) )  for pin in pins]
    workers=[Process(target=eachSensor, args=(q,pin, qtiref) )  for pin in pins[0:2]]
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
    m.turnLeft(speed=200,accel=-1)

    sonar=Process(target=sonarMulti,args=(sonarQ,sonarRef))
    sonar.start()

    prev=-1
    msg=0
    while True:
      #msg=recv.recv()
      try:
          sonMsg=soarQ.get(True, 3)
  	      #print msg
      except Queue.Empty:
          print "TIMEOUT"
          m.stop()
          return
      
      #if isinstance(sonMsg ,float):
		  #this means that it is from the sonar instead of from the qti
		  #stop()
      print msg
      if prev> sonMsg:
	      m.forward(speed=100,driftRatio=1.2)    
      else:
	      m.forward(speed=250)	  
      prev=sonMsg
      
       
      #interrupt signal, make sure that this is accurrate
      msg=q.get(True,1)
      if msg==13 or msg ==11:
		redirect(m)
		#print 'detect front'
		pass

    #close Program
    for worker in workers:
	    worker.join()
      #hopefully this is not problem so here's an alternative
      #worker.terminate()

    sonar.join()
    #sonar.terminate()
    send.close()
    recv.close()

def redirect(m):
	m.stop()
	m.back(speed=250)
	time.sleep(0.0001)
	m.turnLeft(speed=250,accel=-1)
	time.sleep(0.0001)
	m.forward(speed=250)

def sonarMain(q):
    #send, recv=Pipe()
    sonar=Process(target=sonarMulti,args=((send,recv),))
    sonar.start()
    while True:
        #msg=recv.recv()
        print msg

    sonar.join()
    #recv.close()


def entireWrapper():
	qtiRef=qtiWrapper(wiring=False)
	sonarRef=sonarWrapper()
	m=motors()
	#qtiRef.init()
	#sonarRef.init()
	while True:
		#this is to turn on, should be a button click and a hand wave for confirmation
		sonar=sonarRef.takeMeasurement()
   		if sonar <30:
			try:
				time.sleep(2.5)
				multiMain(qtiRef, sonarRef, m)
				sonar=900
			finally:
				m.stop()

#sonarMain()
#multiMain()
entireWrapper()
#main()
