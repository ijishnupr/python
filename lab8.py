import random
rand=random.randint(1,9)
guss=int(input("enter the gussed no:"))
if guss==rand:
    print("the no: you gussed is correct")
elif guss>rand:
    print("the no: you gussed is too high")
else:
    print("the no: you gussed is too low")
