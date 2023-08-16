import csv

tempratures = []
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        try:
            tempratures.append(int(row[1]))
        except:
            pass
        

print(tempratures)