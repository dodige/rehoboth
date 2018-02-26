
./om2.py

sleep 30

pppd call gprs&

/sbin/ip route add default dev ppp0
