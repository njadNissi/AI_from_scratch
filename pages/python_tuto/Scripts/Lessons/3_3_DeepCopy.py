"""
    In Python, there are three core "copy-like" operations: assignment (no real copy), shallow copy, and deep copy.
    The key differences lie in whether a new object is created and whether nested sub-objects are copied recursively.
    Below is a detailed breakdown with examples:
    3. Deep Copy
    What it is:
    A deep copy recursively creates new objects for all levels (top-level + all nested sub-objects).
    The copied object is completely independent of the original—no shared data at any level.
"""
import copy

original = [1, 2, [3, 4]]
# Deep copy
deep_copy = copy.deepcopy(original)

# Modify top-level element of original
original[0] = 99
print("Original:", original)     # [99, 2, [3, 4]]
print("Deep Copy:", deep_copy) # [1, 2, [3, 4]] (no impact)

# Modify nested sub-object of original
original[2][0] = 88
print("Original:", original)     # [99, 2, [88, 4]]
print("Deep Copy:", deep_copy) # [1, 2, [3, 4]] (still no impact)