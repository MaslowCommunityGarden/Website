#!/usr/bin/python

from generateHTML import GenerateHTML

htmlGenerator = GenerateHTML()
htmlGenerator.generateProjectsList()
htmlGenerator.sortProjects()
htmlGenerator.buildMainSite()
htmlGenerator.generatePagesForProjects()
