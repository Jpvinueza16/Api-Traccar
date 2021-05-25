import sys
import os
import xml.etree.ElementTree
import urllib
import urllib2
import json
import socket
import time


from ics import Calendar, Event
c = Calendar()
e = Event()
e.name = "prueba_2"
e.begin = '2014-01-01 00:00:00'
c.events.add(e)
c.events

