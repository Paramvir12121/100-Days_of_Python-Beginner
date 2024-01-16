import pandas

data = pandas.read_csv("weather_data.csv")

temp_list = data["temp"].to_list()

print(temp_list)

total_val = 0

for x in temp_list:
    total_val = total_val + x
    
