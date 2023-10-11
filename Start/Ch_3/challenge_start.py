# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import time


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
try:
    # Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
    headers = ["Magnitude", "Place", "Felt Reports", "Date", "Google Map Link"]
    
    
    rows = []

    for x in sorted(data["features"], key=lambda x: x["properties"]["sig"], reverse=True)[:40]:
        longitude, latitude, _ = x["geometry"]["coordinates"]
        google_maps_link = f"https://www.google.com/maps/search/?api=1&query={latitude}%2C{longitude}"
        rows.append([x["properties"]["mag"], x["properties"]["place"], x["properties"]["felt"], x["properties"]["time"], google_maps_link])

    # order it by the date column
    rows.sort(key=lambda x: x[3], reverse=True)

    # Date should be in the format of YYYY-MM-DD
    for x in rows:
        x[3] = time.strftime("%Y-%m-%d", time.gmtime(x[3]/1000.0))

    #Write the results to the CSV file
    with open("significantseismicevents.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(headers)
        csvwriter.writerows(rows)
        

except (ValueError, KeyError, TypeError):
    print("An error occurred while processing the data.")




