# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a CSV file

import csv
import json
import datetime

# read in the contents of the JSON file
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 5


# Filter the data by quakes that are larger than 5 magnitude
largequakes = list(filter(isbig, data["features"]))

# TODO: Create the header and row structures for the data
headers = ["place", "mag", "time", "url"]
# TODO: populate the rows with the resulting quake data
rows = []
#for q in largequakes:
#    rows.append([q["properties"]["place"], q["properties"]["mag"], q["properties"]["time"], q["properties"]["url"]])
for quake in largequakes:
    thedate = datetime.date.fromtimestamp(int(quake["properties"]["time"] / 1000.0)).strftime("%Y-%m-%d %H:%M:%S")
    rows.append([quake["properties"]["place"], quake["properties"]["mag"], thedate, quake["properties"]["url"]])
#order it by the date column
rows.sort(key=lambda x: x[2], reverse=True)

# TODO: write the results to the CSV file
with open("largequakes.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(headers)
    csvwriter.writerows(rows)