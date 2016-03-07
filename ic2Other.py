#http://www.instructables.com/id/Raspberry-Pi-I2C-Python/

import smbus
import time
bus = smbus.SMBus(0)
address = 0x70

#SRF08 REQUIRES 5V

def write(value):
        bus.write_byte_data(address, 0, value)
        return -1

def lightlevel():
        light = bus.read_byte_data(address, 1)
        return light

def ic2Range():
        range1 = bus.read_byte_data(address, 2)
        range2 = bus.read_byte_data(address, 3)
        range3 = (range1 << 8) + range2
        return range3

def otherMain():
  while True:
          write(0x51)
          time.sleep(0.7)
          lightlvl = lightlevel()
          rng = range()
          print lightlvl
          print rng
otherMain()
