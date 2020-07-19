import pandas as pd
import requests

api_for_complete = 'https://services1.arcgis.com/0IrmI40n5ZYxTUrV/arcgis/rest/services/DailyConfirmedCases/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=DateVal%20asc&outSR=102100&resultOffset=0&resultRecordCount=2000&cacheHint=true'
apiCityDay = 'https://services1.arcgis.com/0IrmI40n5ZYxTUrV/arcgis/rest/services/CountyUAs_cases/FeatureServer/0/query?f=json&where=TotalCases%20%3C%3E%200&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=TotalCases%20desc&outSR=102100&resultOffset=0&resultRecordCount=1000&cacheHint=true'
overallCases = 'https://services1.arcgis.com/0IrmI40n5ZYxTUrV/arcgis/rest/services/DailyIndicators/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outSR=102100&resultOffset=0&resultRecordCount=50&cacheHint=true'


#overall data per day
data = requests.get(url).json()['E92000001']['dailyConfirmedCases']
vals = [x['value'] for x in data]
cols = [x['date'] for x in data]

df = pd.DataFrame([vals], columns=cols)
csvname = 'data/test.csv'
dat = pd.read_csv(csvname)
dat = dat.append(df)
dat.to_csv(csvname, index=False)


#cases per day per city
data = requests.get(apiCityDay).json()['features']
vals = []
cols = []
for x in data:
    x = x['attributes']
    vals.append(x['TotalCases'])
    cols.append(x['GSS_NM'])


df = pd.DataFrame([vals], columns=cols)
csvname = 'data/casescityday.csv'
dat = pd.read_csv(csvname)
dat = dat.append(df)
dat.to_csv(csvname, index=False)


#from graphy
data = requests.get(api_for_complete).json()['features']
arr = []
for x in data:
    x = x['attributes']
    arr.append([x['DateVal'], x['CMODateCount']])

with open("data/graph.json", "w") as graph:
    graph.write(str(arr))
