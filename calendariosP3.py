import urllib.request
import urllib.parse
import urllib.error
import json
import base64

from ics import Calendar, Event

c = Calendar()
e = Event()
e.name = "prueba_2"
e.begin = '2014-01-01 00:00:00'
c.events.add(e)
c.events

message = str(c)
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

url = "http://localhost:8082"
traccar_username ='admin'
traccar_password ='admin'

user = {'email': traccar_username, 'password': traccar_password}
request = urllib.request.Request(url + '/api/session')
response = urllib.request.urlopen(request,urllib.parse.urlencode(user).encode("utf-8"))

print((response.read()))
print ("\n\n")
cookie = response.headers.get('Set-Cookie'), url

data = {
"name":"prueba4",
"data":base64_message
}

request = urllib.request.Request(cookie[1] + '/api/calendars')
request.add_header('Cookie', cookie[0])
request.add_header('Content-Type', 'application/json')
response = urllib.request.urlopen(request,json.dumps(data).encode("utf-8"))
print (data)
