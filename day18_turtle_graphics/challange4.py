from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

t = Turtle()
screen = Screen()

# color_array = ['blue','red','yellow','aquamarine','darkorange','lawngreen','maroon1','purple4','seagreen']
angle_array = [0,90,180,270]

t.ht()
t.speed(0)
t.width(15)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

for _ in range(400):
    t.left(random.choice(angle_array))
    t.color(random_color())
    t.forward(30)





screen.exitonclick()