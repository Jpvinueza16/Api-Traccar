import urllib
import urllib2
import json
import base64


def login(url,user,password): 
    user = {'email': user, 'password': password}
    request = urllib2.Request(url + '/api/session')
    response = urllib2.urlopen(request, urllib.urlencode(user))
    return response.headers.get('Set-Cookie'),url

def geofence_calendar(idg,idc,nombre):

    if idg !=0 and idc!=0:
        cookie=login("http://localhost:8082","admin","admin")
        req = urllib2.Request(cookie[1] + '/api/geofences')
        req.add_header('Cookie', cookie[0])
        req.add_header('Content-Type', 'application/json')
        res = urllib2.urlopen(req)
        data = json.load(res)
        cont=0
        cont1=0
        for id in data:
            cont+=1
            if id['id'] ==idg:
                break
        for id in data:
            cont1+=1
            if cont1 == cont:
                 idg=(id['id'])
                 cont1=0
                 break
        for description in data:
            cont1+=1
            if cont1 == cont:
                 descripcion=(description['description'])
                 cont1=0
                 break
        for area in data:
            cont1+=1
            if cont1 == cont:
                 area1=(area['area'])
                 print area1
                 cont1=0
                 break
        for attributes in data:
            cont1+=1
            if cont1 == cont:
                 atributos=(attributes['attributes'])
                 cont1=0
                 break
        data={"id":idg,"attributes":atributos,"name":nombre,"calendarId":idc,"area": area1
        }
        req = urllib2.Request(cookie[1] + '/api/geofences/'+str("idg"))
        req.add_header('Cookie', cookie[0])
        req.add_header('Content-Type', 'application/json')
        req.add_header('Accept', 'application/json')
        req.get_method = lambda: 'PUT'
        res = urllib2.urlopen(req, json.dumps(data))
        print "asignacion correcta"
        val=1
    else :
        print "asignacion incorrecta "
        val=0

    return val

i = geofence_calendar(101,70,"prueba4")

print i


        
    
