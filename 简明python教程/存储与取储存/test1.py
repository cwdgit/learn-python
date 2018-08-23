#!/usr/bin/python
#filename:test3.py
import cPickle as p
shoplistfile='shoplist.data'
shoplist=['2','3','4']
f=file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()
del shoplist
f=file(shoplistfile)
storedlist=p.load(f)
print storedlist

