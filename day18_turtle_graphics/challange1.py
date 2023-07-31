from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

color_array = ['blue','red','yellow','cadelblue','aquamarine','darkorange','lawngreen','maroon1','purple4','seagreen']

#challange 1
#draw a square

# for _ in range(0,4):
#     turtle.forward(100)
#     turtle.right(90)

# #challange 2
# #dassed line
# turtle.penup()
# turtle.backward(200)
# turtle.pendown()
# for _ in range(20):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()


#challange 3
#shapes
turtle.penup()
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(50)
turtle.left(180)
turtle.pendown()
for side in range (3,10):
    angle = 360/side
    turtle.color(random.choice(color_array))
    for _ in range(side):
        turtle.forward(100)
        turtle.right(angle)





screen.exitonclick()

