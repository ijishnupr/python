import os
pos=r'C:\Users\DELL\Desktop\just text file.txt'
pos2=r'C:\Users\DELL\Desktop\textcopied.txt'
with open(pos,'r') as a:
    s=a.read()
    with open(pos2,'w+') as b:
        b.write(s)
    with open(pos2,'r') as b:
        print(b.read())
    del s




