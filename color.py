import urllib
import urllib2
import json
import math
import time
import random


def hex_code_colors():
    a = hex(random.randrange(0,256))
    b = hex(random.randrange(0,256))
    c = hex(random.randrange(0,256))
    a = a[2:]
    b = b[2:]
    c = c[2:]
    if len(a)<2:
        a = "0" + a
    if len(b)<2:
        b = "0" + b
    if len(c)<2:
        c = "0" + c
    z = a + b + c
    return "#" + z.upper()
color=hex_code_colors()

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
data = json.load(response)


latitud = []
for latitude in data:
        latitud.append(latitude['latitude'])
#print (latitud)

longitud = []
for longitude in data:
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
  "description": "color",
  "name": "rutacolor",
  "attributes": {
            "color":color
        }
}

request = urllib2.Request(cookie[1] + '/api/geofences')
request.add_header('Cookie', cookie[0])
request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request,json.dumps(data))
print ("Creada")
