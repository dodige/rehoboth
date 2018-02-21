__author__ = 'donald'
print "Hello Word"
print "Hello Word2"

import xml.etree.ElementTree as ET
import croniter
from croniter import croniter
from datetime import datetime, timedelta


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


print playlistTable

print datetime.today()

print datetime.now()

#base = datetime(datetime.year,datetime.month,datetime.day,datetime.hour,0)
#base = datetime(2014, 8, 8, 4, 46)

iter = croniter('*/5 * * * *', datetime.now())  # every 5 minites

print iter.get_next(datetime)   # 2010-01-25 04:50:00
print iter.get_next(datetime)   # 2010-01-25 04:55:00
print iter.get_next(datetime)   # 2010-01-25 05:00:00


