from random import randrange
s=0
n=randrange(1,10)
print(n)
for i in range(1,n+1):
   k=1
   for j in range(n+1-i):
       k*=i
       s+=k
print(s)