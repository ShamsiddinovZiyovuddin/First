from functools import reduce

f=open("file_25.py",'r')
s=f.read()
f.close()
print(s)
a= s.split()
k=list((filter(lambda x:x%2==1,a)))
k1=reduce(lambda x,y:x+y,a)
print(k)
print(k1)

#f1=open("file_25.py",'w')
#f1.write(" ".join(list(map(str,k))))
#f1.close()