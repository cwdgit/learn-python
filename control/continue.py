#!/usr/bin/python
#filename:continue.py
while True:
   s = raw_input('please input some thing ')
   if s == 'quit':
      break
   if len(s) < 3:
      continue
   print 'Input is of sufficient length' ,len(s)
