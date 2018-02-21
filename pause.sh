#!/bin/sh


OMXPLAYER_DBUS_ADDR="/tmp/omxplayerdbus"
OMXPLAYER_DBUS_PID="/tmp/omxplayerdbus.pid"
export DBUS_SESSION_BUS_ADDRESS=`cat $OMXPLAYER_DBUS_ADDR`
export DBUS_SESSION_BUS_PID=`cat $OMXPLAYER_DBUS_PID`

[ -z "$DBUS_SESSION_BUS_ADDRESS" ] && { echo "Must have DBUS_SESSION_BUS_ADDRESS" >&2; exit 1; }

dbus-send --session --print-reply --dest=raspberry.pi.OMXPlayer \
    $1  raspberry.pi.OMXPlayer.Pause
