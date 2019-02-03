from github import  Github
import              pygit2
import              os
import              time
import              base64

file = open("/var/www/html/uploads/usrinput.txt", "r")
userInputsText = file.read() 
userInputs     = userInputsText.split('~')
try:
    projectName = userInputs[0].replace('\n', '')
except:
    projectName = "none"

if "test" in projectName:
    print "Test detected, exiting early without creating a project"
    print "GIT URL:> https://www.example.com <---"
    import sys
    sys.exit()

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
    githubUser = githubUser.replace(" ", "")
except:
    githubUser = ""
try:
    category = userInputs[4].replace('\n', '')
    category = category.replace(" ", "")
    category = category.lower()
except:
    category = "other"
    

file = open("/home/ubuntu/gitlogin.txt", "r") 
logins = file.readlines() 
userName = logins[0].replace('\n', '')
password = logins[1].replace('\n', '')

# using username and password
g = Github(userName, password)
org = g.get_organization('MaslowCommunityGarden')

hintText = "\n\nYou can find instructions on how to edit this page on the community garden meta page [here](http://maslowcommunitygarden.org/Website.html?instructions=true)\n\n\n\nThe style cheat sheet [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) is useful"
readmeText = "# " + projectName + "\n\n" + projectDescription

if projectName != "none":
    try:
        
        print("At the very top");
        
        repo = org.create_repo(projectName, description = projectDescription )
        
        time.sleep(3) #This is probably more delay than github needs to create the repo. With no delay at all it worked about half the time
        
        print "Adding GitHub User:"
        print githubUser
        print "       "
        repo.add_to_collaborators(githubUser)
        
        robotText = (
            '{\n'
                '"ModerationLevel": "' + managementStyle + '",\n'
                '"Facilitator": "' + githubUser + '",\n'
                '"Category": "' + category + '"\n'
            '}')
        
        print("Creating markdown file")
        
        #create the markdown files
        repo.create_file("README.md", "init commit", readmeText)
        repo.create_file("INSTRUCTIONS.md", " init commit", "Edit this file to add assembly instructions" + hintText)
        repo.create_file("BOM.md", "init commit", "Edit this file to add a bill of materials"  + hintText)
        repo.create_file("ROBOT.md", "init commit", robotText)
        
        print("keeping track")
        
        #Keep track of what files we've got to add to the repo
        files = os.listdir('/var/www/html/uploads')
        
        #Clone the newly created repo
        repoClone = pygit2.clone_repository(repo.git_url, '/var/www/html/uploads/tmp')
        print "GIT URL:> " + repo.html_url + " <---"
        
        
        #Add the new files to the repo
        for file in files:
            os.rename("/var/www/html/uploads/" + file, "/var/www/html/uploads/tmp/" + file)
        
        #Commit it
        repoClone.remotes.set_url("origin", repo.clone_url)
        index = repoClone.index
        print("index")
        index.add_all()
        index.write()
        print("after write")
        author = pygit2.Signature("MaslowCommunityGardenRobot", "info@maslowcnc.com")
        commiter = pygit2.Signature("MaslowCommunityGardenRobot", "info@maslowcnc.com")
        print("setup author")
        tree = index.write_tree()
        print("\nclone\n");
        oid = repoClone.create_commit('refs/heads/master', author, commiter, "init commit",tree,[repoClone.head.target])
        print("clone")
        remote = repoClone.remotes["origin"]
        print("about to login")
        credentials = pygit2.UserPass(userName, password)
        remote.credentials = credentials
        
        callbacks=pygit2.RemoteCallbacks(credentials=credentials)
        print("about to push")
        remote.push(['refs/heads/master'],callbacks=callbacks)
        
        #This section writes the new tracked project name to the tracked projects list in github
        
        trackedProjectsRepo = org.get_repo('Website')
        
        fileName = 'trackedProjects.txt'
        
        print("getting file contents")
        
        #get the tracked projects list and decode it
        fileContents = trackedProjectsRepo.get_file_contents(fileName)
        trackedProjectsList = base64.b64decode(fileContents.content)
        
        #add the new project
        updatedTrackedProjectsList = trackedProjectsList + "\n" + repo.html_url
        
        print("About to update file")
        
        #push the new project on the list back to the github server
        trackedProjectsRepo.update_file(fileName, "add a project", updatedTrackedProjectsList, fileContents.sha)
        
        
    except Exception as e: 
        print "Oh darn, something went wrong in the python code..."
        print(e)
        try:
            repo.delete()
        except:
            pass
    else:
        print "Congratulations! Your project is has been created and will appear soon"





