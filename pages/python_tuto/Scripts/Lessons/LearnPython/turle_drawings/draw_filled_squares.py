
# draw color-filled square in turtle 
  
import turtle 
  
# creating turtle pen 
t = turtle.Turtle() 
  
# taking input for the side of the square 
s = int(input("Enter the length of the side of the square: ")) 
  
# taking the input for the color 
col = input("Enter the color name or hex value of color(#RRGGBB): ") 
  
# set the fillcolor 
t.fillcolor(col) 
  
# start the filling color 
t.begin_fill() 
  
# drawing the square of side s 
for _ in range(4): 
  t.forward(s) 
  t.right(90) 
  
# ending the filling of the color 
t.end_fill() 

t.screen.mainloop()