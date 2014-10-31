import LatLon
ins = open("../Transit-Stop-Identifier-Conversions-Sweden/stops.txt", "r" )
ids = []
for line in ins:
    parts = line.strip().split(',')
    try:
      ids.append({"id":parts[0],"lat":float(parts[2]),"lon":float(parts[3])})
    except:
      error = 1
ins.close()

latin = 59.3284697
lonin = 18.0617493

start = LatLon.LatLon(latin,lonin)
for line in ids:
  if abs(latin-line["lat"]) < 1 and abs(lonin-line["lon"]) < 1:
    distance = LatLon.LatLon(line["lat"], line["lon"]).distance(start)*1000
    if distance < 5000:
      print str(distance) + "m, id:"+line["id"]
