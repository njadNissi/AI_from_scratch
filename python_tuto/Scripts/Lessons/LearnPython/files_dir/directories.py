import os


filename = input("Input the path to file: ")

if os.path.exists(filename):
    print("File <<" + filename + ">> found!")
else:
    print("File <<" + filename + ">> not found!")
