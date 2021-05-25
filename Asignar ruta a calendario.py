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
# DICCIONARIO DE USURIO 
data={
"id":1,
"attributes":{},
"name":"probar",
"calendarId":1,
"area": "LINESTRING (-0.9366261708350692 -438.61373258314535, -0.936486045004699 -438.61245854882685, -0.9361803183747242 -438.6102162489446, -0.9379255115785412 -438.61003788362166, -0.9384987501600364 -438.6125732124339, -0.936575215752697 -438.61299364220383, -0.9369064205352089 -438.6146244071684)"
}
id = {'id':1}

request1 = urllib2.Request(cookie[1] + '/api/geofences/'+str("id"))
request1.add_header('Cookie', cookie[0])
request1.add_header('Content-Type', 'application/json')
request1.add_header('Accept', 'application/json')
request1.get_method = lambda: 'PUT'
response1 = urllib2.urlopen(request1, json.dumps(data))





 



