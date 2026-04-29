
# draw color-filled hexagon in turtle 
  
import turtle 
  
# creating turtle pen 
t = turtle.Turtle() 
  
# taking input for the side of the hexagon 
s = int(input("Enter the length of the side of the hexagon: ")) 
  
# taking the input for the color 
col = input("Enter the color name or hex value of color(# RRGGBB): ") 
  
# set the fillcolor 
t.fillcolor(col) 
  
# start the filling color 
t.begin_fill() 
  
# drawing the hexagon of side s 
for _ in range(6): 
  t.forward(s) 
  t.right(-60) 
  
# ending the filling of the color 
t.end_fill() 

