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
data = {
"name":"jefferson",
"email":"jefferson@gmail.com",
"readonly":True,
"administrator":False,
"map":"",
"latitude":0.0,
"longitude":0.0,
"zoom":0,
"password":"andres",
"twelveHourFormat":False,
"coordinateFormat":"",
"disabled":False,
"expirationTime":None,
"deviceLimit":-1,
"userLimit":0,
"deviceReadonly":True,
"limitCommands":True,
"poiLayer":"",
"token":None
}

request = urllib2.Request(cookie[1] + '/api/users')
request.add_header('Cookie', cookie[0])
request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request, json.dumps(data))
data = json.load(response)
