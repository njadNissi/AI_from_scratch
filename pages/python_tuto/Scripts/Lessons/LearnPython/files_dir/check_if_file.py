import os


fileName1 = r"C:\Users\njad\Documents\file1.txt"

if os.path.isfile(fileName1):
    print('The file exits')
else:
    print("The file doesn't exist")
