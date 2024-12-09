from itertools import count


def str_count(s1:str,s2:str):
    count=0
    for i in range(len(s1)):
       if s1[i:len(s2)+i]==s2:
           count+=1

    return count

s1='absxf sssdb sss ksss'
s2='sss'
print(str_count(s1,s2))
