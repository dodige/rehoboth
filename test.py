import o1
import os, sys

OMXPLAYER='/usr/bin/omxplayer.bin'
OMXPLAYER_LIB_PATH='/opt/vc/lib:/usr/lib/omxplayer'
LOCAL_LIB_PATH='/usr/local/lib'



reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(LOCAL_LIB_PATH)
os.environ['LD_LIBRARY_PATH'] = OMXPLAYER_LIB_PATH
import time, getopt, re
import signal, multiprocessing, subprocess
import gobject, dbus, dbus.service
from dbus.mainloop.glib import DBusGMainLoop  # setting up an event loop
from o1 import ListService
from o1 import OMXPlayer

DBusServiceName = 'raspberry.pi.OMXPlayer'

IDBusProperties = 'org.freedesktop.DBus.Properties'
IList = 'raspberry.pi.OMXPlayerList'
IPlayer = 'raspberry.pi.OMXPlayer'


Log_Mode = True
Log_Max_Size = 10485760  # 1024 * 1024 * 10 (10MB)
Debug_Mode = True
Bus_Type = 'system'


# You must do this before connecting to the bus.
DBusGMainLoop(set_as_default=True) # if you use DBus.
loop = gobject.MainLoop()

# enable g_event_timer tick.
#gobject.timeout_add(10000, g_event_timer)

if Bus_Type == 'session':
    bus = dbus.SessionBus()
else:
    bus = dbus.SystemBus()
dodo1  = ListService(bus, loop)
dodo1.Service = dodo1

try:
    loop.run()
except:
    pass

x=0
y=0
width=500
height=700
keepratio= True
options = "-o both"
movies = "/home/pi/2.mov"

dodo1.Play(movies, x, y, width, height, keepratio, options)

if Debug_Mode:
    _debug_text = "ON"
else:
    _debug_text = "OFF"


