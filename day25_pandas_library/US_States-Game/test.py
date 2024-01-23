import pandas

data = pandas.read_csv("50_states.csv")

for state in data["state"]:
    print(state)