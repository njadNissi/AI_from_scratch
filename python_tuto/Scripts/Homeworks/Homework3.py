"""
    Symbol printing:
        - Upwards triangle
        *
        **
        ***
        ****
        - Downwards triangle
"""

height = int(input("Enter the height of the triangle: "))

print("Upward triangle:")
for i in range(1, height+1, 1):
    print('*' * i)


print("Downward triangle:")
for i in range(height, 0, -1):
    print('*' * i)