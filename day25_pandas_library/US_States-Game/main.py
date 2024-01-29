import turtle
import pandas

screen = turtle.Screen()
pen = turtle.Turtle()
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


# Code to get coordinates on the screen where mouse clicks
# def get_mouse_click_color(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_color)
# turtle.mainloop()

# pandas variable objects
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

print(states)
state_found = []

end_toggle = False

while end_toggle == False:
    answer_state = screen.textinput(title="Guess the State", prompt="What's Another State")
    print(answer_state)
    if answer_state == 'end':
        end_toggle = True
    elif answer_state in data["state"].values:
        state_found.append(answer_state)
        try:
            states.remove(answer_state)
        except:
            pass
        x_value = data[data['state'] == answer_state]['x'].iloc[0]
        y_value = data[data['state'] == answer_state]['y'].iloc[0]
        print(f"State: {answer_state}, X: {x_value}, Y: {y_value}")
        pen.penup()  # to ensure it doesn't draw a line while moving
        pen.goto(x_value, y_value)  # replace x and y with your desired coordinates

        # Write text at the current position
        pen.write(answer_state, align="left", font=("Arial", 8, "normal"))

    else:
        if answer_state in states:
            print("State already found!")
        else:
            print("No state with this name") 


    

screen.exitonclick()