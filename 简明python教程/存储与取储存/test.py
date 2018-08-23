#!/usr/bin/python
#filename:test.py
import cPickle as p
shoplistfile='shoplist.data'
shoplist = ['1','2','3']

#write to the file
f=file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()

del shoplist

f=file(shoplistfile)
storedlist=p.load(f)
print storedlist


