# 7 steps to creating a snake game
# #1 Creating a Snake body
# #2 Moving Said body
# #3 Controlling the snake with keyboard
# #4 Detect collision with food
# #5 Creating a scoreboard
# #6 Detect collision with wall
# #7 Adding a delay to the snake

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

#1 Snake Body
segments = []
starting_pos = [(0,0),(-20,0),(-40,0)]

for i in range(3):
    new_snake_square = Turtle(shape="square")
    new_snake_square.color("white")
    new_snake_square.penup()
    new_snake_square.goto(starting_pos[i])
    segments.append(new_snake_square)



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    for seg_num in range(len(segments) -1, 0,-1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)
    segments[0].left(90)
    






screen.exitonclick()
