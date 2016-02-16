#!/usr/bin/env python

#import Image
import time
import serial
#import pygame
import sys

#size = ( 1640 , 1480 )
#screen = pygame.display.set_mode(size)
#clock = pygame.time.Clock()
#imageFile = "pic.jpg"
#blackscreen = "black.jpg"
#img = pygame.image.load(imageFile)
#bimg = pygame.image.load(blackscreen)
controller=0
counter=0
temp = ''
tempString=0
rcvString=0
var = 0
var2 = 0

ser = serial.Serial("/dev/ttyAMA0",baudrate=9600,timeout=0.0)
while 1:
        time.sleep(0.09)
        #read 10 bits, anything below 10 doesnt promise you'll get all the  info you need
        rcv = ser.read(10)
        #if the reading is ' ' then no data was sent over the connection / elimnates useless info
        if rcv != ' ':
               print (rcv)
               #if current reading is less than value in temp variable, DO Another read
               #time.sleep(.19)
               while 1:
                time.sleep(0.09)
                temp=ser.read(10)
                if temp != ' ':
                        break
               if temp <  rcv:
                       while 1:
                        time.sleep(0.09)
                        rcv = ser.read(10)
                        if rcv != ' ':
                                break
                       if rcv < temp:
                               counter+=1
                       else:
                               controller+=1
                               if controller == 5:
                                 controller = 0
                                 counter = 0


        if counter == 5:
                while True:
                        start = time.clock()
                        screen.blit(img,(0,0))
                        pygame.display.update()
                        if(start>8):
                                time.sleep(8)
                                screen.blit(bimg,(0,0))
                                pygame.display.update()
                                #execfile("serial_write.py")
                                #sys.exit()
                                break
                counter = 0
                controller = 0

