#!/usr/bin/python

from generateHTML import GenerateHTML

htmlGenerator = GenerateHTML()
htmlGenerator.generateProjectsList()
htmlGenerator.buildMainSite()
htmlGenerator.generatePagesForProjects()
