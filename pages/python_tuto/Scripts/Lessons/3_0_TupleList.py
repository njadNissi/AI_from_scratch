"""
    DAY 1
    # - formatted String: f"my var is {variable}"
    # - Conversion (casting)
"""

# - Tuple: (), INALTERABLE


## Un point p1(-1, 4, 6); p2=(2, 3, 4); p3=[3, 4, 5]
p1 = (-1, 4, 6) # tuple: un groupe de valeurs inalterables.
p2 = 2, 3, 4 # python complete les parentheses manquantes.
print(f"X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
#    Z, A
C = (6, 12)
print(f"Z={C[0]}, A={C[1]}")
# C[0] = 2 # ERROR!!!
a, b = (1, 2)


# - List: [], ALTERBALE: change item value, add items
Na = [11, 23] # unpacking
print(f"Z={Na[0]}, A={Na[1]}")
Na[0] = 2
print(f"Z={Na[0]}, A={Na[1]}")
Na.append(10) # Add to the end
print(Na)
c, d = [3, 4]


# List Comprehension
"""
    l1 = []
    l2 = []
    for i in range(10):
        l1.append(i)
        l2.append(i*2-5)
"""
l1 = [i for i in range(10)]
l2 = [i*2-5 for i in range(10)]
print(l1)
print(l2)


l3 = ["3", "4", "5"]
l3i = [int(l3[i]) for i in range(len(l3))] # Method 1
l3i = [int(e) for e in l3] # Method 2



# List slicing
second_item = l1[1]
print(f"second item = {second_item}")
first_5_items = l1[:5]
print(f"first 5 items: {first_5_items}")
last_5_items = l1[5:]
print(f"last 5 items: {last_5_items}")
middle_items = l1[2:7]
print(f"middle items: {middle_items}")

# list Unpacking
l = [5, -1]
a, b = l
l = [5, -1, 0, 1, 7]
a, b, _ = l