# question 1
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
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

# question 11 || a = 1, 2 ==> a = (1, 2)
colors = ["red", "green", "blue", "yellow", "purple"]
# last_2_elements = colors[-1], colors[-2] # (colors[-1], colors[-2])
"""
    abc[a:b] => elements from index a to index b-1
    abc[:] => all elements or all the indices. 
    abc[:b] => all elements from the beginning to index b-1, 
    abc[a:] => all elements from index a to the end  
"""
last_2_elements = colors[-2:] 
print(last_2_elements)

# question 12
letters = ["a", "b", "c", "d", "e", "f"]
element_from = letters[2:]
print(element_from)

# question 13
letters = ["a", "b", "c", "d", "e", "f"]
element_start_index4 = letters[:4] # 
print(element_start_index4)

# question 14
fruits = ["banana","cherry","date","elderberry"]
sliced_fruits = (fruits[:])
print(sliced_fruits)

# question 15
"""
    a = (1, 2, 3) => sum_a = sum(a) => sum_a = 6
"""
grades = (85, 92, 78, 90, 88)
first_3_average = sum(grades[:3]) / 3
print(first_3_average)

# question 16
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
print(days[2])

# question 17
days = days[1],days[2],days[3]    # Method 1
print(days)
days = days[1:4]      # Method 2
print(days)


# question 18
empty_list = []
print(f"{empty_list} is mutable.")

empty_list = ()
print(f"{empty_list} is immutable.")

# question 19
list_nums = [5,10,15,20]
print(list_nums[-2])

# question 20
list_nums = [5,10,15,20]
nums = list_nums[::2]
print(nums)


# question 21
define_cars = ["Toyota", "Honda", "Ford", "BMW", "Mercedes"]
reverse_list = define_cars [::-1] 
print(reverse_list)

# question 22
cars = ['Mercedes', 'BMW', 'Ford', 'Honda', 'Toyota']
reverse_list = cars [::-1]
print(reverse_list)

# question 23
define_digits = (1,2,3,4,5,6,7,8,9)
reverse = define_digits [::-1]
print(reverse)

# question 24
list_prices = [19.99, 29.99, 9.99, 49.99]
get_elements = list_prices [::2]
print(get_elements)

# question 25
list_prices = [19.99, 29.99,14.99,49.99]
print(list_prices)

# question 26
define_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
other_name = define_names [1:5]
print(other_name)

# question 27
names = define_names [::-1]
print(names)

# question 28
tuple_coordinates = (100, 200, 300, 400)
xy = tuple_coordinates[0], tuple_coordinates[1]
print(xy)

# question 29
shopping_list = ["milk", "eggs", "bread", "butter", "cheese"]
reserve_order = shopping_list [::-1]
print(reserve_order)

# question 30
shopping_list 

# question 31                                       # inalterable
list_scores = [75, 80, 85, 90, 95]
   

                                    
# question 32
define_text = ["p", "y", "t", "h", "o", "n"]
extract = define_text [0:2]
print(extract)

# question 33
define_texts = define_text [::-1]
print(define_texts)
rev_list = ['n', 'o', 'h', 't', 'y', 'p']
indice_2 = rev_list [2]
print(indice_2)


# question 34
months = ("Jan", "Feb", "Mar", "Apr", "May")
revo = months [::-1]
print(revo)

# question 35
numbers_listo = [1,2,3,4,5,6,7,8,9,10]

# question 36

# question 37

# question 38

# question 39

# question 40





