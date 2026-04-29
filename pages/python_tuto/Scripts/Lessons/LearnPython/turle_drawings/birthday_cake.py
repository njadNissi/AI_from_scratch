import turtle as t
import math as m
import random as r


t.bgcolor("#d3dae8")

def drawX(a, i):
    angle = m.radians(i)
    return a * m.cos(angle)


def drawY(b, i):
    angle = m.radians(i)
    return b * m.sin(angle)


for i in range(50):
    t.pu()
    x = r.randint(-500, 500)
    y = r.randint(120, 300)

    t.goto(x, y)
    t.pd()
    t.dot(r.randint(3, 5), t.color(r.randint(0, 7)))
    t.seth(90)
    t.pu()
    t.goto(0, 0)
    t.fd(90)
    t.left(90)
    t.fd(170)
    t.pd()

    t.write("Happy Birthday", font=("Curlz MT", 5))
    t.done()
