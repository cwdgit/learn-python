#!/usr/bin/python
import sys
def readfile(filename):
    '''print a file to the standard output'''
    f=file(filename)
    while True:
      line = f.readline()
      if len(line) == 0:
         break
      print line,
    f.close()

if len(sys.argv) < 2:
   print 'No action specified.'
   sys.exit()
if sys.argv[1].startswith('--'):
   option=sys.argv[1][2:]

   if option == 'version':
      print 'version1.2'
   elif option == 'help':
      print ''' This program prints files to the standard output.
            any number of files can be specified.
            options include:
            --version: prints the version number
            --help: display this help'''
   else:
      print 'unknown option.'
   sys.exit()

else:
    for filename in sys.argv[1:]:
        readfile(filename)
 
      

