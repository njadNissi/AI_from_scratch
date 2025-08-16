"""
    Loops : Les boucles
    1. for
    2. while
"""
## f(x, y) => x, y are parameters
## y = f(2, -1) => 2, -1 are arguments
# iteration = tour = etape

# FOR loop (boucle)
for i in range(10): # range(start=0, stop:10, step=1)
    print(i)

#        (start=-5, stop:5, step=2)
for i in range(-5, 5, 5):
    print(i)
    
# Use for loop to traverse a List/Tuple
l = [1, 2, -1, 4, 6, 2, 0, 5, -1, [3, [2, -4], 2]]
print("For loop (index-wise)")
for i in range(10):
    item = l[i]
    print(f"l[{i}] = {item}")


# For loop (item-wise)
print("For loop item-wise")
i = 0
for item in l:
    print(item)
    i -= 2


## While loop
print("While-loop")
MAX = 10
counter = 0
while counter < MAX:
    counter += 1
    print(counter)

while True:
    print("Hello")