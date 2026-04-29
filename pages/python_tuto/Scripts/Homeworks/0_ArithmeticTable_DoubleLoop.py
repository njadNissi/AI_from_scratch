print("====== TABLE D'ADDITION 12 x 12 ======\n")

SIZE = 10

# Column header
print("\t", end="")
for i in range(1, SIZE+1, 1):
    print(f"{i:>5}", end="")
print("\n" + "-" * 6 * SIZE)

# Lignes de la table: 12x12 Addition
for i in range(1, SIZE+1, 1): # ROW {i = 1, 2, ..., 12} | outer loop
    print(f"{i:>2} |\t", end="") # rows header

    for j in range(1, SIZE+1, 1): # COL {j = 1, 2, ..., 12} | inner loop
        print(f"{i + j:>5}", end="")

    print()

print("\n" + "-" * 6 * SIZE)




"""
Homework:
    1. Read indefinetly from the keyboard:
        - Table size (e.g., 12 for a 12x12 table)
        - Operation type (e.g., addition, multiplication, etc.)
    2. Generate and print the corresponding arithmetic table based on the user input.

    3. Create a program that receives a decimal number from the user amd convers it
    to fraction. (e.g., 0.75 => 3/4, 0.5 => 1/2, etc.)
"""