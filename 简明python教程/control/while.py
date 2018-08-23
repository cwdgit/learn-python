#!/usr/bin/python
#filename:while.py
number=23
running=True
while running:
  guess=int(raw_input('please input a number '))
  if guess == number:
     print 'congratulations, you guessed it'
     running=False
  elif guess < number:
     print 'no it is lower'
  else:
     print 'no it is higher'

else:
   print 'The while loop is over'


print 'Done'
