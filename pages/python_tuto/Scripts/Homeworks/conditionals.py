
age = int(input("Type your age: "))

### IF
if age >= 18:
    print("You are an adult.")

### IF-ELSE
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
    

### IF-ELIF-ELSE
if age < 0:
    print("Error! Age cannot be negative.")
elif age < 18:
    print("You are a minor.")
    if age < 15:
        print("You are a child.")
else:
    print("You are an adult.")

    
"""
Homework: 
    1. Create a program that continuously 
    prompts the user to enter their age until they provide
    a valid input (a number between 1 and 149).
    Use a while loop and conditional statements to validate
    the input and provide appropriate feedback for invalid entries.

    2. Create a program that takes a user's age as input
    and categorizes them into different life stages 
    (e.g., child, teenager, adult, senior)
    based on their age using if-elif-else statements.
    
    3. Create a program that checks if a given number
    is positive, negative, or zero

    4. Create a program that checks if a given year is a leap year or not.
    A leap year is defined as:
        - It is divisible by 4;
        - However, if it is divisible by 100, it must 
        also be divisible by 400 to be a leap year.
        
    5. Create a program that takes a user's input for a password
    and checks if it meets certain criteria:
        - At least 8 characters long
        - Contains both uppercase and lowercase letters
        - Contains at least one digit
        - Contains at least one special character (e.g., !, @, #, etc.)
"""