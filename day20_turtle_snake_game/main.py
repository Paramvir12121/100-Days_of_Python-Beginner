from turtle import Turtle, Screen
from snake import Snake
import time

# 7 steps to creating a snake game
# #1 Creating a Snake body
# #2 Moving Said body
# #3 Controlling the snake with keyboard
# #4 Detect collision with food
# #5 Creating a scoreboard
# #6 Detect collision with wall
# #7 Adding a delay to the snake

screen = Screen()
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")


snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    


screen.exitonclick()
