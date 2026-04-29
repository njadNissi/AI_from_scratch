import turtle

left_angle = int(input('enter angle: '))

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


for i in range(300):
    t.pencolor(colors[i % 6])
    t.circle(i)
    t.left(left_angle)

turtle.done()
