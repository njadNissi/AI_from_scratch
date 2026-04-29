"""
    Read different mformats of files
"""

## modes : r=read, w:write, a:append, x: create file and write
# with open("files/story.txt", mode="r") as f:
#     text = f.read()
#     print(text)

    
    
# print("Read line by line:")
# with open("files/story.txt", mode="r") as f:
#     lines = f.read().splitlines()
#     for i in range(len(lines)):
#         line = lines[i]
#         print(f"line{i} => {line}")


# with open("files/book.txt", mode='x') as f:
#     text = "This is a book createn with python!"
#     f.write(text)

    
"""
    Apply this technique to Homework 6
"""    

import json

data = open("files/dictionary.json", mode="r")
english_french_dict:dict = json.load(data)

print("="*30)
print("|| English-French Dictionary||")
print("="*30)
while True:
    word = input("English world: ")
    if word in english_french_dict.keys():
        french, gram_class = english_french_dict.get(word)
        print(f"French: {french}\ngramatical class.: {gram_class}")
        print("-+-"*15)
    else:
        print(f"Sorry, '{word}' has not been found!")