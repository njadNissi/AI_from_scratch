# Variable: name = value (type)
age = 25 # integer --> int
age2 = age * 2 # arithmetic operation
height = 5.9 # float
test = True # boolean --> bool  [True:1 / False:0]
name1 = "Alice" # string --> str (text)
name2 = 'Bob'
name3 = """Charlie?"""
name4 = '''Je suis un etudiant.'''
text = name1 * 3  # string repetition
print(text)  # Output: AliceAliceAlice

# = attribution operator: assign value to variable
# == equality operator: compare two values
check_age = age == 30 # False

# OUTPUT
print("hello")
print(123)
print(True)
print(7*4-12)
print('The target is "Python"')


# Keyboard 128 characters: ASCII (1Byte): Alphabet + digits + Symbols
# 8 bits = 1 Byte = 256 values (0-255)
# Unicode string: UTF-8: more characters (multi-Bytes)
# e.g., 'é', 'ç', '漢', '字', emojis, etc.
# 4 bytes = 32 bits = over 4 billion values
print("π")
print("\u03C0")
print(chr(960))


# Demo: chr(int) ---> character from ASCII/Unicode code point
# Demo: ord(char) ---> integer code point from character
print(ord('A'))
print(ord('B'))
print(ord('Z'), end="\n")
# print("\n"*2)
print("\tPARAGRAPH")
# 1. Mathematical Symbols
print("=== Mathematical Symbols ===")
print("π (Pi): \u03C0 or", chr(960))
print("± (Plus-Minus): \u00B1 or", chr(177))
print("√ (Square Root): \u221A or", chr(8730))
print("∞ (Infinity): \u221E or", chr(8734))
print("∑ (Sum): \u2211 or", chr(8721))

# 2. Arrows
print("\n=== Arrows ===")
print("← (Left Arrow): \u2190 or", chr(8592))
print("↑ (Up Arrow): \u2191 or", chr(8593))
print("→ (Right Arrow): \u2192 or", chr(8594))
print("↓ (Down Arrow): \u2193 or", chr(8595))
print("↔ (Left-Right Arrow): \u2194 or", chr(8596))

# 3. Emojis (8-digit Unicode: \U000XXXXXX)
print("\n=== Emojis ===")
print("😊 (Smile): \U0001F60A or", chr(128522))
print("❤️ (Heart): \U0001F493 or", chr(128147))
print("🚀 (Rocket): \U0001F680 or", chr(128640))
print("🍕 (Pizza): \U0001F355 or", chr(127829))

# 4. Special Punctuation/Symbols
print("\n=== Special Punctuation ===")
print("• (Bullet Point): \u2022 or", chr(8226))
print("✓ (Check Mark): \u2713 or", chr(10003))
print("✗ (Cross Mark): \u2717 or", chr(10007))
print("© (Copyright): \u00A9 or", chr(169))
print("® (Registered): \u00AE or", chr(174))


# INPUT: y = f(x)
# user_name = input("What is your name? ")
# print(user_name)


# HOMEWORK
print("\t  *")
print("\t" + "*" * 5)
print("     " + "*" * 11) 
print("   " + "*" * 15) 
print("#" + "=" * 20 + "#")
print("#" + " "*20 + "#")
print("#" + " "*20 + "#")
print("#" + " "*20 + "#")
print("#" + " "*20 + "#")
print("#" + " "*20 + "#")
print("#" + " "*20 + "#")
print("#" + " "*20 + "#")
print("#" + " "*20 + "#")
print("#" + "=" * 20 + "#")