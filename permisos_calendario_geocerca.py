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

    "userId":33,
    "calendarId":33,
    "geofenceId":1,
     
   
    }

cookie = response.headers.get('Set-Cookie'), url
request1 = urllib2.Request(cookie[1] + '/api/permissions')
request1.add_header('Cookie', cookie[0])
request1.add_header('Content-Type', 'application/json')
response1 = urllib2.urlopen(request1, json.dumps(data))




