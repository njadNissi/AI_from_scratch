"""
    In Python, there are three core "copy-like" operations: assignment (no real copy), shallow copy, and deep copy.
    The key differences lie in whether a new object is created and whether nested sub-objects are copied recursively.
    Below is a detailed breakdown with examples:
    1. Assignment (No Copy)
    What it is:
    Assignment (=) does not create a new object—it only creates a new variable that references (points to) the same 
    memory address as the original object. The original and "copied" variables are just two labels for the same data.
"""
# Original object (nested list: mutable top-level + mutable sub-object)
original = [1, 2, [3, 4]]
# Assignment (no copy)
assigned = original

# Modify top-level element of original
original[0] = 99 # 1=>99
print("Original:", original)  # [99, 2, [3, 4]]
print("Assigned:", assigned, end="\n\n")  # [99, 2, [3, 4]] (changes reflect immediately)

# Modify nested sub-object of original
original[2][0] = 88 # 3=>88
print("Original:", original)  # [99, 2, [88, 4]]
print("Assigned:", assigned)  # [99, 2, [88, 4]] (nested changes also reflect)