# Community Garden Website

This is the code which generates the Maslow Community Garden website which you are most likely reading. Meta right?


The community garden exists as a place to help facilitate collaborative open source projects.

The garden is a project of the [Maslow CNC](https://www.maslowcnc.com) community. Everyone is welcome and pull requests to improve the site are appreciated.

Every five minutes the website is automatically generated from a list of tracked Github repositories. The website is generated from a python script.

You can build your own version of the site by running the python script `python buildSite.py` the home page will be index.html. This can also be a good way to test any proposed changes to the design of the site.

The order in which the projects are displayed on the page is based on the number of stars that the project has received on GitHub. The more stars the closer to the top of the page the project will appear.

You can link directly to the instructions tab of any project page by adding the text ?instructions=true to the end of the link URL for example: http://maslowcommunitygarden.org/Website.html?instructions=true will take you to the instructions tab for this project.
