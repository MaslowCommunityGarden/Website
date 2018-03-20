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

if projectName != "none":
    repo = org.create_repo(projectName, description = projectDescription )
    print repo
    repo.create_file("/README.MD", "init commit", "This is some test text")


f = open('/var/www/html/uploads/testScriptRan.txt','w')
f.write("This is some text!")
print f
f.close()

