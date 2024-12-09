from random import randint
n=randint(1,20)
s=0
print(n)
a=[]
for i in range(1,n+1):
   s=randint(1,20)
   if s%2==1:
       a.append(s)
print(a)
