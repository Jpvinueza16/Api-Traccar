
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

cookie = response.headers.get('Set-Cookie'), url

print ("\n\n")


cookie = response.headers.get('Set-Cookie'), url
request = urllib2.Request(cookie[1] + '/api/users/33')
request.add_header('Cookie', cookie[0])
response = urllib2.urlopen(request)
print (response.read())



