# https://www.udemy.com/course/100-days-of-code/learn/lecture/20628466#overview

# Day 25

# with open("day25/weather_data.csv") as file:
#     data = file.readlines()

# print(data)

import csv

# temperatures = []
# with open("day25/weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
    
# print(data)
# print(temperatures)

# python -m pip install pandas
# python uninstall pandas
# https://pandas.pydata.org/docs/
import pandas

data = pandas.read_csv("day25/weather_data.csv")
# print(data)
# print(type(data)) # pandas DataFrame object
# print(data["temp"])
# print(type(data["temp"])) # pandas Series object
# data_dict = data.to_dict()
# print(data_dict)


# 2 ways to get the average of a column
# temp_list = data["temp"].to_list()
# print(temp_list)

# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
# print(data["temp"].mean())


# Getting max value in a column
# max_temp = data["temp"].max()
# print(max_temp)


# Getting a row with a specific value
# print(data[data.day == "Monday"])

# Getting the day (row) of the max temperature
# max_temp_day = data[data.temp == data.temp.max()]
# print(max_temp_day)

# monday = data[data.day == "Monday"]
# # Converting monday's temperature into fahrenheit
# monday_F_temp = (int(monday.temp) * 9/5) + 32
# print(monday_F_temp)


# Creating a dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
# new_dataframe = pandas.DataFrame(data_dict)
# print(new_dataframe)
# new_dataframe.to_csv("day25/new_data.csv")


# Analysing squirrel data

squirrel_data = pandas.read_csv("day25/2018_Central_Park_Squirrel_Data.csv")
labels = squirrel_data.columns
# print(labels)
colors_col = squirrel_data["Primary Fur Color"]

data = colors_col.value_counts()
# print(data)
# print(type(data))

data_dict = data.to_dict()
# print(data_dict)
new_dict = {
    "Fur color": [],
    "Count": []
}
for key in data_dict:
    new_dict["Fur color"].append(key)
    new_dict["Count"].append(data_dict[key])

# print(new_dict)

new_csv = pandas.DataFrame(new_dict)
# new_csv.to_csv("day25/Squirrel_count_per_fur_color.csv")