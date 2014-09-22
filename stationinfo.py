import urllib2
import json

files = '''blataget-gtfs.csv 
blekingetrafiken-gtfs.csv 
dalatrafik-gtfs.csv 
gotlandskommun-gtfs.csv 
hallandstrafiken-gtfs.csv 
jonkopingslanstrafik-gtfs.csv 
kalmarlanstrafik-gtfs.csv 
lanstrafikenkronoberg-gtfs.csv 
localdata-gtfs.csv 
masexpressen.csv 
nettbuss-gtfs.csv 
nsb-gtfs.csv 
ostgotatrafiken-gtfs.csv 
pagelinks-gtfs.csv 
peopletravelgrouop.csv 
rt90cords-gtfs.csv 
skanerafiken-gtfs.csv 
sl-gtfs.csv 
swebus-gtfs.csv 
tib-gtfs.csv 
treminalmaps-gtfs.csv 
trv-gtfs.csv 
ul-gtfs.csv 
vasttrafik-gtfs.csv 
xtrafik-gtfs.csv'''

data = files.split("\n")

print data

alldata = {}

for filename in data:
  alldata[filename] = {}
  response = urllib2.urlopen('https://github.com/thuma/Transit-Stop-Identifier-Conversions-Sweden/raw/master/'+filename)
  downloaded = response.read().split("\n")
  rubriker = downloaded[0].split(";")
  downloaded[0] = downloaded[1]
  for row in downloaded:
    parts = row.split(";")
    alldata[filename][parts[0]] = {}
    for i in range(len(parts)):
	alldata[filename][parts[0]][rubriker[i]] = parts[i]

print alldata['hallandstrafiken-gtfs.csv']['7400110']
'''  
response = urllib2.urlopen('https://github.com/thuma/Transit-Stop-Identifier-Conversions-Sweden/raw/master/treminalmaps-gtfs.csv')
maps = response.read()
response = urllib2.urlopen('https://github.com/thuma/Transit-Stop-Identifier-Conversions-Sweden/raw/master/treminalmaps-gtfs.csv')
maps = response.read()
response = urllib2.urlopen('https://github.com/thuma/Transit-Stop-Identifier-Conversions-Sweden/raw/master/treminalmaps-gtfs.csv')
maps = response.read()'''