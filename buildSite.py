#!/usr/bin/python

from yattag import  Doc
import              urllib2  # the lib that handles the url stuff
import              random

#load the currently tracked projects
trackedProjects = open('trackedProjects.txt')
projects = trackedProjects.readlines()
random.shuffle(projects)



#generate the HTML for the site
doc, tag, text = Doc().tagtext()

with tag('html'):
    with tag('head'):
        doc.stag('link',rel='stylesheet', href='styles.css')
    doc.stag('img', src="logo.png", width="664", height="180")
    with tag('body'):
        with tag('h1'):
            text('The Maslow Community Garden')
        with tag('p'):
            text('A place for community driven open source projects to live')
        
        with tag('hr'):
            pass
        
        with tag('a', href="http://example.com", klass="button"):
            text('How does the garden work?')
        
        with tag('a', href="http://example.com", klass="button"):
            text('Add a project')
        
        with tag('hr'):
            pass
        
        #Generate a grid of tracked projects
        
        for project in projects:
            try:
                readmeUrl = project + '/master/README.md'
                readmeUrl = "".join(readmeUrl.split())
                print "readme url: "
                print readmeUrl
                linesInReadme = urllib2.urlopen(readmeUrl)
                
                #this creates a boxed representation of the project
                with tag('a', href="http://example.com"):
                    with tag('div', klass = 'boxed', style="width: 400px; height: 400px; float: left;"):
                        numberOfLinesProcessed = 0
                        maxNumberToProcess = 3
                        for line in linesInReadme: 
                            if line[0] is '#':
                                with tag('h1'):
                                    text(line[1:])
                            elif line[0] is not '!':
                                with tag('p'):
                                    text(line)
                            numberOfLinesProcessed = numberOfLinesProcessed + 1
                            if numberOfLinesProcessed > maxNumberToProcess:
                                break
                        doc.stag('img', src= project + '/master/mainpicture.jpg', width="400", height="180")
            except Exception as e:
                print "\n\n\n\n@#$#@$@"
                print project
                print "could not be read"
                print (e)



f = open('index.html','w')
f.write(doc.getvalue())
f.close()