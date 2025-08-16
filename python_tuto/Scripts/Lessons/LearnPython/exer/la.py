import numpy as np

m = [
    [1, 2, 3],
    [5, -1, 0]
]


try:
    print('det = ', np.linalg.det(m))
except:
    print('no det available for non-square matrices!!!')

# print(np.linalg.inv(m))
