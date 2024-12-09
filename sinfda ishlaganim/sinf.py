from random import randrange
a=randrange( -10 , 9)
b=randrange( -10 , 9)
c=randrange( -10 , 9)
d=randrange( -10 , 9)
e=randrange( -10 , 9)
count=0
print(a,b,c,d,e)
if a>0:
 count+=1
if b > 0:
 count += 1
if c > 0:
 count += 1
if d > 0:
 count += 1
if e > 0:
 count += 1
print(count)