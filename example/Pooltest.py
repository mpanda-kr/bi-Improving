from multiprocessing import Pool
import time
import os
import math


def f(x):
    print("valus", x, " : Pid = ",os.getpid())
    time.sleep(1)
    return x*x

if __name__ == '__main__':
    p = Pool(3)
    startTime = int(time.time())
    print(p.map(f, range(0,10)))  
    endTime = int(time.time())
    print("during time : ", (endTime - startTime))
