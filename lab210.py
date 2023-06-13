a=('bmw','benz','audi','tata','mazda','wv','toyota','byc','kia','ford')
i=len(a)
b=[]
while i>=0:
    b.append(a[i-1])
    i=i-1
a=tuple(b)
print(a)