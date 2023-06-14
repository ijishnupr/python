import os

file_path = r'C:\Users\DELL\Desktop\just text file.txt'  # Use a raw string by adding 'r' prefix
if os.path.exists(file_path):
    with open(file_path, 'a+') as f:
        f.seek(0)  # Move the file pointer to the beginning
        print(f.read())
        f.write(input("Enter the string to append: "))
        f.seek(0)  # Move the file pointer back to the beginning after writing
        print(f.read())
else:
    print("File not found")
