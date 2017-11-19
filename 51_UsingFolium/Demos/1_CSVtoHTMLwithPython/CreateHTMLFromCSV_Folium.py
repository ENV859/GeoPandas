# CreateHTMLFromCSV.py

# Creates a Google Maps HTML document containing
# markers contained in the specified CSV file

# Fall 2013
# J.Fay for ENV859

import sys, os, folium

# Script variables
inputCSV = "Pennsylvania Oil and Gas Violations.csv"
latFld = "latitude"
lonFld = "longitude"
nameFld = "Viol Id"
outputHTML = "Violations_Folium.html"

# Create folium map object
out_map = folium.Map(location=(41.79, -76.58))

# Read header row
inFileObj = open(inputCSV,'r')
headerLine = inFileObj.readline()
fieldNames = headerLine.split(",")

# Get field indices based on where the field names occur in the list of header items
latIdx = fieldNames.index(latFld)
lonIdx = fieldNames.index(lonFld)
nameIdx = fieldNames.index(nameFld)

# Loop through the records in the CSV and add as markers to the map
lineString = inFileObj.readline()
while lineString:
    # Parse the lineString into alist
    lineData = lineString.split(",")
    try: # Will skip line if lat or lon aren't numbers
        # Get Values at the indices discovered above
        lat = float(lineData[latIdx])
        lon = float(lineData[lonIdx])
        name = lineData[nameIdx]
        # Create marker and add to the map
        m = folium.Marker((lat,lon),popup=name).add_to(out_map)
    except:
        pass#print lineString
    
    lineString = inFileObj.readline()

# Close the inFileObj
inFileObj.close()

# Save the map
out_map.save(outputHTML)