import time,os
from itertools import count
from threading import Thread,current_thread
from multiprocessing import Process,current_process
from time import sleep

count1=100_000_000
sleep1=5

def cpu_b(k):
    p_id = os.getpid()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutish boshlandi ")
    while k>0:
        k-=1
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutish tugadi")