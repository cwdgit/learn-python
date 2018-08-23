#!/usr/bin/python
number=23
running=True
while running:
   guess=int(raw_input('please input a number:'))
   if guess == number:
      print 'congratulations,you guessed it.'
      running=False
   elif guess < number:
      print 'no,your number is too lower'
   else:
      print 'no,your number is too higher'

else:
   print 'The while loop is over.'

print 'Done'
