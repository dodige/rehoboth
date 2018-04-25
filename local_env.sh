DBUS_CMD="dbus-daemon --fork --print-address 5 --print-pid 6 --session"
OMXPLAYER_DBUS_ADDR="/tmp/omxplayerdbus.${USER}"
OMXPLAYER_DBUS_PID="/tmp/omxplayerdbus.${USER}.pid"
#OMXPLAYER_DBUS_ADDR="/tmp/omxplayerdbus"
#OMXPLAYER_DBUS_PID="/tmp/omxplayerdbus.pid"

if [ ! -s "$OMXPLAYER_DBUS_PID" ] || ! pgrep -f "$DBUS_CMD" -F "$OMXPLAYER_DBUS_PID" >/dev/null; then
	#echo "starting dbus for the first time" >&2
	exec 5> "$OMXPLAYER_DBUS_ADDR"
	exec 6> "$OMXPLAYER_DBUS_PID"
	$DBUS_CMD
	until [ -s "$OMXPLAYER_DBUS_ADDR" ]; do
		echo "waiting for dbus address to appear" >&2
		sleep .2
	done
fi

DBUS_SESSION_BUS_ADDRESS=`cat $OMXPLAYER_DBUS_ADDR`
DBUS_SESSION_BUS_PID=`cat $OMXPLAYER_DBUS_PID`

DBUS_SYSTEM_BUS_ADDRESS=`unix:path=/host/run/dbus/system_bus_socket`

export DBUS_SESSION_BUS_ADDRESS
export DBUS_SESSION_BUS_PID

export DBUS_SYSTEM_BUS_ADDRESS
