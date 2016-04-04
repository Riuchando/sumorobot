from multiprocessing import Pipe,Process
from qtilClass import *
from sonar import takeMeasurement


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

def eachSensor(pipe,pin):
    toMainPipe, fromMainPipe= pipe
    x=qtiWrapper(wiring=False)
    while True:
	if x.detect(pin, wiring=False)==True:
	    toMainPipe.send(pin)
def sonarMulti(pipe):
    toMainPipe, fromMainPipe= pipe
    while True:
	tm=takeMeasurement()
	#print tm
	if tm <30:
	    toMainPipe.send(tm)


def multiMain():
    send, recv=Pipe()
    pins=[11,13,16,18]
    #pool=Pool=(processes=4)
    workers=[Process(target=eachSensor, args=((send,recv),pin) )  for pin in pins]
    for worker in workers:
	worker.start()
    sonar=Process(target=sonarMulti,args=((send,recv),))
    sonar.start()
    while True:
	msg=recv.recv()
	print msg
	#if msg==13 or msg ==11:
	#    break
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




sonarMain()
#multiMain()
#main()
