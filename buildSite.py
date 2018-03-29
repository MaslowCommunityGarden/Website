#!/usr/bin/python

from generateHTML import GenerateHTML
print "test
htmlGenerator = GenerateHTML()
htmlGenerator.generateProjectsList()
htmlGenerator.buildMainSite()
htmlGenerator.generatePagesForProjects()
