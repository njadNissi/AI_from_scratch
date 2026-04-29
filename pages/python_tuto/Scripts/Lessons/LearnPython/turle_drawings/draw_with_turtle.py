from turtle import *

numOfFaces = 10
x = 360 / numOfFaces
y = 120

for i in range(numOfFaces):
    if i % 2 == 0:
        color("skyblue")
    else:
        color("pink")
    begin_fill()
    forward(y)
    left(x)
    forward(y)
    left(180-x)
    forward(y)
    left(x)
    forward(y)
    left(180-x)
    end_fill()
    left(x)
done()