from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
for x in range(0,4):
    timmy.fd(100)
    timmy.rt(90)
timmy.color("red")
for x in range(0,4):
    timmy.fd(100)
    timmy.lt(90)
timmy.color("black") 
timmy.circle(100)   

my_screen = Screen()

print(my_screen.canvheight)
my_screen.exitonclick()