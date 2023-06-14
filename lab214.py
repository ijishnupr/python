a={'name1':'jishnu','name2':'sachu','name3':'rejani','name4':'pradeep'}
s=input("enter the no:")
if s in a:
    print(a[s])
    del a[s]
    print(a[s])