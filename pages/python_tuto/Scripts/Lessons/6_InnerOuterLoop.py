"""
    Outer Loop
    Inner Loop
"""
# 2D list (list of lists): 3x3 matrix
M = [
    [1, 2, 3], # row 0 ==> i == 0
    [4, 5, 6], # row 1 ==> i == 1
    [7, 8, 9]  # row 2 ==> i == 2
]

# 2D list (list of lists): 3x3 matrix
N = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

# Index-wise for loop
m_len = len(N) # number of rows
for i in range(m_len):
    print(N[i]) # access row with N[i]


rows_num = len(M)
cols_num = len(M[0])
# Outer-loop
for i in range(rows_num): # row-wise traversal
    # access row with M[i]
    row = ""
    # Inner-loop
    for j in range(cols_num): # column-wise traversal
        # access an item with M[i][j]
        row += f"{M[i][j]} "
    print(row)
