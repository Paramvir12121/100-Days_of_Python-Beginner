import pandas

# data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].to_list()

# # print(temp_list)

# # total_val = 0


# # for x in temp_list:
# #     total_val = total_val + x

# # average_temp = total_val/len(temp_list)

# # print("Average temp of week is: ",average_temp)

# # max_temp = data["temp"].max()

# # print("Max Temp: ",max_temp)

# # print(data[data.temp == data.temp.max()])
# # print(data[data.day == "Monday"])

# temp_in_C = data[data.day == "Monday"]["temp"].to_list()

# temp_in_F = (1.8 * temp_in_C[0]) + 32

# # or 
# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp[0]

# print(temp_in_F)

# Creating a Dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "score": [76,56,65]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")