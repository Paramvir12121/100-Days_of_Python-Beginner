import turtle
import pandas

screen = turtle.Screen()
pen = turtle.Turtle()
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


# Code to get coordintes on the screen where mouse clickes
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# pandas varible objects
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
        x_value = data[data['state'] == answer_state]['x'].iloc[0]
        y_value = data[data['state'] == answer_state]['y'].iloc[0]
        print(f"State: {answer_state}, X: {x_value}, Y: {y_value}")
    else:
        print("wrong input")
    





screen.exitonclick()