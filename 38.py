import os
pos=r'C:\Users\DELL\Desktop\just text file.txt'
arr=[]
with open(pos,'r') as a:
    for i in a:
        s=i.strip('\n')
        arr.append(s)
print(arr)
lenn="h"
high=0
l=0
for i in arr:
    l=len(i)
    if l>=high:
        high=l
        lenn=i
    else:
        pass
print(lenn)
