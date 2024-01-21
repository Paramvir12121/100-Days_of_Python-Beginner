import pandas

data = pandas.read_csv("squirrel_data.csv")

color_list = data["Primary Fur Color"].unique()

gray_coat_squirel = len(data[data["Primary Fur Color"]== "Gray"])
cinnamon_coat_squirel = len(data[data["Primary Fur Color"]== "Cinnamon"])
black_coat_squirel = len(data[data["Primary Fur Color"]== "Black"])

print(gray_coat_squirel,"\n",cinnamon_coat_squirel,"\n",black_coat_squirel)
data_dict = {
    "Fur Color": ["Gray", "Cinnamon","Black"],
    "Squirrel Count": [gray_coat_squirel,cinnamon_coat_squirel,black_coat_squirel]
}

df = pandas.DataFrame(data_dict)

print(df)

df.to_csv("squirrel_by_color")