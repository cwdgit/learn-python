#!/usr/bin/python
name='swaroop'
if name.startswith('swa'):
   print 'yes,the string starts with "swa"'
if 'a' in name:
   print 'yes,it contains the string "a"'
if name.find('war')!= -1:
   print 'yes,it contains the string "war"'

delimiter='_*_'
mylist=['brazil','russia','india','chian']
print delimiter.join(mylist)

