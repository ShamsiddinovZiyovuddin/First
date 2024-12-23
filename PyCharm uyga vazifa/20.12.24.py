#1dan 101gacha;juft elementlari ko'paytmasiga toq elementlar ko'paytmasini ayiradigan funksiya
#shuni single,multi threed va multiproccessingda tekshirib kurish
import time,os
from functools import total_ordering
from itertools import count
from threading import Thread,current_thread
from multiprocessing import Process,current_process

sleep=5
import time
def read_file(fayl_name:str):
    with open(fayl_name  , 'r') as file:
        s=file.read()

    return s
fayl_name='toq_juft.py'
read_file(fayl_name)
def add_list(sec):
    a=[h for h in range(1,101)]
    j=1
    t=1
    total=0
    for i in a:
        if i%2==0:
          j*=i
        elif i%2==1:
            t*=i
    total+=j-t

    time.sleep(sleep)

    print("javob:",total)
    print()
    print()
if __name__=="__main__":
            s_time=time.time()
            #1 vaqt= 5.0018134117126465
            # add_list(sleep)
            #2 vaqt= 5.0016844272613525

            # t1 = Thread(target=add_list, args=(sleep,))
            # t2 = Thread(target=add_list, args=(sleep,))
            # t1.start()
            # t2.start()
            # t1.join()
            # t2.join()
            #3 vaqt= 5.184368133544922

            # p1 = Process(target=add_list, args=(sleep,))
            # p2 = Process(target=add_list, args=(sleep,))
            # p1.start()
            # p2.start()
            # p1.join()
            # p2.join()

            e_time = time.time()
            vaqt=abs(s_time-e_time)
            print("vaqt=",vaqt)
