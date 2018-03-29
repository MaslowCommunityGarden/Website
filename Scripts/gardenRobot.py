from github import Github

file = open("/home/ubuntu/gitlogin.txt", "r") 
logins = file.readlines() 
userName = logins[0].replace('\n', '')
password = logins[1].replace('\n', '')

# using username and password
g = Github(userName, password)
org = g.get_organization('MaslowCommunityGarden')

#Open list of tracked projects
file = open("/var/www/html/trackedProjects.txt", "r") 
trackedProjectPaths = file.readlines() 

for projectPath in trackedProjectPaths:
    projectPath = projectPath.replace('\n', '')
    print projectPath
    print projectPath.split('/')