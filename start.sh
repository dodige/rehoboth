
./om2.py

sleep 90

pppd call gprs&

sleep 30

/sbin/ip route add default dev ppp0
