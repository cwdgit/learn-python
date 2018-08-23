#!/usr/bin/python
ab= {'swaroop':'swaroopch@byteofpython.info','larry':'larry@wall.org','matsumoto':'matz@ruby-lang.org','spammer':'spammer@hotmail.com'}

ab['Guido']='guido@python.org'
print ab

del ab['spammer']
print '\nThere are %d contact in the address-book\n' %len(ab)

for name,address in ab.items():
    print 'contact %s at %s' %(name,address)

if 'Guido' in ab: 
    print "\nGuido's address is %s" %ab['Guido']
