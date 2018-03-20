from github import Github

print "python script is running!"

file = open("/home/ubuntu/gitlogin.txt", "r") 
print file
logins = file.readlines() 
print logins
userName = logins[0].replace('\n', '')
password = logins[1]

# using username and password
g = Github(userName, password)
org = g.get_organization('MaslowCommunityGarden')

repo = org.create_repo("auto login from server test")

f = open('/var/www/html/uploads/testScriptRan.txt','w')
f.write("This is some text!")
f.close()