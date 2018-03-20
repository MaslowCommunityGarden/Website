from github import Github

file = open("/var/www/html/uploads/usrinput.txt", "r")
userInputsText = file.readlines() 
userInputs     = userInputsText.split('~')
try:
    projectName = userInputs[0].replace('\n', '')
except:
    projectName = "none"
projectDescription = userInputs[1].replace('\n', '')
managementStyle = userInputs[2].replace('\n', '')
githubUser = userInputs[3].replace('\n', '')

print "\nProject name: "
print projectName
print "\nProject description"
print projectDescription
print "\nManagment style"
print managementStyle
print "\nUser name"
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

