import urllib
import urllib2
import json
url = "http://localhost:8082"
traccar_username ='admin'
traccar_password ='admin'
#login de ingreso 
user = {'email': traccar_username, 'password': traccar_password}
request = urllib2.Request(url + '/api/session')
response = urllib2.urlopen(request, urllib.urlencode(user))
#print(response.headers.get('Set-Cookie'), url)
print (response.read())
print ("\n\n")

geo=[1]

cookie = response.headers.get('Set-Cookie'), url
# DICCIONARIO DE USURIO 
data={
"id": 1,
"attributes": {},
"groupId": 1,
"name": "bus",
"uniqueId": "123",
"status": "offline",
"lastUpdate": None,
"positionId": None,
"geofenceIds":[],
"phone": "",
"model": "",
"contact": "",
"category": "bus",
"disabled": False
}
id = {'id':1}

request1 = urllib2.Request(cookie[1] + '/api/devices/'+str("id"))
request1.add_header('Cookie', cookie[0])
request1.add_header('Content-Type', 'application/json')
request1.add_header('Accept', 'application/json')
request1.get_method = lambda: 'PUT'
response1 = urllib2.urlopen(request1, json.dumps(data))

