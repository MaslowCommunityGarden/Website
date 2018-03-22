from github import Github
import pygit2
import os

def authenticate(credentials):
    return credentials

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
credentials = pygit2.UserPass(userName, password)

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
    repoClone = pygit2.clone_repository(repo.git_url, '/var/www/html/uploads/tmp')
    print "GIT URL: "
    print repo.clone_url
    print "<---"
    
    #Add the new files to the repo
    for file in files:
        os.rename("/var/www/html/uploads/" + file, "/var/www/html/uploads/tmp/" + file)
    
    #Commit it
    repoClone.remotes.set_push_url("origin", repo.clone_url)
    index = repoClone.index
    index.add_all()
    index.write()
    author = pygit2.Signature("MaslowCommunityGardenRobot", "info@maslowcnc.com")
    commiter = pygit2.Signature("MaslowCommunityGardenRobot", "info@maslowcnc.com")
    tree = index.write_tree()
    oid = repoClone.create_commit('refs/heads/master', author, commiter, "init commit",tree,[repoClone.head.get_object().hex])
    #remote = repoClone.remotes["origin"]
    #remote.credentials = credentials
    #signature = author
    #remote.push(['refs/heads/master'], credentials)
    
    
    with open("/var/www/html/trackedProjects.txt", "a") as f:
       f.write("\n" + repo.html_url)
    repo.delete()





