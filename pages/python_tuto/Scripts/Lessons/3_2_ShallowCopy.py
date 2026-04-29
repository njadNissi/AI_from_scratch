"""
    In Python, there are three core "copy-like" operations: assignment (no real copy), shallow copy, and deep copy.
    The key differences lie in whether a new object is created and whether nested sub-objects are copied recursively.
    Below is a detailed breakdown with examples:
    2. Shallow Copy
    What it is:
    A shallow copy creates a new top-level container object, but the nested sub-objects (e.g., inner lists/dictionaries)
    still reference the original's sub-objects. Only the "outer shell" is new—inner elements are shared.
"""
import copy

original = [1, 2, [3, 4]]
# Shallow copy
shallow_copy = copy.copy(original)  # Equivalent to original[:] or original.copy()
# shallow_copied = original[:]
# shallow_copy = original.copy()


# Modify top-level element of original (immutable int)
original[0] = 99
print("Original:", original)       # [99, 2, [3, 4]]
print("Shallow Copy:", shallow_copy, end="\n\n")  # [1, 2, [3, 4]] (top-level is independent)

# Modify nested sub-object (mutable list)
original[2][0] = 88
print("Original:", original)       # [99, 2, [88, 4]]
print("Shallow Copy:", shallow_copy)  # [1, 2, [88, 4]] (nested elements shared)




# ----

