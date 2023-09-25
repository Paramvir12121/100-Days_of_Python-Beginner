from turtle import Turtle, Screen, home
import random
import turtle


turtle.colormode(255)

t = Turtle()
screen = Screen()
# t.speed(0)

color_list = [ (58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]
t.width(15)
space_bw_dots = 40
length = 10
width = 10
t.penup()
t.home()
t.hideturtle()
for x in range(0,length):
    t.penup()
    t.goto(-200,-200)
    t.left(90)
    t.forward(x*space_bw_dots)
    t.right(90)
    t.pendown()
    for _ in range(0,width):
        t.forward(0)
        t.penup()
        t.forward(space_bw_dots)
        t.color(random.choice(color_list))
        t.pendown()
        t.forward(0)
# painting_length = 100
# painting_width = 100

# t.penup()
# t.goto(-100,-100)
# for i in range(0,10):
#     for j in range(0,10):
#         t.pendown()

    


screen.exitonclick()