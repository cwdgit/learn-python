#!/usr/bin/python
class shortinputexception(exception):
   def __init__(self,length,atleast):
       exception.__init__(self)
       self.length=length
       self.atleast=atleast

try:
   s = raw_input('enter something-->')
   if len(s) < 3:
      raise shortinputexception(len(s),3)
except EOFError:
   print '\nWhy did you do an EOF on me?'

except shortinputexception,x:
   print 'shortinputexception: the input was of length %d, was expecting at least %d' %(x.length,x.atleast)
   else:
      print 'No exception was raised.'
   
