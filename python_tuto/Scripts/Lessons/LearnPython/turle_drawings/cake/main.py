# Layer Cake Challenge - www.101computing.net/layer-cake/
from turtle import *
from shapes import *

myPen = Turtle()
myPen.shape("turtle")
myPen.tracer(0)
myPen.speed(0)
myPen.hideturtle() 
window = turtle.Screen()
window.bgcolor("#69D9FF")
y = -140

#Inititalise the dictionary
ingredients = {}
#Add items to the dictionary
ingredients["vanilla"]="#f3e5ab"
ingredients["pistachio"]="#7DFA7F"
ingredients["raspberry"]="#e30b5d"
ingredients["strawberry"]="#FF0D0D"
ingredients["cherry"]="#C20067"
ingredients["apricot"]="#FFB300"
ingredients["lemon"]="#FFFA5C"
ingredients["kiwi"]="#67F55F"
ingredients["pineapple"]="#FFFF17"
ingredients["mango"]="#FFE838"
ingredients["mint"]="#5FF5A0"
ingredients["white chocolate"]="#FFFDC4"
ingredients["milk chocolate"]="#BF671F"
ingredients["dark chocolate"]="#2A1506"
ingredients["coffee"]="#d2691e"
ingredients["toffee"]="#E35209"
ingredients["mocha"]="#93c572"
ingredients["icing sugar"]="#FFFFFF"

#Initialise the list of layers
layers = []
#Add values to the list
layers.append(["raspberry",30])
layers.append(["dark chocolate",20])
layers.append(["milk chocolate",40])
layers.append(["mango",60])
#Add more layers...


#Preview the content of the list
print(layers)
### Now let's preview the layer cake

#let's draw the plate
draw_rectangle(turtle, "white", -150, y-10, +300, 10)


#Iterate through each layer of the list
for layer in layers:
  draw_rectangle(myPen, ingredients[layer[0]], -120, y, 240, layer[1])
  y+=layer[1]

addIcing(myPen, ingredients["icing sugar"],y)
addCherry(myPen, ingredients["cherry"], 0, y+10, 15)

myPen.getscreen().update()

