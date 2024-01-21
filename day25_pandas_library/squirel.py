import pandas

data = pandas.read_csv("squirrel_data.csv")

color_list = data["Primary Fur Color"].unique()

print(color_list)