import urllib
import urllib2
import json
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
latitud = []
for latitude in json.load(response):
        latitud.append(latitude['latitude'])
print (latitud)


