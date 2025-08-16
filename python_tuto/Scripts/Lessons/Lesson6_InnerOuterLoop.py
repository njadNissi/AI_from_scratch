"""
    Outer Loop
    Inner Loop
"""


M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

N = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

# Index-wise for loop
for i in range(3):
    print(M[i])

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
