#!/usr/bin/python
#filename:objvar.py
class Person:
	'''Represetns a person.'''
	population=0

	def __init__(self,name):
		'''Initializes the person.'''
		self.name=name
		print '(Initializes%s)'%self.name
		Person.population+=1
                print Person.population
        def __del__(self):
                '''I am dying.'''
                print '%s says bye.'%self.name
                Person.population-=1
                if Person.population ==0:
                   print 'I am the last one.'
                else:
                   print 'There are still %d people left.'%Person.population
           
        def sayHi(self):
                '''Greeting by the person.'''
                print 'Hi,my name is %s.' %self.name
        def howMany(self):
                '''Prints the current population.'''
                if Person.population ==1:
                   print 'I am the only person here.'
                else:
                   print 'We have %d persons here.'%Person.population

                  
   
p=Person('swaroop')
p.sayHi()
p.howMany()

b=Person('Abdul Kalam')
b.sayHi()
b.howMany()

p.sayHi()
p.howMany()


