import shutil
import os

cur_dir = os.path.dirname(__file__)
fileName1 = f"{cur_dir}/file1.txt"
fileName2 = f"{cur_dir}/file2.txt"
directoryName = f"{cur_dir}/files_dir/"

if os.path.exists(fileName1) and os.path.exists(directoryName):
    print('The file exists')
    shutil.copyfile(fileName1, fileName2)
    print('File copied')
else:
    print('File does not exist')
