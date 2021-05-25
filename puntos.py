import urllib
import urllib2
import json


import sys
import math

import httplib
import time
import random

url = ""
traccar_username =''
traccar_password =''
#login de ingreso 
user = {'email': traccar_username, 'password': traccar_password}
request = urllib2.Request(url + '/api/session')
response = urllib2.urlopen(request, urllib.urlencode(user))
#print(response.headers.get('Set-Cookie'), url)
print (response.read())


print ("\n\n")

cookie = response.headers.get('Set-Cookie'), url

params = { 'deviceId' :11, 'from' : '2020-01-25T12:50:00.000Z', 'to' : '2020-01-25T14:52:00.000Z' }

request = urllib2.Request(cookie[1] + '/api/reports/route?' + urllib.urlencode(params))
request.add_header('Cookie', cookie[0])
request.add_header('Content-Type', 'application/json')
request.add_header('Accept', 'application/json')
response = urllib2.urlopen(request)
response1 = urllib2.urlopen(request)


latitud = []
for latitude in json.load(response):
        latitud.append(latitude['latitude'])
#print (latitud)

longitud = []
for longitude in json.load(response1):
        longitud.append(longitude['longitude'])
#print (longitud)

points = []


for i in range(0, len(longitud)):
    (lat) = latitud[i]
    (lon) = longitud[i]
    points.append(str(lat)+" "+str(lon))
 

print ("\n\n")

data = {
  "area": "LINESTRING "+"("+", ".join(points)+")",
#"area": "LINESTRING " +points1,
  "calendarId": None,
  "description": "ssasasasa",
  "name": "crea2"
}

request = urllib2.Request(cookie[1] + '/api/geofences')
request.add_header('Cookie', cookie[0])
request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request,json.dumps(data))


