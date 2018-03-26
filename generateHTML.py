from yattag import  Doc
import              urllib2  # the lib that handles the url stuff
import              random
from markdown2      import Markdown
from projectClass   import Project

class GenerateHTML:
    
    projects = []
    
    def generateProjectsList(self):
        '''
        
        This function builds out the self.projects list which contains all 
        of the tracked projects and some basic information about them
        
        '''
        #load the currently tracked projects
        trackedProjects = open('trackedProjects.txt')
        projectStrings = trackedProjects.readlines()
        random.shuffle(projectStrings)
        
        for string in projectStrings:                           #this will iterate through our list of tracked project strings and try to generate a meaningful project object from them
                
            thisProject = Project()
                
            try:
                
                #store the link to the page
                thisProject.projectPath = string
                thisProject.projectPath = thisProject.projectPath.replace('\n', '') #remove the carriage return
                
                #find the download link
                thisProject.downloadLink = thisProject.projectPath + "/archive/master.zip"
                
                
                #find the raw version of the string
                thisProject.projectPathRaw = self.findProjectRawPath(string)
                
                #find the path to the README file
                readmeUrl = thisProject.projectPathRaw + '/master/README.md'
                readmeUrl = "".join(readmeUrl.split())
                thisProject.READMEpath = readmeUrl
                
                #find the path to the Instructions file
                instructionsUrl = thisProject.projectPathRaw + '/master/INSTRUCTIONS.md'
                instructionsUrl = "".join(instructionsUrl.split())
                thisProject.INSTRUCTIONSpath = instructionsUrl
                
                #find the path to the BOM file
                bomUrl = thisProject.projectPathRaw + '/master/BOM.md'
                bomUrl = "".join(bomUrl.split())
                thisProject.BOMpath = bomUrl
                
                #Construct the project object
                thisProject.projectName = self.findProjectName(thisProject.projectPathRaw)
                
                print "Project name set to"
                print thisProject.projectName
                
                thisProject.projectFile = thisProject.projectName + '.html'
                thisProject.mainPicture = thisProject.projectPathRaw + '/master/mainpicture.jpg'
                thisProject.READMEpath  = readmeUrl
                
                thisProject.editREADMEpath      = thisProject.projectPath + '/blob/master/README.md'
                thisProject.editINSTRUCTIONpath = thisProject.projectPath + '/blob/master/INSTRUCTIONS.md'
                thisProject.editBOMpath         = thisProject.projectPath + '/blob/master/BOM.md'
                
                
                #read the README file
                linesInReadme = urllib2.urlopen(readmeUrl)
                thisProject.READMEtext  = linesInReadme.read()
                
                #read the INSTRUCTIONS file
                linesInReadme = urllib2.urlopen(instructionsUrl)
                thisProject.INSTRUCTIONStext  = linesInReadme.read()
                
                #read the BOM file
                linesInReadme = urllib2.urlopen(bomUrl)
                thisProject.BOMtext  = linesInReadme.read()
                
                
                
                
                print "Generating entry for: "
                print thisProject.projectName
                
                self.projects.append(thisProject)
                

            except Exception as e:
                print string
                print "<- could not be read"
                print (e)
    
    def buildMainSite(self):
        '''
        
        This function builds the main website
        
        '''
        
        #generate the HTML for the site
        doc, tag, text = Doc().tagtext()
        
        with tag('html'):
            with tag('head'):
                doc.stag('link',rel='stylesheet', href='styles.css')
                doc.stag('link',rel='stylesheet', type="text/css", href="https://fonts.googleapis.com/css?family=Open+Sans")
                
            with tag('body', klass = 'body'):
            
                with tag('header', klass = 'header'):
                
                    with tag('div', klass = 'inner-header'):
            
                        with tag('a', href = 'index.html', klass='header-logo'):
                        
                            doc.stag('img', src="logo.png", width="auto", height="90")
                        
                        with tag('nav', klass = 'navigation'):
                        
                            with tag('a', href="howdoesthegardenwork.html", klass="button"):
                                text('How does the garden work?')
                            
                            with tag('a', href="addaproject.html", klass="button"):
                                text('Add a project')
                                
                            with tag('a', href="index.html", klass="button"):
                                text('Browse projects')
                                
                with tag('section', klass="content"):
                    
                    with tag('p', klass = 'title'):
                        text('Not ready to use! -- A place for community driven open source projects to live - Not yet ready to use!')
                    
                    #Generate a grid of tracked projects
                    
                    for project in self.projects:
                        
                        print "Generating grid entry for: "
                        print project.projectName
                        
                        
                        #this creates a boxed representation of the project
                        with tag('a', href=project.projectFile, klass = "project_link"):
                            with tag('div', klass = 'boxed'):
                                
                                with tag ('div', klass = 'project-thumbnail'):
                                    doc.stag('img', src= project.mainPicture, klass = "project_img")                                    
                                
                                numberOfLinesProcessed = 0
                                maxNumberToProcess = 3
                                linesInReadme = project.READMEtext.split('\n', 5)
                                
                                for line in linesInReadme:
                                    if len(line) > 0:
                                        if line[0] is '#':
                                            with tag('h1', klass = "boxed_text"):
                                                text(line[1:])
                                                project.projectName = line[1:]
                                        elif line[0] is not '!':
                                            with tag('p', klass = "boxed_text"):
                                                text(line)
                                    numberOfLinesProcessed = numberOfLinesProcessed + 1
                                    if numberOfLinesProcessed > maxNumberToProcess:
                                        break
    
        f = open('index.html','w')
        f.write(doc.getvalue())
        f.close()

    def generatePagesForProjects(self):
        for project in self.projects:
            pageHTML = ""
            print "Generating file: "
            print project.projectFile
            
            markdowner = Markdown(extras=["tables"]) #allows for the conversion of markdown files into html
            
            readmeText          = markdowner.convert(project.READMEtext)
            instructionsText    = markdowner.convert(project.INSTRUCTIONStext)
            bomText             = markdowner.convert(project.BOMtext)
            
            pageHTML = ("<!DOCTYPE html>"
                "<html>"
                    "<head>"
                        "<meta name='viewport' content='width=device-width, initial-scale=1'>"
                        "<link href='styles.css' rel='stylesheet' />"
                        "<link href='https://fonts.googleapis.com/css?family=Open+Sans' type='text/css' rel='stylesheet' />"
                        "<title>" + project.projectName + "</title>"
                    "</head>"
                    "<body>"
                    
                    "<header class = 'header'>"
                        "<div class='inner-header'>"
                            "<a href='index.html'>"
                                "<img src='logo.png' style='width:auto;height:90px;border:0;'>"
                            "</a>"
                            "<nav class='navigation'>"
                                "<a href='howdoesthegardenwork.html' class='nav-link button one-col'>How Does the Garden Work?</a>"
                                "<a href='addaproject.html' class='nav-link button one-col'>Add A Project</a>"
                                "<a href='index.html#projectsSection' class='nav-link button one-col'>Browse Projects</a>"
                            "</nav>"
                        "</div>"
                    "</header>"
                        
                    "<section class = 'content'>"
                        "<div class = 'ProjectName'>"
                            "<h1 class='title'>" + project.projectName + "</h1>"
                        "</div>"
                    
                        "<div class='tab three-col'>"
                            "<button class=\"tablinks\" onclick=\"openTab(event, 'Files')\" id=\"defaultOpen\">Files</button>"
                              "<button class=\"tablinks\" onclick=\"openTab(event, 'Instructions')\">Instructions</button>"
                              "<button class=\"tablinks\" onclick=\"openTab(event, 'Forums')\">Forums</button>"
                              "<button class=\"tablinks\" onclick=\"openTab(event, 'Buy')\">Buy</button>"
                        "</div>"
                        "<div id='Files' class='tabcontent'>"
                            "<div class='tab-title'>"
                                "<h3 class='two-col'>Files</h3>"
                                "<a href=" + project.editREADMEpath + " class = 'edit_this_page_button'>Edit this page</a>"
                            "</div>"
                            "<table>"
                                "<tr>"
                                    "<td class='project_image_area two-col'>"
                                        "<img src=" + project.mainPicture + " class = 'project_page_image'>"
                                    "</td>"
                                    "<td>"
                                        "<a href=" + project.downloadLink + " class = 'button one-col'>Download</a>"
                                        "<a href=" + project.projectPath + " class = 'button one-col' target='_blank'>Source</a>"
                                    "</td>"
                                "</tr>"
                            "</table>"
                            "<div class='three-col'>"
                                + readmeText +
                            "</div>"
                        "</div>"
                        "<div id='Instructions' class='tabcontent'>"
                            "<div class='tab-title'>"
                                "<h3 class='two-col'>Instructions</h3>"
                                "<a href=" + project.editINSTRUCTIONpath + " class = 'edit_this_page_button'>Edit this page</a>"
                            "</div>"
                            "<div class='three-col'>"
                                + instructionsText +
                            "</div>"
                        "</div>"

                        "<div id='Forums' class='tabcontent'>"
                          "<div class='tab-title'>"
                            "<h3 class='three-col'>Forums</h3>"
                          "</div>"
                          "<div id='discourse-comments'>"

                          "<script type='text/javascript'>"
                            "DiscourseEmbed = { discourseUrl: 'https://forums.maslowcnc.com/',"
                                               "discourseEmbedUrl: 'http://maslowcommunitygarden.org/" + project.projectFile + "' };"

                            "(function() {"
                              "var d = document.createElement('script'); d.type = 'text/javascript'; d.async = true;"
                              "d.src = DiscourseEmbed.discourseUrl + 'javascripts/embed.js';"
                              "(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(d);"
                            "})();"
                          "</script>"
                          "</div>"
                        "</div>"

                        "<div id='Buy' class='tabcontent'>"
                            "<div class='tab-title'>"
                                "<h3 class='two-col'>Buy</h3>"
                                "<a href=" + project.editBOMpath + " class = 'edit_this_page_button'>Edit this page</a>"
                            "</div>"
                            
                            "<div class='three-col'>"
                              + bomText +
                           "</div>"   
                        "</div>"

                        "<div class='three-col'>"
                            "<script>"
                            "function openTab(evt, tabName) {"
                                "var i, tabcontent, tablinks;"
                                "tabcontent = document.getElementsByClassName('tabcontent');"
                                "for (i = 0; i < tabcontent.length; i++) {"
                                    "tabcontent[i].style.display = 'none';"
                                "}"
                                "tablinks = document.getElementsByClassName('tablinks');"
                                "for (i = 0; i < tablinks.length; i++) {"
                                    "tablinks[i].className = tablinks[i].className.replace(' active', '');"
                                "}"
                                "document.getElementById(tabName).style.display = 'block';"
                                "evt.currentTarget.className += ' active';"
                            "}"
    
                            "document.getElementById('defaultOpen').click();"
                            "</script>"
                        "</div>"  
                    "</section>"
                    "</body>"
                "</html>")
            
            #Generate and HTML file for the project
            f = open(project.projectFile,'w')
            f.write(pageHTML)
            f.close()
    
    def findProjectName(self, project):
        '''
        
        Extract the name of the project from the github URL
        
        '''
        projectName = project.split('/')[-1]
        
        return projectName
    
    def findProjectRawPath(self, string):
        '''
        
        Find the raw version of the project path
        
        '''
        rawPath = string.split('.com')[-1]
        rawPath = "https://raw.githubusercontent.com" + rawPath
        rawPath = rawPath.replace('\n', '')
        return rawPath