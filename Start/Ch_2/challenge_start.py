# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import Counter

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

try:
    event_types = [x["properties"]["type"] for x in data.get("features", {}) if x.get("properties", {}).get("felt") is not None and x.get("properties", {}).get("type") is not None]
    print("Number of each event type that was felt by people: ", Counter(event_types))
except (ValueError, KeyError, TypeError):
    print("An error occurred while processing the data.")