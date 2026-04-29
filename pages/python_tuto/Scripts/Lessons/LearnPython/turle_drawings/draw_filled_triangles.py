
# draw color filled triangle in turtle 
  
import turtle 
  
# creating turtle pen 
t = turtle.Turtle() 
  
# taking input for the side of the triangle 
s = int(input("Enter the length of the side of the triangle: ")) 
  
# taking the input for the color 
col = input("Enter the color name or hex value of color(# RRGGBB): ") 
  
# set the fillcolor 
t.fillcolor(col) 
  
# start the filling color 
t.begin_fill() 
  
# drawing the triangle of side s 
for _ in range(3): 
  t.forward(s) 
  t.right(-120) 
  
# ending the filling of the color 
t.end_fill() 

