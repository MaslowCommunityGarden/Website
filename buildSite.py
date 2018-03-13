#!/usr/bin/python

import sys
print(sys.version)

f = open('itRan','w')
f.write(sys.version)
f.close()

from yattag import Doc

import time

'''#!/usr/bin/python





doc, tag, text = Doc().tagtext()

with tag('html'):
    doc.stag('img', src="logo.png", width="1328", height="360")
    with tag('body'):
        with tag('h1'):
            text('The Maslow Community Garden')
        with tag('p'):
            text('This page is a place for community driven open source projects to live')
        
        with tag('p'):
            text('12:18 test')


print "got to the end of the script...almost"

f = open('index.html','w')
f.write(doc.getvalue())
f.close()

print "really got to the end"'''

f = open('index.html','w')
f.write("test")
f.close()