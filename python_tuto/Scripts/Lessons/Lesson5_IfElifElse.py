"""
    Conditional Statement:
        - If
        - If-else
        - If-elif-else
        - inline If-else
"""

print("\tAge Checker\n", "="*25)

## Version FOR-loop
for _ in range(10000):

    age = int(input("Type your age: "))

    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")


## Version While-loop
while True:

    age = int(input("Type your age: "))

    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")