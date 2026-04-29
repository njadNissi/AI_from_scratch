# Program to show various ways to read and write data in a file.
# modes : open for
# r: reading | w: writing | x:create and write | a:append to the EOF| b: binary | t: txt | +: disk file for read & write

# Open function to open the file at same or different directory
# file = open("MyFile.txt", "mode") or file = open(r"D:\Text\MyFile2.txt", "mode")

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

file1 = open("myfile.txt", "w")
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes

file1 = open("myfile.txt", "r+")
print("Output of Read function is: ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth bite from the beginning.
file1.seek(0)
print("Output of Readline function is: ")
print(file1.readline())
print()

file1.seek(0)
# To show difference between read and readline
print("#Output of Read(9) function is: ")
print(file1.read(9))
print()

file1.seek(0)
print("##Output of Readline(9) function is ")
print(file1.readline(9))

file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()
