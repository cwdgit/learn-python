#!/usr/bin/python
#filename:reference.py
shoplist = ['apple','mango','carrot','banana']
mylist=shoplist
del shoplist[0]
print shoplist[0]
print 'shoplist is',shoplist
print 'mylist is',mylist

test = ['1','2','3']
test1=test[:]
del test[0]
print test
print test1

