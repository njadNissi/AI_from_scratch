import numpy as np

A = [[1,2], [3,4]]
A = np.array(A)
B = np.array([[0, -1], [-2, 5]])
size = A.shape
sum = A + B
sub = A - B
prod = A * B
div = A / B
trans =  A.T # np.transpose(A)
inv = np.invert(A) # A.I

D = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ])
d21 = D[2, 1]
cols13 = D[:,[1,3]]
rows12 = D[[1,2], :]
exp1 = D[D[:,0]>5, :] # all elements from rows of wich the col 0 that is > 5
exp2 = D[D[:,0]>5, [2,3]] # all elements from 2,3 cols of which the col 0 > 5

TF = [True, False, False, True]
dt1 = D[TF,:]
dt2 = D[TF, [2,3]]


X = [[1, 2], [3, 4]]
Y = [[5, 6], [7, 8]]
H = np.hstack((X, Y))
V = np.vstack((X, Y))
np.save('Vstack', V)
np.save('Hstack', H)
newV = np.load('Vstack.npy')


m1 = np.mat("1 2 3; 4 5 6; 7 8 9")
m2 = np.matrix([[1, 2, 3], [5, 6, 7], [9, 10, 11]])


arr1 = np.eye(3)
arr2 = 3 * arr1
mat = np.bmat("arr1 arr2; arr1 arr2")
newMat = np.mat(np.arange(7).reshape(2, 2))


a = 0




