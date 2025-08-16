"""
    Conditional Statement: >> True or False
        - If
        - If-else
        - If-elif-else
        - inline If-else
"""

print("\tAge Checker\n", "="*25)

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

print(f"Parent? \
    R: {True if int(input('How many children you haven? R: ')) >= 1 else False}")