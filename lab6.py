tex=input("enter the string")
rev=tex[::-1]
print(rev)
if rev==tex:
    print("The string you entered is a palindrom")
else:
    print("It is not a palindrome")