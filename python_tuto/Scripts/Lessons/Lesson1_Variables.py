print('Hello World!') # not Print but print
print("Hello World 2!")

# This car is "blue"/'blue'
print('"Hello World 3!"')
print("'Hello World 3!'")

## Variables Types
## Numbers
a = 4 # int: integer
b = 3.14 # float: floating-point number
c = 1 + 2j # complex
d = -25 # int
l = 9999999999999
e = 1e-5 # 10^-5
h = 2 ** 5 # Exponent: 2^5
save = True # bool: boolean
save = False
equality = a == b # comparaison d'egalite
superiority = a >= b # >=
inferiority = a <= b
truth = bool('True') # truth = True
print(f"{a} == {b}? result={save}")

# '=' : Attribution, '==': equality
# x = type(e);print(x)
print(type(e))
print(a * b - c / d)

## Others
## (1) Je porte une chemise. (2) La chemise est blueue. ==> Je porte une chemise blueue.
s1 = 'Hello' # str: string
s2 = "Hello"
print(type(s1), ", ", type(s2))
# s3 = s1 + ', ' + s2
print(s1 + ', ' + s2)

## Casting: conversion d'un type a un autre
f = 3.1415 # float
g = int(f) # recuperer la partie <int>
h = float(3)
i = bool(0) # 1=True, 0=False
print(f"i={i}")
r = round(f, 2) # limiter les places decimales
a = 18
b = 7
c = a // b # same as: c = int(a / b)
mod = a % b # reste de la division entiere
s = str(45)
print(type(s))

