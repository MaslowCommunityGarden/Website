from github     import Github
import          urllib2
import          datetime
import          pygit2
from robot      import Robot

file = open("/home/ubuntu/gitlogin.txt", "r") 
logins = file.readlines() 
userName = logins[0].replace('\n', '')
password = logins[1].replace('\n', '')

# using username and password
g = Github(userName, password)
org = g.get_organization('MaslowCommunityGarden')

repos = org.get_repos()

file = open("/home/ubuntu/gitlogin.txt", "r") 
logins = file.readlines() 
userName = logins[0].replace('\n', '')
password = logins[1].replace('\n', '')

robot = Robot()

for repo in repos:
    
    #print "\n\nRobot processing repo: " + repo.name
    
    #read the ROBOT.md file to see if the robot should interact with this project
    
    robot.voteOnPRs(repo)