from github import Github

file = open("../gitlogin.txt", "r") 
logins = file.readlines() 
userName = logins[0].replace('\n', '')
password = logins[1]

# using username and password
g = Github(userName, password)
org = g.get_organization('MaslowCommunityGarden')

repo = org.create_repo("auto login from server test")

f = open('/var/www/html/uploads/testScriptRan.txt','w')
f.write("This is some text!")
f.close()