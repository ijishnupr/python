import os

file_path = r'C:\Users\DELL\Desktop\just text file.txt'  # Use a raw string by adding 'r' prefix
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        print(f.read())
else:
    print("File not found")
