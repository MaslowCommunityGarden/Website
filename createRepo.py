from github import Github

file = open("/var/www/html/uploads/usrinput.txt", "r")
userInputs = file.readlines() 
projectName = logins[0].replace('\n', '')
projectDescription = logins[1].replace('\n', '')
managementStyle = logins[2].replace('\n', '')
githubUser = logins[3].replace('\n', '')

print "Project name: "
print projectName
print "Project description"
print projectDescription
print "Managment style"
print managementStyle
print "User name"
print githubUser

file = open("/home/ubuntu/gitlogin.txt", "r") 
logins = file.readlines() 
userName = logins[0].replace('\n', '')
password = logins[1].replace('\n', '')

# using username and password
g = Github(userName, password)
org = g.get_organization('MaslowCommunityGarden')

#org.create_repo("auto login from server test")


f = open('/var/www/html/uploads/testScriptRan.txt','w')
f.write("This is some text!")
print f
f.close()

