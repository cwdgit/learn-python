#!/usr/bin/python
import os
import time
file=['/home/swaroop/byte','/home/swaroop/bin']
target_dir = '/mnt/backup/'
target = target_dir + time.strftime('%Y%M%d%H%M%S') + '.zip'
zip_command= 'zip -qr %s %s'%(target,' '.join(file))
print zip_command
if os.system(zip_command)==0:
   print 'successful backup to',target
else:
   print 'backup faild'
