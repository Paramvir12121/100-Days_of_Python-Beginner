import pandas

data = pandas.read_csv("weather_data.csv")

temp_list = data["temp"].to_list()

# print(temp_list)

# total_val = 0


# for x in temp_list:
#     total_val = total_val + x

# average_temp = total_val/len(temp_list)

# print("Average temp of week is: ",average_temp)

# max_temp = data["temp"].max()

# print("Max Temp: ",max_temp)

# print(data[data.temp == data.temp.max()])
# print(data[data.day == "Monday"])

temp_in_C = data[data.day == "Monday"]["temp"].to_list()

temp_in_F = (1.8 * temp_in_C[0]) + 32

print(temp_in_F)