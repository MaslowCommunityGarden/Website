from github import Github

file = open("/home/ubuntu/gitlogin.txt", "r") 
logins = file.readlines() 
userName = logins[0].replace('\n', '')
password = logins[1].replace('\n', '')

# using username and password
g = Github(userName, password)

#Open list of tracked projects
file = open("/var/www/html/trackedProjects.txt", "r") 
trackedProjectPaths = file.readlines() 

for projectPath in trackedProjectPaths:
    projectPath = rawPath.replace('\n', '')
    print projectPath