#!/usr/bin/python
#filename:using_list.py

shoplist=['apple','mango','carrot','banana']
print shoplist
print 'I have',len(shoplist),'items to purchase.'
print 'These items are: '
for item in shoplist:
    print item,

print '\nI also have to buy rice.'
shoplist.append('rice')
print 'my shopping list is now',shoplist

print 'The first item I will buy is', shoplist[0]
olditem=shoplist[0]
del shoplist[0]
print 'I bought the',olditem
print 'My shopping list is now',shoplist
