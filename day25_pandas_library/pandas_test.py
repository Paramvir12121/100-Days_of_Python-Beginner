import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()

tempratures = data["temp"].to_list()

total_temp = 0

for temp in tempratures:
    total_temp += temp

avg_temp = total_temp/(len(tempratures))

print(avg_temp)