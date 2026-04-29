"""
    Create a program that:
    1. reads two numbers.
    2. read an operator. (+, -, *, /, **) [show ]
    3. show the result as `Operand1 Operator Operand2 = Result`
"""

print("\tC A L C U L A T O R\n", "="*35)

"""
    operands = input("Type 2 numbers: ").split(sep=" ")
    print("'+': Addition",
      "'-': Subtraction",
      "'*': Product",
      "'/': Division",
      "'**': power")
    operator = input("Type the operator: ")

    result = None
    if operator == '+':
        result = float(operands[0]) + float(operands[1])
    elif operator == '-':
        result = float(operands[0]) - float(operands[1])
    print(f"{operands[0]} {operator} {operands[1]} = {result}")
""" 

""" 4 LINES VERSION """

print("'+': Addition",
      "'-': Subtraction",
      "'*': Product",
      "'/': Division",
      "'**': power")
expression = input("Type the arithmetic expression: ")
result = eval(expression)
print(f"{expression} = {result}")

""" 3 LINES VERSION """


""" 2 LINES VERSION """

