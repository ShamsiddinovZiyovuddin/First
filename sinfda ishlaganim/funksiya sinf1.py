def toqsum():
    a=[1,2,3,5,6,7,8]
    s=0
    for i in a:
        if i%2==1:
          s+=i
    return s

print(toqsum())