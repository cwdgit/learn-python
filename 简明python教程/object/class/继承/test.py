#!/usr/bin/python
#filename:test.py
class SchoolMembers:
   def __init__(self,name,age):
       self.name=name
       self.age=age
       print '(Initialized SchoolMember:%s)'%self.name
   def tell(self):
       print 'Name:"%s" Age:"%s"' %(self.name,self.age),

class Teacher(SchoolMembers):
   def __init__(self,name,age,salary):
       SchoolMembers.__init__(self,name,age)
       self.salary=salary
       print '(Initialized Teacher:%s)'%self.name
       
   def tell(self):
       SchoolMembers.tell(self)
       print 'Salary:"%d"'%self.salary

class Student(SchoolMembers):
   def __init__(self,name,age,marks):
       SchoolMembers.__init__(self,name,age)
       self.marks=marks
       print '(Initialized Student:%s)'%self.name

   def tell(self):
       SchoolMembers.tell(self)
       print 'marks:"%d"'%self.marks

t=Teacher('Mrs.Shrividya',40,30000)
t.tell()
s=Student('swaroop',22,75)
s.tell()

