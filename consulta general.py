
import sys
import os
import xml.etree.ElementTree
import urllib
import urllib2
import json
import socket
import time

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
print ("\n\n")
cookie = response.headers.get('Set-Cookie'), url




request = urllib2.Request(cookie[1] + '/api/devices')
request.add_header('Cookie', cookie[0])
res = urllib2.urlopen(request)
            
ids = []
for id in json.load(res):
        ids.append(id['id'])

result = []
for i in range(0, len(ids)):

    params = { 'deviceId' : 11, 'type': "geofenceExit",'from' : '2020-01-01T12:50:00.000Z', 'to' : '2020-03-01T14:52:00.000Z' }
    request = urllib2.Request(cookie[1] + '/api/reports/events?'+ urllib.urlencode(params))
    request.add_header('Cookie', cookie[0])
    res = urllib2.urlopen(request)
    data = json.load(res)
    result.append(data)




    
        



