"""
    Loops : Les boucles
    1. for
    2. while
"""
## f(x, y) => x, y are parameters
## y = f(2, -1) => 2, -1 are arguments
# iteration = tour = etape

# FOR loop (boucle): range(start=0, stop=10, step=1)
# ex1: stop when i < 20
# for i in range(5, 20, 2):
#     print(i)


# ex2: Should always have a stop value, start and step are optional.
# for i in range(10): 
    # print(i)


# ex3: can use negative values: (start=-6, stop:7, step=3)
# for i in range(-6, 7, 3):
#     print(i)
    
l = [1, 2, -1, 4, 6, 2, 0, 5, -1, [3, [2, -4], 2]]

# ex4: Use for loop to traverse a List/Tuple
# print("For loop (index-wise)")
# for i in range(len(l)):
#     item = l[i]
#     print(f"l[{i}] = {item}")


# ex5: For loop (item-wise)
# print("For loop item-wise")
# for item in l:
#     print(item)


# ex6: For loop (item-wise) + indices
# print("For loop item-wise + indices")
# i = 0
# for item in l:
#     print(f"l[{i}] = {item}")
#     i += 1    # i = i + 1

## While loop
# print("While-loop")
# stop = 10    # stop when counter < MAX
# start = 0  # start
# step = 1
# counter = start
# while counter < stop:
#     counter += step
#     print(counter)

### True = 1
# while True:
#     print("Hello")