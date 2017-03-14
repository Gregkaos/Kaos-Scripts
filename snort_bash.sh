/usr/local/bin/pulledpork.pl -c /etc/snort/pulledpork.conf -T -l -i /etc/snort/disablesid.conf -h /var/log/sid_changes.log -I Balanced
pid=$(ps -ef | grep snort | grep -v grep | awk '{print $2}')
kill -SIGHUP $pid
grep Begin /var/log/sid_changes.log  | tail -1 > /usr/src/updates.txt
tail -n +$(( 1 + $(grep -m1 -n -f /usr/src/updates.txt /var/log/sid_changes.log | cut -d: -f1) )) /var/log/sid_changes.log >> /usr/src/updates.txt
python /etc/snort/snort_logs.py

echo 'This script will update snort rules and email logs if snort_logs.py is available' 
