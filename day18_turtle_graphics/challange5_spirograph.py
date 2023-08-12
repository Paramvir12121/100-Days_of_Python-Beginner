from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

t = Turtle()
screen = Screen()
t.speed(0)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


for angle in range(0,360):
    t.color(random_color())
    t.left(1)
    r = 100
    t.circle(r)






screen.exitonclick()