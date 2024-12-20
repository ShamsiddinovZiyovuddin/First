import time,os
from itertools import count
from threading import Thread,current_thread
from multiprocessing import Process,current_process




count=100_000_000
sleep=5

def io_b(sec):
    p_id=os.getpid()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutish boshlandi ")
    time.sleep(sleep)
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutish tugadi")


def cpu_b(k):
    p_id = os.getpid()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutish boshlandi ")
    while k>0:
        k-=1
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutish tugadi")

if __name__ == "__main__":
    s_time=time.time()
    # 1.single_threed i_ob     5.000407695770264
    #
    # io_b(sleep)
    #

    #2 multi_threeding io_b 5.002727031707764

    # t1=Thread(target=io_b,args=(sleep,))
    # t2=Thread(target=io_b,args=(sleep,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # #3 multithreeding cpu_b  0.0020008087158203125

    # t1 = Thread(target=cpu_b, args=(sleep,))
    # t2 = Thread(target=cpu_b, args=(sleep,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # #4 multithreeding cpu_b 14.694947719573975

    # t1 = Thread(target=cpu_b, args=(count,))
    # t2 = Thread(target=cpu_b, args=(count,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # #5 multiproccessing cpu_b 7.68060827255249

    # p1 = Process(target=cpu_b, args=(count,))
    # p2 = Process(target=cpu_b, args=(count,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    # #6 multiprocessing i_ob     5.142765998840332

    # p1 = Process(target=io_b, args=(sleep,))
    # p2 = Process(target=io_b, args=(sleep,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    e_time=time.time()
    vaqt=abs(s_time-e_time)
    print(vaqt)
