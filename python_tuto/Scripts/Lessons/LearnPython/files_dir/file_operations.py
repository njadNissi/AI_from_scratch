import shutil
import os

frompath = "C:/Users/njad/Documents/file1.txt"
topath = "C:/Users/njad/Documents/file2.txt"


def copy1():
    if os.path.exists(frompath):
        print('the found found')
    try:
        shutil.copyfile(frompath, 'C:/Users/njad/Documents/file2.txt')
        # use 'r' before the filename is to avoid string formating with '\n, \t, ...'
        shutil.copyfile(frompath, r'C:\Users\njad\Documents\file2.txt')
    except:
        print('There was a problem')


#
def copy2():
    if os.path.exists(frompath):
        print('the found found')
    try:
        os.popen('copy ' + frompath + ' r' + topath)
    except:
        print('There was a problem')


copy2()
