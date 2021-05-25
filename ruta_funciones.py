import urllib
import urllib2
import json
import base64


def principal(nombre_calendario,hora_inicio,hora_fin,nombre_geocerca,imei):
    cookie=login("http://localhost:8082","admin","admin")
    idg=geofence(nombre_geocerca,cookie)
    idd=id_bus(imei,cookie)
    idc=0
    if  idg!=0 and idd!=0 :
        idc=calendario(hora_inicio,hora_fin,nombre_calendario,cookie)
        if idc != 0:
            asn_cal_geo=geofence_calendario(idg,idc,nombre_geocerca,cookie)     
            asn_ruta=ruta_bus(idg,idd)
        print "correcto "+" Calendario : "+ str(idc)+" Geocerca : "+str(idg)+" Dispositivo : "+str(idd)
    else :
        print "error "+" Calendario : "+ str(idc)+" Geocerca : "+str(idg)+" Dispositivo : "+str(idd)
     
#1 login de ingreso

def login(url,user,password): 
    user = {'email': user, 'password': password}
    req = urllib2.Request(url + '/api/session')
    resp = urllib2.urlopen(req, urllib.urlencode(user))
    return resp.headers.get('Set-Cookie'),url


# 2 creacion de calendarios 
def formato(hora):
    partes = hora.split(":")
    convertida = "".join(partes)
    partes=convertida.split("-")
    convertida = "".join(partes)
    return convertida

def calendario(inicio,fin,nombre,cookie):
    req = urllib2.Request(cookie[1] + '/api/calendars')
    req.add_header('Cookie', cookie[0])
    req.add_header('Content-Type', 'application/json')
    res = urllib2.urlopen(req)
    data = json.load(res)
    for name in data:
        ver= (name['name'])
        if str(ver) == nombre:
            idc=0
            print "nombre de calendario ya existe"
            break
        else:
            idc=1
    if(idc==1):
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
        print "calendario creado"
    return idc


#3 id por nombre geocerca

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
            for id in data:
                cont1+=1
                if cont1 == cont:
                    idg=(id['id'])
            break                                       
        else :
            idg=0
    if idg != 0:
        print "geocerca encontrada "
    else :
        print "geocerca no encontrada"
    return (idg)


#4 asignar geocerca a calendario

def geofence_calendario(idg,idc,nombre,cookie):
    if idg !=0 and idc!=0:
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
        print "asignacion calendario correcta"
        val=1
    else :
        print "asignacion calendario incorrecta "
        val=0
    return val


#5 obtener id dipositivo

def id_bus(imei,cookie):
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

#6 asignar ruta
    
def ruta_bus(idg,idd):
    if idg != 0 and idd !=0:
        cookie=login("http://localhost:8082","admin","admin")
        data={"deviceId":idd , "geofenceId": idg}
        req = urllib2.Request(cookie[1] + '/api/permissions' )
        req.add_header('Cookie', cookie[0])
        req.add_header('Content-Type', 'application/json')
        req.add_header('Accept', 'application/json')
        res = urllib2.urlopen(req,json.dumps(data,sort_keys=True))
        print "asignacion de ruta correcta"
        val = 1
    else:
        print "asignacion de ruta incorrecta"
        val =0
    return val

principal("calendario","2020-01-21T20:51:00Z","2020-01-25T21:52:00Z","prueba",358004090445321)

