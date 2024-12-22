#1dan 101gacha;juft elementlari ko'paytmasiga toq elementlar ko'paytmasini ayiradigan funksiya
#shuni single,multi threed va multiproccessingda tekshirib kurish
import a

sleep=5
import time
def read_file(f_name:str):
    with open(f_name  , 'r') as file:
        s=file.read()

    return s
f_name='toq_juft.py'
read_file(f_name)
def add_list(a:list,sec):
    for i in a:
        j=1
        t=1
        if i%2==0:
          j*=i
        if i%2==1:
            t*=i

        total=j-t
        print("javob:",total)
        if __name__=="__main__":
            s_time=time.time()
            add_list(a,5)

            e_time = time.time()
            vaqt=s_time-e_time
            print(vaqt)
a= [a for i in range(1,101)]
add_list(a)
