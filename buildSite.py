#!/usr/bin/python

from yattag import Doc

doc, tag, text = Doc().tagtext()

with tag('html'):
    doc.stag('img', src="logo.png", width="1328", height="360")
    with tag('body'):
        with tag('h1'):
            text('The Maslow Community Garden')
        with tag('p'):
            text('This page is a place for community driven open source projects to live')
        
        with tag('p'):
            text('11:40 test')



f = open('index.html','w')
f.write(doc.getvalue())
f.close()