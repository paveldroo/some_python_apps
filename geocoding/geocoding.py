import pandas

import geopy

df0 = pandas.read_json('https://pythonhow.com/supermarkets.json')
df0['Address'] = df0['Address'] + ', ' + df0['City'] + ', ' + df0['State'] + ', ' + df0['Country']

geolocator = geopy.Nominatim()

df0['Coordinates'] = df0['Address'].apply(geolocator.geocode)

df0['Latitude'] = df0['Coordinates'].apply(lambda x: x.latitude if x != None else 'Not Found')
df0['Longitude'] = df0['Coordinates'].apply(lambda x: x.longitude if x != None else 'Not Found')

print(df0)