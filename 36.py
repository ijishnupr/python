import os
pos=r'C:\Users\DELL\Desktop\just text file.txt'
arr=''
with open(pos,'r') as a:
    for i in a:
        s=i.strip('\n')
        arr=arr+" "+s
print(arr)