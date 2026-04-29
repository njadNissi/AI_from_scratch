"""
    y = f(x)        z = f(x, y)         h = f(x, y, z)
    y = 2x+3        z = 2x+3y           h = 2x+3y+4z
"""
# ex1
def Print(text):  # text => parameter
    print(f"==> {text} <==")
    
Print("Hello World") # "Hello World" => argument 
Print(text="Python is great")
Print(text=50) # text can be of any type, not just string

# ex2
def PrintAge(age:int):
    if type(age) != int: # != means "not equal to", == means "equal to"
        print("Error: age must be an integer.")
        return
    print(f"Age is {age}")

PrintAge(age=25)
PrintAge(age=12.25) # age can be passed as a positional argument without naming it.


# ex3
def PrintInfo(name:str, age:int, city:str):
    print(f"{name} is {age} years old and lives in {city}.")

    
PrintInfo(name="Alice", age=30, city="New York")
PrintInfo(name="Alice", city="New York", age=30)
PrintInfo("Bob", 25, "Los Angeles") # positional arguments without naming them.
PrintInfo("Bob", "Los Angeles", 25) # positional arguments without naming them.


# ex4
def GreetMe(name:str="Guest"):
    print(f"Hello, {name}!")

GreetMe() # uses default value "Guest"
GreetMe(name="Alice") # overrides default value with "Alice"


# ex5
def Power(base:float, exponent:float):
    return base ** exponent

p1 = Power(base=2, exponent=3) # returns 8
p1 = Power(2, 3) # positional arguments without naming them, also returns 8
print(f"2^3 = {p1}")

p2 = Power(3, -1)
print(f"3^-1 = {p2}")


# ex6
import math

def CircleArea(radius:float)->float:
    area = 2 * math.pi * radius
    return area

r = 5
area = CircleArea(radius=r)
print(f"Area of circle with radius {r} is {area:.2f} \nwith π={math.pi}")



# ex7
import time

def ArithTable(size:int, operation:str, delay:float=0.1):
    # Force valid operations (add French aliases for usability)
    valid_ops = {"addition", "multiplication", "add", "mult"}
    if operation.lower() not in valid_ops:
        print(f"Erreur: Opération '{operation}' non valide. Utilisez 'addition' ou 'multiplication'.")
        return

    # Standardize operation name
    op = "addition" if operation.lower() in ["addition", "add"] else "multiplication"
    
    print(f"\n\n====== TABLE D'{op.upper()} {size} x {size} ======\n")

    # Column header (element-by-element printing)
    print("\t", end="", flush=True)  # flush=True = force immediate print
    for i in range(1, size+1):
        print(f"{i:>5}", end="", flush=True)  # Flush after each column number
        time.sleep(delay)  # Pause AFTER printing the element
    print("\n" + "-" * 6 * size)  # Newline for rows

    # Rows (element-by-element: each cell prints with delay)
    for i in range(1, size+1):
        # Print row header (immediate, no delay)
        print(f"{i:>2} |\t", end="", flush=True)
        
        # Inner loop: print each cell with delay
        for j in range(1, size+1):
            # Calculate result
            if op == "addition":
                result = i + j
            else:  # multiplication
                result = i * j
            
            # Print cell + flush + delay (critical for element-by-element)
            print(f"{result:>5}", end="", flush=True)
            time.sleep(delay)  # Pause AFTER printing the cell
        
        # Newline after row is complete
        print()

    print("\n" + "-" * 6 * size)


# ArithTable(size=12, operation="addition", delay=0.1)



# ex8
def array_add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

    
sum = array_add(4, 6, -1, 9, 30)
print(sum)



# ex9 | 3. Inner function: possible in python, JS, go
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