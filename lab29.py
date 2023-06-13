a=['bmw','benz','audi','tata','mazda','wv','toyota','byc','kia','ford']
print(a)
s=input("enter the string to find index")
count=0
for i in a:

    if i==s:
        print("found in {}".format(count))
    count=count+1