#!/usr/bin/env python

import dbus, time, sys, os
from subprocess import Popen

import ctypes

c1 = "OMXPLAYER_DBUS_ADDR = '/tmp/omxplayerdbus' "
c2 = "OMXPLAYER_DBUS_PID = '/tmp/omxplayerdbus.pid'"
c3 = "export DBUS_SESSION_BUS_ADRESS = 'cat $OMXPLAYER_DDUS_ADDR'"
c4 = "export DBUS_SESSION_BUS_PID = 'cat $OMXPLAYER_DBUS_PID'"

#if os.fork() == 0:
ctypes.CDLL('libbcm_host.so').bcm_host_init()

OMXPLAYER='/usr/bin/omxplayer'
OMXPLAYER_LIB_PATH='/opt/vc/lib:/usr/lib/omxplayer'
LOCAL_LIB_PATH='/usr/local/lib'

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(LOCAL_LIB_PATH)
os.environ['LD_LIBRARY_PATH'] = OMXPLAYER_LIB_PATH

c5 = "OMXPLAYER_DBUS_ADDR='/tmp/omxplayerdbus'"
c6 = "OMXPLAYER_DBUS_PID='/tmp/omxplayerdbus.pid'"
c7 = "export DBUS_SESSION_BUS_ADDRESS=`cat $OMXPLAYER_DBUS_ADDR`"
c8 = "export DBUS_SESSION_BUS_PID=`cat $OMXPLAYER_DBUS_PID`"

c10 ="export OMXPLAYER_LIBS='$OMXPLAYER_LIBS:/usr/lib/omxplayer'"
c9 = "export LD_LIBRARY_PATH='$OMXPLAYER_LIBS${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}'" 

lay=10000

# media file to open
file="/home/pi/4.mp4"
file2="/home/pi/3.mp4"
file3="/home/pi/2.mp4"

Popen([c5],shell=True)
Popen([c6],shell=True)
#Popen([c7],shell=True)
#Popen([c8],shell=True)


Popen([c9],shell=True)
Popen([c10],shell=True)


# open omxplayer



dbusa ="com.gg.com1"+str(lay)
dbusb="com.gg.com2"+str(lay-2)
dbusc="com.gg.com3"+str(lay-4)

cmd = "omxplayer.bin --no-keys  --layer %s  --no-osd --dbus_name %s  %s"  %(lay,dbusa,file)
cmd2 = "omxplayer.bin  --no-keys --layer %s   --no-osd --dbus_name %s   %s" %(lay-2,dbusb,file2)

cmd3 = "omxplayer.bin  --no-keys --layer %s  --no-osd --dbus_name %s   %s" %(lay-4,dbusc,file3)

Popen([cmd], shell=True)
#Popen([cmd2], shell=True)

# wait for omxplayer to initialise
done,retry=0,0
while done==0:
    try:
        with open('/tmp/omxplayerdbus', 'r+') as f:
            omxplayerdbus = f.read().strip()
        bus = dbus.bus.BusConnection(omxplayerdbus)
        done=1
    except:
        retry+=1
        if retry >= 500:
            print retry
            print "ERROR"
            raise SystemExit

time.sleep(2)
second =0
print "step1a"
while 1:
    done=0
    retry2=0
    while done==0:
        try:
            object = bus.get_object(dbusa,'/org/mpris/MediaPlayer2', introspect=False)
            done=1
        except:
            retry2+=1
            if retry2 >= 500:
                print "error q1"
                raise SystemExit
       
    dbusIfaceProp = dbus.Interface(object,'org.freedesktop.DBus.Properties')
    dbusIfaceKey = dbus.Interface(object,'org.mpris.MediaPlayer2.Player')
    print "step2"
    

    if second==1:
        print "step inside 1"
        dbusIfaceKey.Action(dbus.Int32("16")) 
        dur4 = dbusIfaceProp3.Duration()
        pos4 = dbusIfaceProp3.Position()  
        while pos4<dur4-1000000:
            pos4=dbusIfaceProp3.Position()
            #print pos4
        dbusIfaceKey.Action(dbus.Int32("16"))

    
    time.sleep(1)  
    print "here we go again"      

    dur=dbusIfaceProp.Duration()
    print dur

    print dbusIfaceProp.Position()

    pos = dbusIfaceProp.Position()
    #while pos<dur-1000000:
    #    pos=dbusIfaceProp.Position()
    #    print pos

    #ctypes.CDLL('libbcm_host.so').bcm_host_init()
    Popen([cmd2], shell=True)

    time.sleep(1)
    #object2 = bus.get_object('com.gg.com2','/org/mpris/MediaPlayer2', introspect=False)

    ret0=0
    done2=0
    while done2==0:
        try:
            object2 = bus.get_object(dbusb,'/org/mpris/MediaPlayer2', introspect=False)
            done2=1
        except:
            ret0+=1
            if ret0 >= 500:
                print "error q2"
                raise SystemExit

    dbusIfaceProp2 = dbus.Interface(object2,'org.freedesktop.DBus.Properties')
    dbusIfaceKey2 = dbus.Interface(object2,'org.mpris.MediaPlayer2.Player')

    #time.sleep(1)
    dbusIfaceKey2.Action(dbus.Int32("16"))
    print "sleeping"


    while pos<dur-1000000:
        pos=dbusIfaceProp.Position()
        #print pos

    #time.sleep(5) 
    print "waking" 
    #ctypes.CDLL('libbcm_host.so').bcm_host_init()
    dbusIfaceKey2.Action(dbus.Int32("16"))

    #ctypes.CDLL('libbcm_host.so').bcm_host_init()
    Popen([cmd3], shell=True)
    time.sleep(1)

    #object3 = bus.get_object('com.gg.com3','/org/mpris/MediaPlayer2', introspect=False)


    ret00=0
    done20=0
    while done20==0:
        try:
            object3 = bus.get_object(dbusc,'/org/mpris/MediaPlayer2', introspect=False)
            done20=1
        except:
            ret00+=1
            if ret00 >= 500:
                print "error q3"
                raise SystemExit




    dbusIfaceProp3 = dbus.Interface(object3,'org.freedesktop.DBus.Properties')
    dbusIfaceKey3 = dbus.Interface(object3,'org.mpris.MediaPlayer2.Player')
    #time.sleep(1)
    dbusIfaceKey3.Action(dbus.Int32("16"))
    print "sleeping"



    dur3 = dbusIfaceProp2.Duration()
    pos3 = dbusIfaceProp2.Position()
    while pos3<dur3-1000000:
        pos3=dbusIfaceProp2.Position()
        #print pos3


    print "waking"
    #ctypes.CDLL('libbcm_host.so').bcm_host_init()
    dbusIfaceKey3.Action(dbus.Int32("16"))

    if lay < 100:
        lay = 10000

 
    lay=lay - 5
    # open omxplayer



    dbusa ="com.gg.com1"+str(lay)
    dbusb="com.gg.com2"+str(lay-2)
    dbusc="com.gg.com3"+str(lay-4)

    cmd = "omxplayer.bin --no-keys --layer %s   --no-osd --dbus_name %s  %s"  %(lay,dbusa,file)
    cmd2 = "omxplayer.bin  --no-keys --layer %s   --no-osd --dbus_name %s   %s" %(lay-2,dbusb,file2)
    cmd3 = "omxplayer.bin  --no-keys --layer %s  --no-osd --dbus_name %s   %s" %(lay-4,dbusc,file3)

    #cmd = "omxplayer.bin --layer %s  -g --no-osd --dbus_name com.gg.com1%s  %s"  %(lay,lay,file)
    #cmd2 = "omxplayer.bin  --layer %s   -g --no-osd --dbus_name com.gg.com2%s   %s" %(lay-2,lay-2,file2)
    #cmd3 = "omxplayer.bin  --layer %s  -g --no-osd --dbus_name com.gg.com3%s   %s" %(lay-4,lay-4,file3)





    #ctypes.CDLL('libbcm_host.so').bcm_host_init()
    Popen([cmd], shell=True)
    time.sleep(1)
    second=1
    #lay=lay - 5
    # open omxplayer
    #cmd = "omxplayer.bin --layer %s  -g --no-osd --dbus_name com.gg.com1  %s"  %(lay,file)
    #cmd2 = "omxplayer.bin  --layer %s   -g --no-osd --dbus_name com.gg.com2   %s" %(lay-2,file2)

    #cmd3 = "omxplayer.bin  --layer %s  -g --no-osd --dbus_name com.gg.com3   %s" %(lay-4,file3)




#dbusIfaceKey.Action(dbus.Int32("16"))
#dbusIfaceKey2.Action(dbus.Int32("16"))

#time.sleep(5)
#dbusIfaceKey.Action(dbus.Int32("16"))
#time.sleep(5)
#dbusIfaceKey2.Action(dbus.Int32("16"))



# property: print duration of file
#print dbusIfaceProp.Duration()

# key: pause after 5 seconds
#time.sleep(5)
#dbusIfaceKey.Action(dbus.Int32("28"))

# key: un-pause after 5 seconds
#time.sleep(5)
#dbusIfaceKey.Action(dbus.Int32("29"))

# key: quit after 5 seconds
#time.sleep(5)
#dbusIfaceKey.Action(dbus.Int32("15"))
