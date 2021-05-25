import urllib
import urllib2
import json
import base64

def login(url,user,password):
    
    user = {'email': user, 'password': password}
    request = urllib2.Request(url + '/api/session')
    response = urllib2.urlopen(request, urllib.urlencode(user))
    return response.headers.get('Set-Cookie'),url

def geofence(nombre):
    cookie=login("http://localhost:8082","admin","admin")
    req = urllib2.Request(cookie[1] + '/api/geofences')
    req.add_header('Cookie', cookie[0])
    req.add_header('Content-Type', 'application/json')
    res = urllib2.urlopen(req)
    data = json.load(res)
    cont=0
    cont1=0
    for name in data:
        cont+=1
        ver= (name['name'])
        if str(ver) ==nombre:
            for id in data:
                cont1+=1
                if cont1 == cont:
                    ids=(id['id'])
            break                                       
        else :
            ids=0
    if ids != 0:
        print "nombre encontrado"
    else :
        print "nombre no encontrado"
    return (ids)
i=geofence("prueba2")
print i
