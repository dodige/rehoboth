#!/usr/bin/env python

import dbus, time, sys, os
from subprocess import Popen

import ctypes

import xml.etree.ElementTree as ET
import croniter
from croniter import croniter
from datetime import datetime, timedelta



def reloadPlaylist(playlistTable, playlist_len):
    period_tree = ET.parse('period.xml')
    period_root = period_tree.getroot()
    print period_root.tag
    print period_root.attrib

    duration = 5
    for child in period_root:
        print child.tag, child.attrib, child.text
        if child.tag == "duration":
            print "duration"
            duration = int(child.text)
            print duration


    playlist_tree = ET.parse('playlist.xml')
    playlist_root = playlist_tree.getroot()
    print playlist_root.tag
    print playlist_root.attrib

    i=0
    currentDate = datetime.now()
    maxDate = currentDate + timedelta(minutes=duration)
    print "maxDate=", maxDate

    playlistTable =[["" for y in xrange(10)] for x in xrange(100)]
    for item in playlist_root.findall('video'):
        print item.tag, item.attrib, item.find('filename').text, item.find('duration').text, item.find('schedule').text, item.find('url').text, item.find('local_url').text
        iter1 = croniter(item.find('schedule').text,currentDate)
        #checkif  video next date is lower than (current time  + period) and higher than curent time
        next_play = iter1.get_next(datetime)
        if next_play < maxDate :
            print next_play
            print "pp"
            playlistTable[i][0] = item.find('filename').text
            playlistTable[i][1] = item.find('duration').text
            playlistTable[i][2] = item.find('schedule').text
            playlistTable[i][3] = item.find('url').text
            playlistTable[i][4] = item.find('local_url').text
            playlistTable[i][5] = item.get('time_played')
            playlistTable[i][6] = item.get('priority')
            i += 1

    playlist_len = i
    print playlistTable

    pass



period_tree = ET.parse('period.xml')
period_root = period_tree.getroot()
print period_root.tag
print period_root.attrib

duration = 5
for child in period_root:
    print child.tag, child.attrib, child.text
    if child.tag == "duration":
        print "duration"
        duration = int(child.text)
        print duration


playlist_tree = ET.parse('playlist.xml')
playlist_root = playlist_tree.getroot()
print playlist_root.tag
print playlist_root.attrib

i=0
currentDate = datetime.now()
maxDate = currentDate + timedelta(minutes=duration)
print "maxDate=", maxDate

playlistTable =[["" for y in xrange(10)] for x in xrange(100)]
#playlistTable =[[] ]

def getKeyp(itemx):
    #int(itemx.get('time_played'))
    print itemx.get('time_played')
    #int(itemx.get('priority'))
    print itemx.get('priority')
    print "jjjjjjjjjjj"
    return  (int(itemx.get('priority')), int(itemx.get('time_played')))

print "!!!!!!!!!!!!!"
print "ll"
hh = playlist_root.findall('video')
print
hh [:] = sorted(hh, key=getKeyp)
print "!!!!!!!!!!!!!"

#for item in playlist_root.findall('video'):
for item in sorted(playlist_root.findall('video'), key=getKeyp):
    print item.tag, item.attrib, item.find('filename').text, item.find('duration').text, item.find('schedule').text, item.find('url').text, item.find('local_url').text
    iter1 = croniter(item.find('schedule').text,currentDate)
    #checkif  video next date is lower than (current time  + period) and higher than curent time
    next_play = iter1.get_next(datetime)
    if next_play < maxDate :
        print next_play
        print "pp"
        playlistTable[i][0] = item.find('filename').text
        playlistTable[i][1] = item.find('duration').text
        playlistTable[i][2] = item.find('schedule').text
        playlistTable[i][3] = item.find('url').text
        playlistTable[i][4] = item.find('local_url').text
        playlistTable[i][5] = item.get('time_played')
        playlistTable[i][6] = item.get('priority')
        i += 1

playlist_len = i


print playlistTable


def playlist_order(playlisteTable):

    pass



#playlistTable = sorted(playlistTable,key=playlist_order)
#playlistTable.sort();
print "after sort 1 "
print playlistTable


print datetime.today()

print datetime.now()

#base = datetime(datetime.year,datetime.month,datetime.day,datetime.hour,0)
#base = datetime(2014, 8, 8, 4, 46)

iter = croniter('*/5 * * * *', datetime.now())  # every 5 minites

print iter.get_next(datetime)   # 2010-01-25 04:50:00
print iter.get_next(datetime)   # 2010-01-25 04:55:00
print iter.get_next(datetime)   # 2010-01-25 05:00:00

print "environnmnent set up"

c0 = "/home/pi/local_env.sh"
c1 = "OMXPLAYER_DBUS_ADDR = '/tmp/omxplayerdbus.pi' "
c2 = "OMXPLAYER_DBUS_PID = '/tmp/omxplayerdbus.pi.pid'"
c3 = "export DBUS_SESSION_BUS_ADRESS = 'cat $OMXPLAYER_DDUS_ADDR'"
c4 = "export DBUS_SESSION_BUS_PID = 'cat $OMXPLAYER_DBUS_PID'"

#if os.fork() == 0:
ctypes.CDLL('libbcm_host.so').bcm_host_init()

print "host init done"

OMXPLAYER='/usr/bin/omxplayer'
OMXPLAYER_LIB_PATH='/opt/vc/lib:/usr/lib/omxplayer'
LOCAL_LIB_PATH='/usr/local/lib'

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(LOCAL_LIB_PATH)
os.environ['LD_LIBRARY_PATH'] = OMXPLAYER_LIB_PATH

print " env1 "

c5 = "OMXPLAYER_DBUS_ADDR='/tmp/omxplayerdbus.root'"
c6 = "OMXPLAYER_DBUS_PID='/tmp/omxplayerdbus.root.pid'"
c7 = "export DBUS_SESSION_BUS_ADDRESS=`cat $OMXPLAYER_DBUS_ADDR`"
c8 = "export DBUS_SESSION_BUS_PID=`cat $OMXPLAYER_DBUS_PID`"

c10 ="export OMXPLAYER_LIBS='$OMXPLAYER_LIBS:/usr/lib/omxplayer'"
c9 = "export LD_LIBRARY_PATH='$OMXPLAYER_LIBS${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}'" 

lay=10000

# media file to open
file="/home/pi/4.mp4"
file2="/home/pi/3.mp4"
file3="/home/pi/2.mp4"

print "env2 "

Popen([c5],shell=True)
Popen([c6],shell=True)
Popen([c0],shell=True)
Popen([c7],shell=True)
Popen([c8],shell=True)


print "env3"
#Popen([c0],shell=True)

Popen([c9],shell=True)
Popen([c10],shell=True)


# open omxplayer

print "starting players"

dbusa ="com.gg.com1"+str(lay)
dbusb="com.gg.com2"+str(lay-2)
dbusc="com.gg.com3"+str(lay-4)

#cmd = "omxplayer.bin --no-keys  --layer %s  --no-osd --dbus_name %s  %s"  %(lay,dbusa,file)
cmd = "omxplayer --no-keys  --layer %s  --no-osd --dbus_name %s  %s"  %(lay,dbusa,playlistTable[0][0])


#cmd2 = "omxplayer.bin  --no-keys --layer %s   --no-osd --dbus_name %s   %s" %(lay-2,dbusb,file2)
cmd2 = "omxplayer  --no-keys --layer %s   --no-osd --dbus_name %s   %s" %(lay-2,dbusb,playlistTable[1][0])


#cmd3 = "omxplayer.bin  --no-keys --layer %s  --no-osd --dbus_name %s   %s" %(lay-4,dbusc,file3)
cmd3 = "omxplayer  --no-keys --layer %s  --no-osd --dbus_name %s   %s" %(lay-4,dbusc,playlistTable[2][0])


for videoItem in playlist_root.findall('video'):
    if videoItem.find('filename').text == playlistTable[0][0]:
        videoItem.set("time_played", str(int(videoItem.get("time_played"))+1))
        d1 = videoItem.find("duration")
    if videoItem.find('filename').text == playlistTable[1][0]:
        videoItem.set("time_played", str(int(videoItem.get("time_played"))+1))
        d2 = videoItem.find("duration")
    if videoItem.find('filename').text == playlistTable[2][0]:
        videoItem.set("time_played", str(int(videoItem.get("time_played"))+1))
        d3 = videoItem.find("duration")

#print videoItem


Popen([cmd], shell=True)
#Popen([cmd2], shell=True)

# wait for omxplayer to initialise
done,retry=0,0
while done==0:
    try:
        with open('/tmp/omxplayerdbus.root', 'r+') as f:
            omxplayerdbus = f.read().strip()
        bus = dbus.bus.BusConnection(omxplayerdbus)
        done=1
    except:
        retry+=1
        if retry >= 500:
            print retry
            print "ERROR"
            raise SystemExit

time.sleep(1)
second =0
print "step1a"


if playlist_len > 3:
    ind = 3
else:
    ind = 0


totaldur = 0
#main loop
while 1:
    done=0
    retry2=0
    while done==0:
        try:
            time.sleep(1)
            object = bus.get_object(dbusa,'/org/mpris/MediaPlayer2', introspect=False)
            done=1
        except:
            retry2+=1
            if retry2 >500:
                
                print "error q1"
                raise SystemExit
       
    dbusIfaceProp = dbus.Interface(object,'org.freedesktop.DBus.Properties')
    dbusIfaceKey = dbus.Interface(object,'org.mpris.MediaPlayer2.Player')
    print "step2"
    

    if second==1:
        print "step inside 1"
        dbusIfaceKey.Action(dbus.Int32("16")) 
        dur4 = dbusIfaceProp3.Duration()
        d3.text = str(dur4/500000)
        totaldur += dur4
        print "totalduration:"
        print totaldur
        pos4 = dbusIfaceProp3.Position()
        while pos4<=dur4-500000:
            pos4=dbusIfaceProp3.Position()
            #print pos4
            if pos4 == 0:
                break
        dbusIfaceKey.Action(dbus.Int32("16"))

    
   # time.sleep(1)  
    print "here we go again"      

    dur=dbusIfaceProp.Duration()
    d1.text = str(dur/500000)
    totaldur += dur
    print dur
    print "totalduration:"
    print totaldur

    print dbusIfaceProp.Position()

    pos = dbusIfaceProp.Position()
    #while pos<dur-500000:
    #    pos=dbusIfaceProp.Position()
    #    print pos

    #ctypes.CDLL('libbcm_host.so').bcm_host_init()
    Popen([cmd2], shell=True)

   # time.sleep(1)
    #object2 = bus.get_object('com.gg.com2','/org/mpris/MediaPlayer2', introspect=False)
    #playlist_root.findall("filename")




    ret0=0
    done2=0
    while done2==0:
        try:
            time.sleep(1)
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
    print "sleeping_"


    while pos<=dur-500000:
        pos=dbusIfaceProp.Position()
        #print pos
        if pos == 0:
            break

    #time.sleep(1) 
    print "waking" 
    #ctypes.CDLL('libbcm_host.so').bcm_host_init()
    dbusIfaceKey2.Action(dbus.Int32("16"))

    #ctypes.CDLL('libbcm_host.so').bcm_host_init()
    Popen([cmd3], shell=True)
   # time.sleep(1)

    #object3 = bus.get_object('com.gg.com3','/org/mpris/MediaPlayer2', introspect=False)


    ret00=0
    done20=0
    while done20==0:
        try:
           time.sleep(1)
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
    d2.text = str(dur3/500000)
    totaldur += dur3
    print "totalduration:"
    print totaldur
    pos3 = dbusIfaceProp2.Position()
    while pos3<=dur3-500000:
        pos3=dbusIfaceProp2.Position()
        #print pos3
        if pos3 == 0:
            break


    print "waking"
    #ctypes.CDLL('libbcm_host.so').bcm_host_init()
    dbusIfaceKey3.Action(dbus.Int32("16"))

    if lay < 100:
        lay = 10000

 
    lay=lay - 5
    # open omxplayer

    reloadFlag = 0

    if ind < playlist_len:
        ind1 = ind
    else:
        ind = 0
        ind1= 0
        reloadFlag = 1


    if ind+1 < playlist_len:
        ind2= ind+1
    else:
        ind = -1
        ind2 = 0
        reloadFlag = 1


    if ind+2 < playlist_len:
        ind3= ind+2
    else:
        ind = 0
        ind3 = 0
        reloadFlag = 1


    #if reloadFlag ==1 :
    #    reloadPlaylist(playlistTable,playlist_len)

    if totaldur > duration*60000000:
        print "*********************  duration timeexpired  ********************************************* "
        reloadFlag = 1
        totaldur = 0
        ind = 0



    dbusa ="com.gg.com1"+str(lay)
    dbusb="com.gg.com2"+str(lay-2)
    dbusc="com.gg.com3"+str(lay-4)

    cmd = "omxplayer --no-keys --layer %s   --no-osd --dbus_name %s  %s"  %(lay,dbusa,playlistTable[ind1][0])
    cmd2 = "omxplayer  --no-keys --layer %s   --no-osd --dbus_name %s   %s" %(lay-2,dbusb,playlistTable[ind2][0])
    cmd3 = "omxplayer  --no-keys --layer %s  --no-osd --dbus_name %s   %s" %(lay-4,dbusc,playlistTable[ind3][0])

    for videoItem in playlist_root.findall('video'):
        if videoItem.find('filename').text == playlistTable[ind1][0]:
            videoItem.set("time_played", str(int(videoItem.get("time_played"))+1))
            d1 = videoItem.find("duration")
        if videoItem.find('filename').text == playlistTable[ind2][0]:
            videoItem.set("time_played", str(int(videoItem.get("time_played"))+1))
            d2 = videoItem.find("duration")
        if videoItem.find('filename').text == playlistTable[ind3][0]:
            videoItem.set("time_played", str(int(videoItem.get("time_played"))+1))
            d3 = videoItem.find("duration")
        #print videoItem






    print "next 3 files:"
    print playlistTable[ind1][0]
    print playlistTable[ind2][0]
    print playlistTable[ind3][0]

    ind = ind + 3
    if reloadFlag ==1 :


        #d1.text  = str(dur)
        #d2.text  = str(dur3)
        #d3.text  = str(dur4)



        #reloadPlaylist(playlistTable,playlist_len)
        #playlist_tree.write("playlist.xml")
        ind = 0
        print "reloading list"
        period_tree = ET.parse('period.xml')
        period_root = period_tree.getroot()
        #print period_root.tag
        #print period_root.attrib

        duration = 5
        for child in period_root:
            #print child.tag, child.attrib, child.text
            if child.tag == "duration":
                #print "duration"
                duration = int(child.text)
                #print duration


        version_cur=0
        for item in playlist_root.findall('version'):
            print item.text
            version_cur = float(item.text)


        playlist_tree_temp  = ET.parse('playlist.xml')
        playlist_root_temp  = playlist_tree_temp.getroot()
        for item in playlist_root_temp.findall('version'):
            print item.text
            if float(item.text) != version_cur:
                playlist_root = playlist_tree_temp.getroot()
                playlist_tree = playlist_tree_temp
                print "new version"
            else:
                playlist_tree.write("playlist.xml")
                playlist_root = playlist_tree.getroot()
                print "old version"



        #print playlist_root.tag
        #print playlist_root.attrib

        i=0
        # currentDate = datetime.now()
        maxDate = currentDate + timedelta(minutes=duration)
        #print "maxDate=", maxDate

        playlistTable =[["" for y in xrange(10)] for x in xrange(100)]
        #playlistTable =[[] ]

        #for item in playlist_root.findall('video'):
        for item in sorted(playlist_root.findall('video'), key=getKeyp):
            #print item.tag, item.attrib, item.find('filename').text, item.find('duration').text, item.find('schedule').text, item.find('url').text, item.find('local_url').text
            iter1 = croniter(item.find('schedule').text,currentDate)
            #checkif  video next date is lower than (current time  + period) and higher than curent time
            next_play = iter1.get_next(datetime)
            if next_play < maxDate :
                #print next_play
                #print "pp"
                playlistTable[i][0] = item.find('filename').text
                playlistTable[i][1] = item.find('duration').text
                playlistTable[i][2] = item.find('schedule').text
                playlistTable[i][3] = item.find('url').text
                playlistTable[i][4] = item.find('local_url').text
                playlistTable[i][5] = item.get('time_played')
                playlistTable[i][6] = item.get('priority')
                i += 1

        playlist_len = i
        print playlistTable

        #playlistTable.sort();
        print "after sort 2"
        print playlistTable







    print "futur next 3 files:"
    print playlistTable[ind1][0]
    print playlistTable[ind2][0]
    print playlistTable[ind3][0]



    #cmd = "omxplayer.bin --layer %s  -g --no-osd --dbus_name com.gg.com1%s  %s"  %(lay,lay,file)
    #cmd2 = "omxplayer.bin  --layer %s   -g --no-osd --dbus_name com.gg.com2%s   %s" %(lay-2,lay-2,file2)
    #cmd3 = "omxplayer.bin  --layer %s  -g --no-osd --dbus_name com.gg.com3%s   %s" %(lay-4,lay-4,file3)





    #ctypes.CDLL('libbcm_host.so').bcm_host_init()
    Popen([cmd], shell=True)
   # time.sleep(1)
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
