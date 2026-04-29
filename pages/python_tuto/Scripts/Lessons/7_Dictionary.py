"""
   Dictionary 
"""

symbols = ["H", "He", "Li", "B", "Be", "C", "N", "O", "F", "Ne"]
atomic_num = [i for i in range(1, 10+1, 1)]

print("Chemistry Dictionary\n=====================\n")
print(symbols)

s = input("Type the element symbol: ")

# Method 1
index = symbols.index(s)
print(f"Method1: Z = {atomic_num[index]}")

# dictionary creation: {key: value}
elements = {
    "H":1,
    "He":2,
    "Li":3,
    "B":4,
    "Be":5,
    "C": 6,
    "N":7,
    "O":8,
    "F":9,
    "Ne":10
}
print(f"Symbols: {elements.keys()}")
print(f"Atomic: {elements.values()}")
print(f"Method2: Z = {elements.get(s)}")

