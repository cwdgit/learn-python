#!/usr/bin/python
class person:
   '''represents a person. '''
   population = 0
   def __init__(self,name):
       self.name=name
       print '(initializing %s)' %self.name
       person.population += 1

   def __del__(self):
       '''I am dying.'''
       print '%s says bye.' %self.name
       person.population -= 1
       if person.population ==0:
          print 'I am the last one.'

       else:
          print 'There are still %d people left.' %person.population

   def sayhi(self):
       '''greeting by the person.'''
       print 'Hi, my name is %s.' %self.name
    
   def howmany(self):
        '''prints the current population.'''
        if person.population == 1:
           print 'I am the only person here.'

        else:
           print 'we have %d persons here.' %person.population

swaroop = person('swaroop')
swaroop.sayhi()
swaroop.howmany()

kalam=person('abdul kalam')     
kalam.sayhi()
kalam.howmany()

swaroop.sayhi()
swaroop.howmany()
       
