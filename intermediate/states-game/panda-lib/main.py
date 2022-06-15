# Without csv module ======================

# with open("./weather_data.csv") as raw:
#     data = raw.readlines()
#     print(data)

# import csv

# # With csv module ===========================
# with open("./weather_data.csv") as raw:
#     data = csv.reader(raw)
#     temperatures = []
#     for temp in data:
#         if temp[1] != "temp":
#             temperatures.append(int(temp[1]))
#     print(temperatures)

# with panda library
# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_to_dict = data.to_dict()
# print(data_to_dict)

# temp_list = data["temp"].to_list()
# # average datas in a list
# print(sum(temp_list) / len(temp_list))

# # average datas in a list WITH panda lib==========
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.temp.mean())

# getting data in a row=========================
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp_in_f = (monday.temp * 9 / 5) + 32
# print(monday.temp)
# print(monday_temp_in_f)

# creating a dataframe from scratch ===============
# data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)


# # squirrel data attempt==================
# import pandas as pd

# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
# cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

# squirrel_data_dict = {
#     "fur_color": ["Gray", "Cinnamon", "Black"],
#     "count": [gray_squirrels, black_squirrels, cinnamon_squirrels],
# }
# squirrel_data = pd.DataFrame(squirrel_data_dict)
# squirrel_data.to_csv("squirrel_data.csv")

l1 = ["one", "two", "three", "four"]
l2 = ["one", "two"]

print(list(set(l1) - set(l2)))
