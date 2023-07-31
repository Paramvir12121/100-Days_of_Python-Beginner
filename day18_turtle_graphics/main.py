from turtle import Turtle, Screen


timmy_the_turtle = Turtle()

screen = Screen()

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        timmy_the_turtle.color(c)
        timmy_the_turtle.forward(steps)
        timmy_the_turtle.right(30)





screen.exitonclick()