#!/usr/bin/python
number=23
guess=int(raw_input("please input a number"))
if number==guess:
   print 'congratulations,you guessed it.'
elif number < guess:
   print 'no, your number is higher than that'
else:
   print 'no, your number is lower than that'

print 'Done'
