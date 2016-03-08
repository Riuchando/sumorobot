import time
import smbus
#from Adafruit_I2C import Adafruit_I2C as bus
bus = smbus.SMBus(1)
address=0x70
def write(value):
    bus.write_byte_data(address, 0, value)

def lightlevel():
    light=bus.read_byte_data(address,1)
    return light

def rng():
    rng1=bus.read_byte_data(address,2)
    rng2=bus.read_byte_data(address,3)
    print rng1, rng2
    return (rng1<<8)+rng2
def probe():
    for i in range(0x30)[::0x10]:
        print bus.read_byte_data(i,0)
while True :
    write(0x51)
    print rng()
    #print probe()
    time.sleep(0.01)
    
	
