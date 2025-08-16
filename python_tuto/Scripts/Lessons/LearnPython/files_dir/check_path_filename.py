import shutil
import os

fileName1 = r"C:\Users\njad\Documents\file1.txt"
fileName2 = "C:\Users\njad\Documents\file2.txt"
directoryName = 'D://somedir/'

if os.path.exists(fileName1) and os.path.exists(directoryName):
    print('The file exists')
    shutil.copyfile(fileName1, fileName2)
    print('File copied')
else:
    print('File does not exist')
