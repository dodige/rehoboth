
./om2.py

sleep 90

pppd call gprs&

/sbin/ip route add default dev ppp0
