import pandas

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

print(states)

state_found = []

end_toggle = False

while end_toggle == False:
    answer_state = input("Guess the State: ")
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