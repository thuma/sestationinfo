import LatLon
import tornado.ioloop
import tornado.web

ins = open("../Transit-Stop-Identifier-Conversions-Sweden/stops.txt", "r" )
ids = []
for line in ins:
    parts = line.strip().split(',')
    try:
      ids.append({"id":parts[0],"lat":float(parts[2]),"lon":float(parts[3])})
    except:
      error = 1
ins.close()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
      done = []
      try:
        latin = float(self.get_argument('lat'))
        lonin = float(self.get_argument('lon'))
        distin = float(self.get_argument('distance',5000))
        limit = int(self.get_argument('limit',100))
        start = LatLon.LatLon(latin,lonin)
      except:
        self.write({"error":"malformed request must be formated like this example ?lat=15.2&long=60.0 , optional: &distance=10000 in meters. Good values are 1 to 10000 default 5000 meters, &limit=2 number of stops to show default 100"})
        self.finish()
      for line in ids:
        if abs(latin-line["lat"]) < 1 and abs(lonin-line["lon"]) < 1:
          distance = LatLon.LatLon(line["lat"], line["lon"]).distance(start)*1000
          if distance < distin:
            line["distance"] = distance
            done.append(line)
      self.write({"closesto":sorted(done, key=lambda row: row["distance"])[:limit]})

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(9090)
    tornado.ioloop.IOLoop.instance().start()




