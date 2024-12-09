from random import randrange

from sinf import count

n=randrange(100000000,1000000000)
print("n=",n)
s=0
count=0
while n>0:
    k1=n%10
    if k1%2==0:
        s+=k1
        count+=1

     n//10
    print("n= ",n)

print("s=",s)