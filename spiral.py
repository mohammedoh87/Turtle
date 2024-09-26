import turtle
turtle.Screen().bgcolor("aqua")

spiral = turtle.Turtle()
size = 0

while True:
    for i in range(4):
        spiral.forward(size + 1)
        spiral.left(90)
        size -= 5

    size += 1

turtle.done()    
