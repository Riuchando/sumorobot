import multiprocessing
from qtilClass import *
#from multiprocessing import Process
from multiprocessing import Pool
pool = Pool(4)
x=qtiWrapper(wiring=False)
pins=[11,13,16,18]
#detect=x.detect()
#for pin in pins:
#    print Process(target=x.detect,args=( pin,False,False )).start()
pool.map(x.detect, args=(pins,False,False))



