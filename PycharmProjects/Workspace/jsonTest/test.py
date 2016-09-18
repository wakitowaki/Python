from json2xml.json2xml import Json2xml

url = ("http://maps.googleapis.com/maps/api/geocode/json?"
       "address=googleplex&sensor=false")
data = Json2xml.fromurl(url).data
data_object = Json2xml(data)

print data_object.json2xml()
print data