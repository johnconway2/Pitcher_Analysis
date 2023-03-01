import csv

pitcher_data="Pitcher_data.csv"
count=0
avg_era=0
balk_age=0

with open(pitcher_data, "r") as csvfile:
    csvreader=csv.reader(csvfile)
    header=next(csvreader)