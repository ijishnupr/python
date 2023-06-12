import datetime
name=input("enter you name")
age=int(input("enter your age"))
y=datetime.datetime.now().year
diff=100-age
cent=diff+y
print("hello {0} your will become 100 years old at the year {1}" .format(name,cent) )