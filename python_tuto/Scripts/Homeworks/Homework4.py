import math


print("Second degree Equation\n==========================")

abc = input("a,b,c = ").split(",") # list of 3 string values
abc = [float(e) for e in abc]
a, b, c = abc # unpacking

# DEVOIR: Dynamiser cette equation
print(f"{a}x^2 + {b}x + {c} = 0")


# delta = b^2 - 4ac
delta = b ** 2 -  4 * a * c

if delta < 0:
    print("There is no solution because delta < 0.")

elif delta == 0:
    print("x1 = x2 because delta=0.")

# x1 = (-b + Vdelta)/2a
x1 = (-b + math.sqrt(delta)) / 2 * a

# x2 = (-b - Vdelta)/2a
x2 = (-b - math.sqrt(delta)) / 2 * a

print(f"delta = {delta}, x1 = {x1}, x2 = {x2}")