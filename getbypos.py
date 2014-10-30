import LatLon
ins = open("../Transit-Stop-Identifier-Conversions-Sweden/stops.txt", "r" )
ids = []
for line in ins:
    parts = line.split(',')
    if parts[0] != "stopid":
    	ids.append({"id":parts[0],"lon":parts[2],"lat":parts[3]})
ins.close()

start = LatLon.LatLon(60.0, 16.0)
for line in parts:
	distance = LatLon.LatLon(line["lat"], line["lon"]).distance(start)
	print distance
	