# This is a custom module we've made.  
# Modules are files full of code that you can import into your programs.
# This one teaches our turtle to draw various shapes.

import turtle
import math

def draw_circle(turtle, color, x, y, radius):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(radius)
  turtle.end_fill()
    
def draw_triangle(turtle, color, x, y, size):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range (3):
    turtle.forward(size)
    turtle.left(120)
  turtle.end_fill()
  turtle.setheading(0)
    
def draw_square(turtle, color, x, y, size):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range (4):
    turtle.forward(size)
    turtle.left(90)
  turtle.end_fill()
  turtle.setheading(0)
  
def draw_rectangle(turtle, color, x, y, width, height):
  turtle.hideturtle()
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range (2):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    
  turtle.end_fill()
  turtle.setheading(0)  
  turtle.getscreen().update()
  
def draw_star(turtle, color, x, y, size):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.right(144)
  for i in range(5):
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
  turtle.end_fill()
  turtle.setheading(0)
  turtle.getscreen().update()


def addCherry(turtle,color,x,y,radius):
  draw_circle(turtle, color, x, y, radius)  
  turtle.getscreen().update()
  
def addIcing(turtle,color,y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(-125,y+10)
  turtle.pendown()
  turtle.begin_fill()

  for x in range(-125,125):
    turtle.goto(x,y-10-10*math.cos((x/100)*2*math.pi))
  
  turtle.goto(125,y+10)
  turtle.goto(-125,y+10)
  turtle.end_fill()
  turtle.getscreen().update()
  
