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
                #find the path to the README file
                readmeUrl = string + '/master/README.md'
                readmeUrl = "".join(readmeUrl.split())
                thisProject.READMEpath = readmeUrl
                
                #Construct the project object
                thisProject.projectName = self.findProjectName(string)
                thisProject.projectFile = thisProject.projectName + '.html'
                thisProject.mainPicture = string + '/master/mainpicture.jpg'
                thisProject.READMEpath  = readmeUrl
                
                #read the README file
                linesInReadme = urllib2.urlopen(readmeUrl)
                thisProject.READMEtext  = linesInReadme.read()
                
                
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
        
        with tag('div', klass="content"):
            with tag('html'):
                with tag('head'):
                    doc.stag('link',rel='stylesheet', href='styles.css')
                    doc.stag('link',rel='stylesheet', type="text/css", href="https://fonts.googleapis.com/css?family=Open+Sans")
                    
                with tag('body', klass = 'body'):
                
                    doc.stag('img', src="logo.png", width="166", height="45")
                    
                    with tag('a', href="http://example.com", klass="button"):
                        text('How does the garden work?')
                    
                    with tag('a', href="http://example.com", klass="button"):
                        text('Add a project')
                    
                    with tag('hr'):
                        pass
                    
                    
                    with tag('p'):
                        text('A place for community driven open source projects to live')
                    
                    with tag('hr'):
                        pass
                    

                    
                    #Generate a grid of tracked projects
                    
                    for project in self.projects:
                        
                        print "Generating grid entry for: "
                        print project.projectName
                        
                        
                        #this creates a boxed representation of the project
                        with tag('a', href=project.projectFile):
                            with tag('div', klass = 'boxed'):
                                
                                doc.stag('img', src= project.mainPicture, width="400", height="180")
                                
                                numberOfLinesProcessed = 0
                                maxNumberToProcess = 3
                                linesInReadme = project.READMEtext.split('\n', 5)
                                
                                for line in linesInReadme:
                                    if len(line) > 0:
                                        if line[0] is '#':
                                            with tag('h1'):
                                                text(line[1:])
                                        elif line[0] is not '!':
                                            with tag('p'):
                                                text(line)
                                    numberOfLinesProcessed = numberOfLinesProcessed + 1
                                    if numberOfLinesProcessed > maxNumberToProcess:
                                        break
    
        f = open('index.html','w')
        f.write(doc.getvalue())
        f.close()

    def generatePagesForProjects(self):
        for project in self.projects:
            
            markdowner = Markdown() #allows for the conversion of markdown files into html
            
            print "Generating file: "
            print project.projectFile
            
            #Generate and HTML file for the project
            f = open(project.projectFile,'w')
            f.write(markdowner.convert(project.READMEtext))
            f.close()
    
    def generateHowDoesTheGardenWorkPage(self):
        '''
        
        The function which builds the "how does it work" page
        
        '''
        pass
    def findProjectName(self, project):
        projectName = project.split('/')[-1]
        projectName = projectName[0:-1] #remove the trailing newline
        
        return projectName
    