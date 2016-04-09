#!/usr/bin/python
import signal, os
import random
import time
from multiprocessing import Process
import multiprocessing
#import multiprocessing.Process
import Queue
#import subprocess

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")


def toMain(toMainPipe,fromMainPipe):
    #just seeing if this will work
    i=0
    pins=[11,13,16,18]
    while True:
      #interrupt signal
      #if fromMainPipe == True:
      #    return
      for pin in pins:
        #sends detection signal to main
        if random.randint(1,pin) > 7:
          toMainPipe.send(pin)
          i+=1
        if i>100:
          time.sleep(100)

def main():
    send, recv=Pipe()
    p= Process(target=toMain, args=(send,recv))
    p.start()
    signal.signal(signal.SIGALRM, toMain)
    signal.alarm(5)

    while True:
      #try:
      #ismsg=recv.poll(5)
      # Call receive_alarm in 2 seconds

      #if  ismsg== False:
      #  print "!!!!!"
      #print "ismsg",ismsg
      msg=recv.recv()

      # Set the signal handler and a 5-second alarm
      #signal.signal(signal.SIGALRM, toMain)
      #signal.alarm(5)
      print msg
      #if msg == 13 or msg==16:
      #    break
      #except EOFError:
      #    break
    p.join()
    send.close()
    recv.close()

def queueImpl(q):
  i=0
  pins=[11,13,16,18]
  while True:
    #interrupt signal
    #if fromMainPipe == True:
    #    return
    for pin in pins:
    #sends detection signal to main
      if random.randint(1,pin) > 7:
        q.put(pin)
        i+=1
      if i>100:
        time.sleep(100)
def queueMain():
  q= multiprocessing.Queue()
  p= Process(target=queueImpl, args=(q,))
  p.start()
  t=0
  while True:
    try:
      t+=q.get(True,1)

    except Queue.Empty:
      print "TIMEOUT"
      p.terminate()
      print t
      break

def otherMain():
  while True:
    r=random.randint(1,100)
    if  r > 50:
      queueMain()


#queueMain()
otherMain()