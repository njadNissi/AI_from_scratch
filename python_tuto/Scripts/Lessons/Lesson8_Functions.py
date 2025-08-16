""" 
    Functions
"""
import math
import random


def find_delta(a:float, b:float, c:float)->float:
    """
        this is the function to compute the delta
        with equation: delta = b^2 - 4ac
    """
    # delta = b^2 - 4ac
    delta = b ** 2 -  4 * a * c
    return delta

    
def find_roots(delta, b):
    """
        ths is the function to compute the two roots
        of a second-degree equation, based on delta and b.
    """
    # x1 = (-b + Vdelta)/2a
    x1 = (-b + math.sqrt(delta)) / 2 * a

    # x2 = (-b - Vdelta)/2a
    x2 = (-b - math.sqrt(delta)) / 2 * a

    return (x1, x2)


def read_equation():
    """this functions reads user input"""
    abc = input("a,b,c = ").split(",") # list of 3 string values
    abc = [float(e) for e in abc]
    a, b, c = abc # unpacking

    # DEVOIR: Dynamiser cette equation
    print(f"{a}x^2 + {b}x + {c} = 0")

    return a, b, c



print("Second degree Equation\n==========================")

a, b, c = read_equation()

# delta = find_delta(a=a, c=c, b=b)
delta = find_delta(a, b, c)

x1, x2 = find_roots(delta=delta, b=b)

if delta < 0:
    print("There is no solution because delta < 0.")
elif delta == 0:
    print("x1 = x2 because delta=0.")

print(f"delta = {delta}, x1 = {x1}, x2 = {x2}")
