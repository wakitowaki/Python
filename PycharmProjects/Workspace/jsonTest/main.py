import json
import urllib2
import tablib


headers = ('first_name', 'last_name','c','d')
url = ("http://maps.googleapis.com/maps/api/geocode/json?"
       "address=googleplex&sensor=false")
output = urllib2.urlopen(url).read()

data = tablib.Dataset(*output)

print data[1]