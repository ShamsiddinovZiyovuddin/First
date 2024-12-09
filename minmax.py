from random import randrange

n = randrange(10, 15)
print("n = ", n)
a = randrange(-100,100)
print("1. ",a)
min = a
for i in range(2,n+1):
    a = randrange(-100, 100)
    print(f"{i}. ", a)
    if min>a:
        min = a