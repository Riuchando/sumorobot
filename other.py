from multiprocessing import Pool
def f(x): print(x)  # FIRST
p = Pool(3) # SECOND
p.map(f, range(20))
