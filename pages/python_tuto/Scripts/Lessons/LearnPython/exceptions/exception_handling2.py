

try:
    number = int(input('Input a number: '))
    print('You inputed the number:', number)
except:
    print('You inputed an invalid number format')
finally:  # optional, present for stuctural view
    print('finishing the execution')
print('Program exited safely')
