from github import Github

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
    
print "\n\nProject name: "
print projectName
print "\n\nProject description"
print projectDescription
print "\n\nManagment style"
print managementStyle
print "\n\nUser name"
print githubUser

file = open("/home/ubuntu/gitlogin.txt", "r") 
logins = file.readlines() 
userName = logins[0].replace('\n', '')
password = logins[1].replace('\n', '')

# using username and password
g = Github(userName, password)
org = g.get_organization('MaslowCommunityGarden')

readmeText = "#" + projectName + "\n" + projectDescription

if projectName != "none":
    repo = org.create_repo(projectName, description = projectDescription )
    print repo
    repo.create_file("/README.MD", "init commit", readmeText)
    repo.create_file("/INSTRUCTIONS.MD", " init commit", "Edit this file to add assembly instructions")
    repo.create_file("/BOM.MD", "init commit", "Edit this file to add a bill of materials")
    repo.create_file("/mainpicture.jpg", "init commit", readmeText)
    repo.delete()


#f = open('/var/www/html/trackedProjects.txt','w')
#f.write("This is some text!")
#print f
#f.close()

