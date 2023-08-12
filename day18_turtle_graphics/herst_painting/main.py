from turtle import Turtle, Screen
import random
import turtle

t = Turtle()
screen = Screen()
# t.speed(0)
t.width(10)
color_list = [ (58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]

for _ in range(0,10):
    t.forward(0)
    t.penup()
    t.forward(20)
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