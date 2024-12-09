#cning oxiridagi elementlari boshidagi bilan almashishi
b=[4,7,9,1]
c=[3,4,2,5]
k=len(c)//2
for i in range(len(c)//2):
    c[i],c[i+len(c)//2+1]=c[i+len(c)//2+1],c[i]
print(c)