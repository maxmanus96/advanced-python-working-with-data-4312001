# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
    
#number 1
print("Number of quakes: ", len(data["features"]))

#number 2
print("Number of quakes felt by at least 100 people: ", len([x for x in data["features"] if x["properties"]["felt"] is not None and x["properties"]["felt"] >= 100]))

#number 3
try:
    print("Name of place whose quake was felt by the most people: ", max((x for x in data.get("features", []) if x.get("properties", {}).get("felt") is not None), key=lambda x: x["properties"]["felt"])["properties"]["place"])
except (ValueError, KeyError, TypeError):
    print("An error occurred while processing the data.")


#number 4
print("Top 10 most significant events: ")
for x in sorted(data["features"], key=lambda x: x["properties"]["sig"], reverse=True)[:10]:
    print(x["properties"]["title"], x["properties"]["sig"])

