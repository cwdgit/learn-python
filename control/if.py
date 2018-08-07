#!/usr/bin/python
#filename:if.py
number=23
guess=int(raw_input('please input a number'))
if guess == number:
   print 'congratulations, you guessed it'
elif guess > number:
   print 'no it is higher'
else:
   print 'no it is lower'



print 'Done'
