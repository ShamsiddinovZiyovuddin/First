from random import randint

a=randint(1,10)
b=randint(1,10)
f=lambda a,b: pow(a,2)+pow(b,2)
print(f(2,3))