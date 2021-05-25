import urllib
import urllib2
import json
import base64

def login(url,user,password):
    
    user = {'email': user, 'password': password}
    request = urllib2.Request(url + '/api/session')
    response = urllib2.urlopen(request, urllib.urlencode(user))
    return response.headers.get('Set-Cookie'),url

def formato(hora):
    partes = hora.split(":")
    convertida = "".join(partes)
    partes=convertida.split("-")
    convertida = "".join(partes)
    return convertida

def calendario(inicio,fin,nombre):
    cookie=login("http://localhost:8082","admin","admin")
    req = urllib2.Request(cookie[1] + '/api/calendars')
    req.add_header('Cookie', cookie[0])
    req.add_header('Content-Type', 'application/json')
    res = urllib2.urlopen(req)
    data = json.load(res)
    for name in data:
        ver= (name['name'])
        if str(ver) ==nombre:
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

    
id=calendario("2020-01-21T20:51:00Z","2020-01-25T21:52:00Z","calendario13")
print id
    
