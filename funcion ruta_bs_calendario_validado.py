import urllib
import urllib2
import json
import base64


def rutas(ime,nombre_geocerca,nombre_calendario,fechaHora_inicio,fechaHora_fin):
    cookie=login("http://localhost:8082","admin","admin")
    params = { 'uniqueId' :ime}
    req = urllib2.Request(cookie[1] + '/api/devices?'+urllib.urlencode(params))
    req.add_header('Cookie', cookie[0])
    req.add_header('Content-Type', 'application/json')
    res = urllib2.urlopen(req)
    data = json.load(res)
    idg=r=geofence(nombre_geocerca,cookie)
    for id in data:
        idd=(id['id'])
    idc=calendario(fechaHora_inicio,fechaHora_fin,cookie,nombre_calendario)
    geofence_calendar(cookie,idg,idc,nombre_geocerca)
    ruta_bus(idg,idd,cookie)


def geofence(nombre,cookie):
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
            break
    for id in data:
        cont1+=1
        if cont1 == cont:
             return (id['id'])


def ruta_bus(idg,idd,cookie):
    data={"deviceId":idd , "geofenceId": idg}
    req = urllib2.Request(cookie[1] + '/api/permissions' )
    req.add_header('Cookie', cookie[0])
    req.add_header('Content-Type', 'application/json')
    req.add_header('Accept', 'application/json')
    res = urllib2.urlopen(req,json.dumps(data,sort_keys=True))


def formato(hora):
    partes = hora.split(":")
    convertida = "".join(partes)
    partes=convertida.split("-")
    convertida = "".join(partes)
    return convertida


def calendario(inicio,fin,cookie,nombre):
    inicio=formato(inicio)
    fin=formato(fin)
    c='BEGIN:VCALENDAR\r\nBEGIN:VEVENT\r\nDTSTART:'+inicio+'\r\nDTEND:'+fin+'\r\nSUMMARY:'+nombre+'\r\nEND:VEVENT\r\nEND:VCALENDAR'    
    message_bytes = c.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    with open(nombre+'.ics', 'w') as my_file:
        my_file.writelines(c)
    data = {"name":nombre,"data":base64_message}   
    req = urllib2.Request(cookie[1] + '/api/calendars')
    req.add_header('Cookie', cookie[0])
    req.add_header('Content-Type', 'application/json')
    req.add_header('Accept', 'application/json')
    res = urllib2.urlopen(req, json.dumps(data))
    data = json.load(res)
    idc=(data['id'])
    return idc
    

def geofence_calendar(cookie,idg,idc,nombre):
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
             break
    for description in data:
        if cont1 == cont:
             descripcion=(description['description'])
             break
    for area in data:
        if cont1 == cont:
             area1=(area['area'])
             break
    for attributes in data:
        if cont1 == cont:
             atributos=(attributes['attributes']) 
             break
    data={"id":idg,"attributes":atributos,"name":nombre,"calendarId":idc,"area": area1
    }
    req = urllib2.Request(cookie[1] + '/api/geofences/'+str("idg"))
    req.add_header('Cookie', cookie[0])
    req.add_header('Content-Type', 'application/json')
    req.add_header('Accept', 'application/json')
    req.get_method = lambda: 'PUT'
    res = urllib2.urlopen(req, json.dumps(data))


def login(url,user,password):
    
    user = {'email': user, 'password': password}
    request = urllib2.Request(url + '/api/session')
    response = urllib2.urlopen(request, urllib.urlencode(user))
    return response.headers.get('Set-Cookie'),url    

rutas(123,"p3","calendarioprueba4","2020-01-25T12:50:00Z","2020-01-25T12:50:00Z")



