import time,os
from itertools import count
from threading import Thread,current_thread
from multiprocessing import Process,current_process
from time import sleep
from multithreeding import io_b
from multitheiding2 import cpu_b

def read_file(fayl_name:str):
    with open(fayl_name , 'r') as f:
        s=f.read()
    return s
if __name__ == "__main__":
    s_time=time.time()
#singlethreed
    io_b(sleep)
#multithreed
    # t1 = Thread(target=io_b, args=(sleep,))
    # t2 = Thread(target=io_b, args=(sleep,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
#multiprocess
    # p1 = Process(target=cpu_b, args=(count,))
    # p2 = Process(target=cpu_b, args=(count,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    e_time = time.time()
    vaqt = abs(s_time - e_time)
    print(vaqt)

fayl_name="multithreeding.py"
read_file(fayl_name)