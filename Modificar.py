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
cookie = response.headers.get('Set-Cookie'), url
data={
     "id": 65,
      "attributes": {},
        "groupId": 0,
        "name": "MIBUS11",
        "uniqueId": "12345",
        "status": "online",
        "lastUpdate": "2020-02-26T19:28:41.267+0000",
        "positionId": 1604,
        "geofenceIds": [],
        "phone": "",
        "model": "",
        "contact": "",
        "category": None,
        "disabled": False
}
id = {'id':65}
        
request1 = urllib2.Request(cookie[1] + '/api/devices/'+str("id"))
request1.add_header('Cookie', cookie[0])
request1.add_header('Content-Type', 'application/json')
request1.add_header('Accept', 'application/json')
request1.get_method = lambda: 'PUT'
response1 = urllib2.urlopen(request1, json.dumps(data))
