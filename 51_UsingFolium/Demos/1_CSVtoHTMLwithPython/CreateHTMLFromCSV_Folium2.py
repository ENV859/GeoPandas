# CreateHTMLFromCSV.py

# Creates a Google Maps HTML document containing
# markers contained in the specified CSV file

# Fall 2017
# J.Fay for ENV859

import pandas as pd
import folium
from folium.plugins import MarkerCluster

#Filename to save the output to:
outputHTML = 'Violations_folium.html'

#Read the data into a Pandas dataFrame
df = pd.read_csv('Pennsylvania Oil and Gas Violations.csv')

#Remove rows missing lat/long data
df.dropna(subset=['latitude','longitude'],axis='rows',how='any',inplace=True)

#Get the mean latitude and longitude, to set as the center of the map
meanLat = df['latitude'].mean()
meanLng = df['longitude'].mean()

#Create the folium map object
wellMap = folium.Map(location=(meanLat,meanLng),zoom_start=7)

#Create a marker cluster object which enables a cleaner display of markers
marker_cluster = MarkerCluster()
marker_cluster.add_to(wellMap)

#Add as Clustered Markers
for row in df[:20].iterrows():
    data = row[1] #The data of the row is the 2nd object (1st is the row's index)
    
    #Get the row's data that we want
    lat = data['latitude']
    lon = data['longitude']
    name = data['Viol Id']
    
    #Create a marker
    m = folium.Marker((lat,lon),popup=str(name))
    
    #Add it to the marker cluster object
    m.add_to(marker_cluster)

# Save the map
wellMap.save(outputHTML)