import sys
import os
import xml.etree.ElementTree
import urllib
import urllib2
import json
import socket
import time

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

data= {

"deviceId":2,
"userId":65
}

cookie = response.headers.get('Set-Cookie'), url
request = urllib2.Request(cookie[1] + '/api/permissions')
request.add_header('Cookie', cookie[0])
request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request, json.dumps(data))
print (response.read())



