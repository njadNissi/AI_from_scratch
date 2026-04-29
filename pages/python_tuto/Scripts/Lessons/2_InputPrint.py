"""
    This program is created in Nanjing, China.
    On 4th August 2025. It explains User Input.
"""

phone = "123-456-789"
parts = phone.split(sep="-")
print(type(parts))

print('Returning Student Registration Form')
# print('===================================')
print('='*43) # str concatenation

print("I. Full Name\n------------")
## input: (1) Print the question. (2) Read the keyboard.
fullname = input('First,Last: ').split(sep=',')
# first, last = fullname.split(sep=',')
# first_last = fullname.split(sep=',')

print("II. Grade/Class\n-------------------")
grades = ('freshman', 'sophomore', 'junior', 'senior')
for i in range(len(grades)):
    print(f'\t{i+1} -> {grades[i]}')
grade = int(input('Type your grade [1-4]: '))


print("III. Phone Number\n-------------------")
phone = input("Type your phone number: ")

print("Resume:\n=============")
# print(f"your full name is {fullname}, your grade is {grade}, and your phone number is {phone}.")
print(f"your first name is {fullname[0]}",
      f"\nyour last name is {fullname[1]}",
      f"\nyour grade is {grades[grade - 1]}",
      f"\nand your phone number is {phone}.")