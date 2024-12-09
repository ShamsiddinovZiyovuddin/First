from functools import reduce
x=6
y=5
n=3
print(reduce(lambda x,y:x+y, range(1,n+1)))
a=list(range(1,16))