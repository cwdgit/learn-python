#!/usr/bin/python
class person():
   def __init__(self,name):
       self.name=name
   def sayhi(self):
       print 'hello,my name is',self.name

p=person('swaroop')
p.sayhi()

