import pandas

data = pandas.read_csv("229-2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

grey_s_count = len(data[data["Primary Fur Color"] == "Gray"])
red_s_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_s_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Full Color": ["Gray", "Cinnamon", 'Black'],
    "Count": [grey_s_count, red_s_count, Black_s_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
