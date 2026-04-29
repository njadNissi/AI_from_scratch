
# draw color filled star in turtle 
  
import turtle 
  
# creating turtle pen 
t = turtle.Turtle() 
  
# taking input for the side of the star 
s = int(input("Enter the length of the side of the star: ")) 
  
# taking the input for the color 
col = input("Enter the color name or hex value of color(#RRGGBB): ") 
  
# set the fillcolor 
t.fillcolor(col) 
  
# start the filling color 
t.begin_fill() 
  
# drawing the star of side s 
for _ in range(5): 
  t.forward(s) 
  t.right(144) 
  
# ending the filling of color 
t.end_fill() 

