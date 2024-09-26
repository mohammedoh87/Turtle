import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

num_sides = 7
angle = 360.0 / num_sides
side_length = 80

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.left(angle)

turtle.done()

