import os


fileName1 = r"C: \Users\njad\Documents\\"

if os.path.isdir(fileName1):
    print('The directory exits')
else:
    print("The directory doesn't exist")
