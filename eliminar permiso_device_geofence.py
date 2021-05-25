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

data={"deviceId":11 , "geofenceId": 8}

cookie = response.headers.get('Set-Cookie'), url
request1 = urllib2.Request(cookie[1] + '/api/permissions' )
request1.add_header('Cookie', cookie[0])
request1.add_header('Content-Type', 'application/json')
request1.add_header('Accept', 'application/json')
request1.get_method = lambda: 'DELETE'
response1 = urllib2.urlopen(request1,json.dumps(data,sort_keys=True))
