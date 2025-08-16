"""
    Functions
"""

# 1. Define a function
def say_hi():
    print("Hi!")


# 2. Call a function
say_hi()

# 3. with a parameter
def speak(speech):
    print(speech)

speak(speech="I am speaking...")

# 4. with multiple parameters
def power(base, exp):
    return base ** exp


r = power(2, 5)
r = power(base=2, exp=5)
r = power(exp=5, base=2)
print(r)

# r = power(base=3, 4) # >>> WILL NOT WORK!!!!
r = power(3, exp=7) # >>>> WILL WORK

# Unknown parameters
# 1. Default argument
def call_me(fname, lastname, midlename=""):
    print(f"{fname} {midlename} {lastname}")

    
call_me(fname="Joao", lastname="Enstein")
call_me(fname="Joao", midlename="Albert", lastname="Enstein")

# 2. Uknown paramters number
def array_add(*args):
    total = 0
    for num in args:
        total += num
    return total

    
sum = array_add(4, 6, -1, 9, 30)
print(sum)


# 3. Inner function
def cook():

    def buy_vegetables():
        print("I am buying vegetables")

    def cook_vegetabes():
        print("I am cooking vegetables")

    def cook_meat():
        print("I am cooking meat")

    # 1. 
    buy_vegetables()
    # 2. 
    cook_vegetabes()
    #3. 
    cook_meat()

    
cook()