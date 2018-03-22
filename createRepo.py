from github import Github
import pygit2
import os

file = open("/var/www/html/uploads/usrinput.txt", "r")
userInputsText = file.read() 
userInputs     = userInputsText.split('~')
try:
    projectName = userInputs[0].replace('\n', '')
except:
    projectName = "none"
try:
    projectDescription = userInputs[1].replace('\n', '')
except:
    projectDescription = "No description entered"
try:
    managementStyle = userInputs[2].replace('\n', '')
except:
    managementStyle = "none"
try:
    githubUser = userInputs[3].replace('\n', '')
except:
    githubUser = "nobody"
    

file = open("/home/ubuntu/gitlogin.txt", "r") 
logins = file.readlines() 
userName = logins[0].replace('\n', '')
password = logins[1].replace('\n', '')

# using username and password
g = Github(userName, password)
org = g.get_organization('MaslowCommunityGarden')

readmeText = "# " + projectName + "\n" + projectDescription

if projectName != "none":
    repo = org.create_repo(projectName, description = projectDescription )
    
    #create the markdown files
    repo.create_file("/README.MD", "init commit", readmeText)
    repo.create_file("/INSTRUCTIONS.MD", " init commit", "Edit this file to add assembly instructions")
    repo.create_file("/BOM.MD", "init commit", "Edit this file to add a bill of materials")
    
    #Keep track of what files we've got to add to the repo
    files = os.listdir('/var/www/html/uploads')
    
    #Clone the newly created repo
    Repo = pygit2.clone_repository(repo.html_url, '/var/www/html/uploads/tmp')
    print Repo
    
    #Add the new files to the repo
    for file in files:
        os.rename("/var/www/html/uploads/" + file, "/var/www/html/uploads/tmp/" + file)
    
    #Commit it
    
    
    
    with open("/var/www/html/trackedProjects.txt", "a") as f:
       f.write("\n" + repo.html_url)
    repo.delete()





