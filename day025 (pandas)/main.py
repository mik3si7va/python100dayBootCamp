from os import path

directory = path.dirname(__file__)

# read the lines of weather_data.csv into a list called data
data = []
with open(path.join(directory, "weather_data.csv")) as data_file:
    data = data_file.readlines()

print(data)

# make the data into a list of lists
new_data = []
for row in data:
    new_data.append(row.strip().split(","))

print(new_data)
print("\n---------------------\n")
import csv

with open(path.join(directory, "weather_data.csv")) as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)


print("\n---------------------\n")

import pandas

pandas_data = pandas.read_csv(path.join(directory, "weather_data.csv"))
print(pandas_data)

print(type(pandas_data))
print(type(pandas_data["temp"]))

pandas_data_dict = pandas_data.to_dict()
print(pandas_data_dict)

temperatures_list = pandas_data["temp"].to_list()
print(temperatures_list)

average_temp = pandas_data["temp"].mean()
print(average_temp)


max_temp = pandas_data["temp"].max()
print(max_temp)

# get the row of data where the day is Monday

monday_data = pandas_data[pandas_data["day"] == "Monday"]
print(monday_data)


# get the row of data where the temp is the max temp

max_temp_data = pandas_data[pandas_data["temp"] == pandas_data["temp"].max()]
print(max_temp_data)

monday = pandas_data[pandas_data["day"] == "Monday"]
monday_temp = int(monday["temp"])
monday_temp_f = monday_temp * 9 / 5 + 32
print(monday_temp_f)

# create a dataframe from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

data = pandas.DataFrame(data_dict)
print(data)
