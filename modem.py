
#!/usr/bin/python
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details:
#
# Copyright (C) 2009 Novell, Inc.
#

# An example on how to send an SMS message using ModemManager

import sys
import dbus
import time
from subprocess import Popen

c1 = "export DBUS_SYSTEM_BUS_ADDRESS='unix:path=/host/run/dbus/system_bus_socket'"
Popen([c1],shell=True)


#if len(sys.argv) != 3:
#    print "Usage: %s <number> <message>" % sys.argv[0]
#    sys.exit(1)

#number = sys.argv[1]
#message = sys.argv[2]

bus = dbus.SystemBus()

manager_proxy = bus.get_object('org.freedesktop.ModemManager1', '/org/freedesktop/ModemManager1')
manager_iface = dbus.Interface(manager_proxy, dbus_interface='org.freedesktop.ModemManager1')

manager_iface.ScanDevices()
time.sleep(10)

#modems = manager_iface.EnumerateDevices()
#if len(modems) == 0:
#    print "No modems found"
#    sys.exit(1)

om = dbus.Interface(manager_proxy, "org.freedesktop.DBus.ObjectManager")

states = { 10: "Connecting", 11: "Connected" }

modems = om.GetManagedObjects()
for mpath in modems.keys():
    modem_state = modems[mpath]['org.freedesktop.ModemManager1.Modem']['State']
    try:
        state = states[modem_state]
    except KeyError:
        state = "Not connected"
    print "Modem object path: " + mpath + "  (" + state + ")"


