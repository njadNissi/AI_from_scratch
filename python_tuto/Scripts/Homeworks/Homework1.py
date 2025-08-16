print("====== TABLE D'ADDITION 12 x 12 ======\n")

# En-tête
print("\t", end="")
for i in range(1, 13):
    print(f"{i:>4}", end="")
print("\n" + "-" * 57)

# Lignes de la table
for i in range(1, 13):
    print(f"{i:>2} |\t", end="")
    for j in range(1, 13):
        print(f"{i + j:>4}", end="")
    print()
