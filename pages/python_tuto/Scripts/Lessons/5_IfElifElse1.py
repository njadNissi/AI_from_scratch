"""
    Conditional Statement: >> True or False
        - If
        - If-else
        - If-elif-else
        - inline If-else   || inline for loop
"""

# print("\tAge Checker\n", "="*25)

# age = int(input("Type your age: "))

##1 IF-ELSE
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

# -------------------------

"""
    [0-11]: infant
    [12-17]: minor
    [18-29]: adult
    [30-...[: old
"""
##2 IF-ELIF-ELSE
# if age >= 0 and age <=11:
#    print("You're an infant.") 
# elif age >= 12 and age <=17:
#    print("You're a minor.")
# elif age >= 18 and age <=29:
#    print("You're an adult.")
# elif age >= 30:
#    print("You're old.")
# else:
#     print("Please, Enter an age >= 0.")
    

##3 inline IF-ELSE
""" VERSION 6 LINES
    children_num = int(input("How many children you haven? R: "))
    if children_num >= 1:
        parent = True
    else:
        parent = False
    print(f"Parent? R: {parent}")
"""

"""VERSION 3 LINES
    children_num = int(input("How many children you haven? R: "))
    parent = True if children_num >= 1 else False
    print(f"Parent? R: {parent}")
"""

"""VERSION 2 LINES
    children_num = int(input("How many children you haven? R: "))
    print(f"Parent? R: {True if children_num >= 1 else False}")
"""

# print(f"Parent? \
#     R: {True if int(input('How many children you haven? R: ')) >= 1 else False}")

    
## EXAMPLES: INLINE
a = 3

lisa = [1, 2, 3, 4, 5] # list by extension

print("a > 0" if a > 0 else "a < 0")

sign = "a > 0" if a > 0 else "a < 0"
print(f"sign: {sign}")

# inline if-else in list comprehension

listx = [*range(0, 10, 1)]
print(f"listx: {listx}")

listy = [e for e in range(10)]
print(f"listy: {listy}")

listy = [e*-1 for e in range(10)]
print(f"listy: {listy}")

listz = [el for el in range(10) if el/2 > 3]
print(f"listz: {listz}")
""" a % b => remainder of divion of a by b """
x = 5
print("even" if x % 2 == 0 else "odd")


listw = [listx[i] if i%2 == 0 else listy[i] for i in range(len(listx))]
print(f"listw: {listw}")