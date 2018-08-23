#!/usr/bin/python
class schoolmember:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print '(initialized schoolmember:%s)'%self.name

    def tell(self):
        print 'name:%s age:%s'%(self.name,self.age),

class teacher(schoolmember):
    def __init__(self,name,age,salary):
        schoolmember.__init__(self,name,age)
        self.salary=salary
        print '(initialized teacher:%s)' %self.name,

    def tell(self):
        schoolmember.tell(self)
        print 'salary: %d'%self.salary

class student(schoolmember):
    def __init__(self,name,age,marks):
       schoolmember.__init__(self,name,age)
       self.marks=marks
       print '(initialized student:%s)'%self.name,

    def tell(self):
        schoolmember.tell(self)
        print 'marks:%d'%self.marks

t=teacher('Mrs.Shrividya',40,30000)
t.tell()
s=student('swaroop',22,75)
s.tell()
