"""
    This scripts calculates the determinant
    of a square matrix.
    M = np.array(l)
    detM = np.floor(np.linalg.det(M))
    print(f"determinant = {detM}")
"""

import numpy as np

def print_matrix(M):
    for i in range(len(M)):
        row = ""
        for j in range(len(M[0])):
            row += f"\t{M[i][j]}"
        print(row)
    

def get_matrix_shape(matrix:list[list]):
    rows = len(matrix)
    cols = len(matrix[0])
    return rows, cols

    
def is_matrix_square(M):
    rows, cols = get_matrix_shape(M)
    return rows == cols

    
def get_helper_row(M:list[list], elim_col:int):
    helper_row = M[elim_col]
    return helper_row


def helper_row_coef(helper_row:list, row:list, elim_col:int):
    a = helper_row[elim_col]
    b = row[elim_col]
    x = -b / a
    return x
    

def mult_row(row, coef):
    return [coef * e for e in row]


def add_rows(row1, row2):
    sum_row = [e1+e2 for e1, e2 in zip(row1, row2)]
    return sum_row


def get_main_diagonal(M, rows:int):
    md = [M[x][x] for x in range(rows)]
    return md
    

def multiply_main_diagonal(md:list, rows:int):
    total = 1
    for i in range(rows):
        total *= md[i]
    return total
    
    
def compute_determinant(M):
    rows, cols = get_matrix_shape(l)
    for i in range(1, rows, 1): # traverse row by row
        for j in range(i): # traverse col by col
            hrow:list = get_helper_row(M, elim_col=j)
            row = M[i]
            coef:float = helper_row_coef(row=row, helper_row=hrow, elim_col=j)
            hrow:list = mult_row(hrow, coef)
            new_row = add_rows(hrow, row)
            M[i] = new_row
            print(f"e{i+1}{j+1} ==> coef.: {coef} ==> hrow:r{j+1} {hrow}")

            print_matrix(M)
            print("=============================")
    
    md = get_main_diagonal(M, rows)
    det = multiply_main_diagonal(md, rows)

    return det


# ----------------------------------------------
l = [
    [1, 2, 3],
    [2, 2, 1],
    [5, 2, 7]
]
print_matrix(M=l)


square = is_matrix_square(l)
if not square:
    print("The determinant does not exist!")
else:
    det = compute_determinant(M=l)
    print(f"Determinant = {det}")