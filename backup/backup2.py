#!/usr/bin/python
#filename:backup2.py
import os
import time
file = ['/home/swaroop/byte','/home/swaroop/bin']
target_dir= '/mnt/backup/'
today = target_dir+time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
   os.mkdir(today)
   print 'successfully created directory',today

target = today + os.sep + now + '.zip'
zip_command = "zip -qr %s %s"%(target, ' '.join(file))

if os.system(zip_command) == 0:
   print 'successful backup to', target
else:
   print 'backup failed'
