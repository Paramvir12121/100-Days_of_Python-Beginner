from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()

color_array = ['blue','red','yellow','aquamarine','darkorange','lawngreen','maroon1','purple4','seagreen']
angle_array = [0,90,180,270]

t.ht()
t.width(6)

for _ in range(100):
    t.left(random.choice(angle_array))
    t.color(random.choice(color_array))
    t.forward(40)





screen.exitonclick()