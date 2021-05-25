import urllib
import urllib2
import json
import base64


def login(url,user,password): 
    user = {'email': user, 'password': password}
    request = urllib2.Request(url + '/api/session')
    response = urllib2.urlopen(request, urllib.urlencode(user))
    return response.headers.get('Set-Cookie'),url

def rutas(imei):
    cookie=login("http://localhost:8082","admin","admin")
    params = { 'uniqueId' :imei}
    req = urllib2.Request(cookie[1] + '/api/devices?'+urllib.urlencode(params))
    req.add_header('Cookie', cookie[0])
    req.add_header('Content-Type', 'application/json')
    try:
        res = urllib2.urlopen(req)
        data = json.load(res)
        for id in data:
            idd=(id['id'])
        print "imei encontado"
    except :
        print "imei no existe" 
        idd=0
    return idd

i=rutas(321)

print i
