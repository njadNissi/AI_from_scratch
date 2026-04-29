# question 1
fruits = ["apple", "banana", "cherry", "date", "elderberry"].
print(fruits[0])  # Output: apple

# question 2
print(fruits[-1])  # Output: cherry

# question3 
numbers = (10, 20, 30, 40, 50)
number3 = numbers[2]
print(number3)  # Output: 30


# question 4
print(numbers[-2])

# question 5
colors = ["red", "green", "blue", "yellow", "purple"]
print(colors[1], colors[4]) # method 1
print(f"{colors[1]}, {colors[4]}") # method 2


# question 6
numbers[1] = 25 # This will raise a TypeError because tuples are immutable

# question 7
mixed = [1, "hello", 3.14, True, (6,7)]
print(mixed[3])

# question 8
print(mixed[4]) # methiod  1
print(mixed[-1]) # method 2

# question 9
first_3_fruits = fruits[0:3]
print(first_3_fruits)

# question 10
numbers_1to4 = numbers[0:3+1] # 3 (inclusive) => 3+1 (to include the last element)
print(numbers_1to4)