def seria_list(a:list):
    b=[]
    c=[]
    b.append(a[0])
    c.append(1)
    k=0
    for i in range(1,len(a)):
        if a[i]==a[i-1]:
            c[k]+=1
        else:
            b.append(a[i])
            c.append(1)
            k+=1
    return b,c
a=[10,10,10,1,1,1,1,2,2]
print(seria_list(a))
#!!!
#a=[1,1,1,1,2,2,34,34,34,8888,8888,8888,8888]
#b=[1,2,34,8888]
#c=[4,2,3,4]
#!!!
# orqamachasi
def seria_list(b:list,c:list):
    a=[]
    for i in range(len(b)):
        for j in range(c[i]):
            a.append(b[i])
    return a


