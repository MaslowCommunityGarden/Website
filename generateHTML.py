import              urllib2  # the lib that handles the url stuff
import              random
from markdown2      import Markdown
from projectClass   import Project
import              json
import              re

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
                
                #find the path to the ROBOT file
                robotUrl = thisProject.projectPathRaw + '/master/ROBOT.md'
                robotUrl = "".join(robotUrl.split())
                
                
                #Construct the project object
                thisProject.projectName = self.findProjectName(thisProject.projectPathRaw)
                
                
                thisProject.projectFile = thisProject.projectName + '.html'
                thisProject.mainPicture = thisProject.projectPathRaw + '/master/mainpicture.jpg'
                thisProject.READMEpath  = readmeUrl
                
                thisProject.editREADMEpath      = thisProject.projectPath + '/blob/master/README.md'
                thisProject.editINSTRUCTIONpath = thisProject.projectPath + '/blob/master/INSTRUCTIONS.md'
                thisProject.editBOMpath         = thisProject.projectPath + '/blob/master/BOM.md'
                
                
                #read the README file
                thisProject.READMEtext  = urllib2.urlopen(readmeUrl).read()
                
                #read the INSTRUCTIONS file
                thisProject.INSTRUCTIONStext  = urllib2.urlopen(instructionsUrl).read()
                
                #read the BOM file
                thisProject.BOMtext  = urllib2.urlopen(bomUrl).read()
                
                #read the ROBOT file
                thisProject.ROBOTtext  = urllib2.urlopen(robotUrl).read()
                
                #find the download link
                print thisProject.projectName
                try:
                    downloadTarget = json.loads(thisProject.ROBOTtext)["DownloadTarget"]
                    thisProject.downloadLink = thisProject.projectPath + downloadTarget
                    print "download target read*************************"
                    print thisProject.downloadLink
                except:
                    thisProject.downloadLink = thisProject.projectPath + "/archive/master.zip"
                
                #scrape the number of project star gazers
                starGazersScrape = urllib2.urlopen(thisProject.projectPath).read()
                match = re.search( '(?<=aria-label=")(.*)(?= users starred this repository)', starGazersScrape)
                
                if match:
                    thisProject.starGazers = int(match.group(1))
                else:
                    "unable to read stargazers defaulting to 0"
                    
                
                self.projects.append(thisProject)
                

            except Exception as e:
                print string
                print "<- could not be read"
                print (e)
    
    def sortProjects(self):
        '''
        
        Sort projects based on how many likes each has gotten
        
        '''
        
        self.projects.sort(key=lambda x: x.starGazers, reverse=True)
    
    def buildMainSite(self):
        '''
        
        This function builds the main website
        
        '''
        
        #generate the HTML for the main page
        
        pageHTML = ("<!DOCTYPE html>"
                "<html>"
                    "<head>"
                        "<link href='styles.css' rel='stylesheet' />"
                        "<link href='https://fonts.googleapis.com/css?family=Open+Sans' type='text/css' rel='stylesheet' />"
                    "</head>"
                    "<body class = body>"
                        "<header class = 'header'>"
                            "<div class='inner-header'>"
                                "<a href='index.html'>"
                                    "<img src='logo.png' style='width:auto;height:90px;border:0;'>"
                                "</a>"
                                "<nav class='navigation'>"
                                    "<a href='howdoesthegardenwork.html' class='nav-link button one-col'>How Does the Garden Work?</a>"
                                    " "
                                    "<a href='addaproject.html' class='nav-link button one-col'>Add A Project</a>"
                                "</nav>"
                            "</div>"
                        "</header>"
                        "<section class = content>"
                            "<div class='tab three-col'>"
                                "<button class=\"tablinks\" onclick=\"openTab(event, 'Maslow'        )\"id=\"defaultOpen\">Maslow</button>"
                                "<button class=\"tablinks\" onclick=\"openTab(event, 'Furniture'     )\">Furniture</button>"
                                "<button class=\"tablinks\" onclick=\"openTab(event, 'Food+Shelter'  )\">Food+Shelter</button>"
                                "<button class=\"tablinks\" onclick=\"openTab(event, 'Signs'         )\">Signs</button>"
                                "<button class=\"tablinks\" onclick=\"openTab(event, 'Other'         )\">Other</button>"
                            "</div>"
                    )
                    
                    #Generate a grid of tracked projects
        
        maslowProjects      = ""
        furnitureProjects   = ""
        foodshelterProjects = ""
        signsProjects       = ""
        otherProjects       = ""
        
        for project in self.projects:
            print "Generating grid entry for: "
            print project.projectName
            
            
            #this creates a boxed representation of the project
            
            projectSection = ("<a href= " + project.projectFile + " class = project_link>"
                                "<div class = boxed>"
                                    "<div class = project-thumbnail>"
                                        "<img src="+project.mainPicture+" class = project_img>")
                    
            numberOfLinesProcessed = 0
            maxNumberToProcess = 3
            linesInReadme = project.READMEtext.split('\n', 5)
            
            for line in linesInReadme:
                if len(line) > 0:
                    if line[0] is '#':
                        projectSection = projectSection + (
                        "<h1 class = boxed_text>"
                            +line[1:]+
                        "</h1>")
                        
                        project.projectName = line[1:]
                    elif line[0] is not '!':
                        projectSection = projectSection + (
                        "<p class = boxed_text>"
                            +line+
                        "</p>")
                numberOfLinesProcessed = numberOfLinesProcessed + 1
                if numberOfLinesProcessed > maxNumberToProcess:
                    break
            projectSection = projectSection + "</div> </div> "
            
            
            try:
                projectCategory = json.loads(project.ROBOTtext)["Category"]
            except Exception as e:
                projectCategory =  "other"
            
            if projectCategory == "maslow":
                maslowProjects = maslowProjects + projectSection
            elif projectCategory == "furniture":
                furnitureProjects = furnitureProjects + projectSection
            elif projectCategory == "food+shelter":
                foodshelterProjects = foodshelterProjects + projectSection
            elif projectCategory == "signs":
                signsProjects = signsProjects + projectSection
            else:
                otherProjects = otherProjects + projectSection
                
        
        pageHTML = pageHTML + (
        "<div id='Maslow' class='tabcontent'>"
            + maslowProjects +
        "</div>"
        
        "<div id='Furniture' class='tabcontent'>"
            + furnitureProjects +
        "</div>"
        
        "<div id='Food+Shelter' class='tabcontent'>"
            + foodshelterProjects +
        "</div>"
        
        "<div id='Signs' class='tabcontent'>"
            + signsProjects +
        "</div>"
        
        "<div id='Other' class='tabcontent'>"
            + otherProjects +
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
        "<script>"
            "function truncate( n, useWordBoundary ){"
                "if (this.length <= n) { return this; }"
                "var subString = this.substr(0, n-1);"
                "return (useWordBoundary "
                "   ? subString.substr(0, subString.lastIndexOf(' ')) "
                "   : subString) + '&hellip;';"
            "};"

            "var boxed_titles = document.querySelectorAll('.boxed h1.boxed_text');"
            "var boxed_title_length = 55;"
            "for(var i = 0; i < boxed_titles.length; i++){"
            "  boxed_titles[i].innerHTML = truncate.apply(boxed_titles[i].innerText, [boxed_title_length, true]);   "
            "}"

            "var boxed_descriptions = document.querySelectorAll('.boxed p.boxed_text');"
            "var boxed_descriptions_length = 85;"
            "for(var i = 0; i < boxed_descriptions.length; i++){"
            "  boxed_descriptions[i].innerHTML = truncate.apply(boxed_descriptions[i].innerText, [boxed_descriptions_length, true]);  " 
            "}"
        "</script>"
            )
        f = open('index.html','w')
        f.write(pageHTML)
        f.close()

    def generatePagesForProjects(self):
        for project in self.projects:
            pageHTML = ""
            print "Generating file: "
            print project.projectFile
            
            classesDict = {'img':'page_img'}
            markdowner = Markdown(extras={"tables": None, "html-classes":classesDict}) #allows for the conversion of markdown files into html
            
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
                        "<script>"
                          "function resizeIframe(obj) {"
                            "obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';"
                          "}"
                        "</script>"
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
                            "</nav>"
                        "</div>"
                    "</header>"
                        
                    "<section class = 'content'>"
                        "<div class = 'ProjectName'>"
                            "<h1 class='title'>" + project.projectName + "</h1>"
                        "</div>"
                    
                        "<div class='tab three-col'>"
                            "<button class=\"tablinks\" onclick=\"openTab(event, 'Files'       )\" id=\"defaultOpen\">Files</button>"
                            "<button class=\"tablinks\" onclick=\"openTab(event, 'Instructions')\" id=\"instructionsBTN\">Instructions</button>"
                            "<button class=\"tablinks\" onclick=\"openTab(event, 'Forums'      )\">Forums</button>"
                            "<button class=\"tablinks\" onclick=\"openTab(event, 'Buy'         )\">Buy</button>"
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
                            "<br>"
                            "<br>"
                            "<br>"
                            "<br>"
                            "<div class='three-col'>"
                                + instructionsText +
                            "</div>"
                        "</div>"

                        "<div id='Forums' class='tabcontent'>"
                          "<div class='tab-title'>"
                            "<h3 class='three-col'>Forums</h3>"
                          "</div>"
                              "<div id='discourse-comments', class = 'forums_section'>"
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
                            "<br>"
                            "<br>"
                            "<br>"
                            "<br>"
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
                                "var ifr = document.getElementById('discourse-embed-frame');"
                                "ifr.src = ifr.src;"
                            "}"
    
                            "document.getElementById('defaultOpen').click();"
                            "</script>"
                            "<script>"
                                "if (window.location.search.indexOf('instructions=true') > -1) {"
                                    "document.getElementById('instructionsBTN').click();"
                                "}"
                                "if (window.location.search.indexOf('instructions=True') > -1) {"
                                    "document.getElementById('instructionsBTN').click();"
                                "}"
                            "</script>"
                        "</div>"  
                        "<footer class='footer-basic-centered'>"

                            "<p class='footer-company-motto'>The garden is a project of the <a href='http://www.maslowcnc.com'>Maslow CNC</a> community.</p>"

                            "<p class='footer-links'>"
                                "<a href='http://maslowcommunitygarden.org/howdoesthegardenwork.html'>Why</a>"
                                "  "
                                "<a href='#'>How</a>"
                                "  "
                                "<a href='http://maslowcommunitygarden.org/addaproject.html'>Add</a>"
                                "  "
                                "<a href='http://maslowcommunitygarden.org/index.html'>See</a>"
                                "  "
                                "<a href='http://www.maslowcnc.com/'>Maslow CNC</a>"
                                "  "
                                "<a href='http://www.maslowcnc.com/forums'>Forums</a>"
                            "</p>"

                            "<p class='footer-company-name'>All content available under license of creator</p>"

                        "</footer>"
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