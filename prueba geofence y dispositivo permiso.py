import urllib
import urllib2
import json
import base64


def login(url,user,password): 
    user = {'email': user, 'password': password}
    request = urllib2.Request(url + '/api/session')
    response = urllib2.urlopen(request, urllib.urlencode(user))
    return response.headers.get('Set-Cookie'),url

def ruta_bus(idg,idd):
    if idg != 0 and idd !=0:
        cookie=login("http://localhost:8082","admin","admin")
        data={"deviceId":idd , "geofenceId": idg}
        req = urllib2.Request(cookie[1] + '/api/permissions' )
        req.add_header('Cookie', cookie[0])
        req.add_header('Content-Type', 'application/json')
        req.add_header('Accept', 'application/json')
        res = urllib2.urlopen(req,json.dumps(data,sort_keys=True))
        print "asignacion correcta"
        val = 1
    else:
        print "asignacion incorrecta"
        val =0
    return val

i=ruta_bus(0,1)
    
print i


    
