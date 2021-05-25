import urllib
import urllib2
import json
import base64

def formato(hora):
    partes = hora.split(":")
    convertida = "".join(partes)
    partes=convertida.split("-")
    convertida = "".join(partes)
    return convertida

def calendario(inicio,fin,nombre):
    inicio=formato(inicio)
    fin=formato(fin)
    c='BEGIN:VCALENDAR\r\nBEGIN:VEVENT\r\nDTSTART:'+inicio+'\r\nDTEND:'+fin+'\r\nSUMMARY:'+nombre+'\r\nEND:VEVENT\r\nEND:VCALENDAR'
    with open(nombre+'.ics', 'w') as my_file:
        my_file.writelines(c)

    return c


calendario=calendario('2020-02-27T12:50:00Z','2020-01-25T17:50:00Z','PRUEBAS1NOTIFICACIONES')
message = calendario
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')


url = "http://localhost:8082"
traccar_username ='admin'
traccar_password ='admin'

user = {'email': traccar_username, 'password': traccar_password}
request = urllib2.Request(url + '/api/session')
response = urllib2.urlopen(request, urllib.urlencode(user))
#print(response.headers.get('Set-Cookie'), url)
print (response.read())
print ("\n\n")
cookie = response.headers.get('Set-Cookie'), url

data = {
"name":"calendario3",
"data":base64_message
}
        
request1 = urllib2.Request(cookie[1] + '/api/calendars')
request1.add_header('Cookie', cookie[0])
request1.add_header('Content-Type', 'application/json')
request1.add_header('Accept', 'application/json')
response1 = urllib2.urlopen(request1, json.dumps(data))





 

  


