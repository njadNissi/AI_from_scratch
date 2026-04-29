import os

filepath = "C:/Users/njad/Documents/"
os.mkdir(filepath + 'hello')
os.mkdir(filepath + 'newdir')
os.mkdir(filepath + 'somedir')
os.rmdir(filepath + 'newdir')
