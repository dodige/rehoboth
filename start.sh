cd /home/pi/PiModules/code/python/package
python ./setup.py install

cd /home/pi/PiModules/code/python/upspico/picofssd
##RUN RUN chmod +x ./setup.py
python ./setup.py install
update-rc.d picofssd defaults
update-rc.d picofssd enable

sudo /etc/init.d/cron restart

./om2.py

# sleep 30

# ./net_tester
