# run.py
import ctypes
import os
import sys

# --- 1. Find the compiled library file ---
# Determine extension based on OS
if sys.platform.startswith('win'):
    lib_name = "mylib.dll"
else:
    # Linux/macOS typically use .so
    lib_name = "./mylib.so"

# Get absolute path to ensure Python finds it
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), lib_name))

print(f"Python: Attempting to load library: {lib_path}")

if not os.path.exists(lib_path):
    print("\nERROR: Compiled library not found!")
    print("Did you run the compilation step in the README?")
    sys.exit(1)

# --- 2. Load the library ---
try:
    # CDLL is used for standard C calling convention
    cpp_lib = ctypes.CDLL(lib_path)
    print("Python: Library loaded successfully.")
except OSError as e:
    print(f"ERROR: Could not load library. {e}")
    sys.exit(1)


# --- 3. Define argument and return types (VERY IMPORTANT) ---
# The C++ signature is: int add_numbers_cpp(int a, int b)

# Define inputs: a list of ctypes representing the arguments
cpp_lib.add_numbers_cpp.argtypes = [ctypes.c_int, ctypes.c_int]

# Define output: the ctype representing the return value
cpp_lib.add_numbers_cpp.restype = ctypes.c_int


# --- 4. Call the function ---
num1 = 10
num2 = 55

print(f"\nPython: Calling C++ function with {num1} and {num2}...")

# Perform the call
result = cpp_lib.add_numbers_cpp(num1, num2)

print(f"Python: Result received back from C++: {result}")

assert result == 65
print("\nPython: Verification successful.")