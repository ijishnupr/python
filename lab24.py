s=input("enter the string")
a=[]
b=[]
for i in s:
    if i in b:
        a=s.count(i)
        print("the no of {} is {}".format(i,a))
    else:
        b.append(i)