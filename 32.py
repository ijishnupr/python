import os

file_path = r'C:\Users\DELL\Desktop\just text file.txt'  # Use a raw string by adding 'r' prefix
n=int(input("enter the no: of string you want to enter"))
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        print(f.read(n))
else:
    print("File not found")