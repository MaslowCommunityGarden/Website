from github     import Github
import              urllib2

file = open("/home/ubuntu/gitlogin.txt", "r") 
logins = file.readlines() 
userName = logins[0].replace('\n', '')
password = logins[1].replace('\n', '')

# using username and password
g = Github(userName, password)
org = g.get_organization('MaslowCommunityGarden')

#Open list of tracked projects -- right now the robot can only work on repos in the community garden org
#file = open("/var/www/html/trackedProjects.txt", "r") 
#trackedProjectPaths = file.readlines() 

repos = org.get_repos()

for repo in repos:
    
    print "robot processing repo: " + repo.name
    
    #read the ROBOT.md file to see if the robot should interact with this project
    
    try:
        #find the URL to the file
        trackedURL  = repo.html_url
        rawPath     = trackedURL.split('.com')[-1]
        rawPath     = "https://raw.githubusercontent.com" + rawPath
        rawPath     = rawPath.replace('\n', '')
        robotURL    = rawPath + '/master/ROBOT.md'
        robotURL    = "".join(robotURL.split())
        
        #read the file
        text        = urllib2.urlopen(robotURL)
        robotText   = text.read()
        
        print "Robot text:"
        print robotText
        
        if 'communityManaged' in robotText:
            print "This project is community managed"
        else:
            print "this project is not community managed"
        
        openPullRequests = repo.get_pulls()
        for pullRequest in openPullRequests:
            print (repo.name)
            print pullRequest.title
            
            pullRequestAlreadyRespondedTo = False
            
            print "mergable"
            print pullRequest.mergeable
            print "user:"
            print pullRequest.user
            print "comments:"
            print pullRequest.comments
            print "review comments:"
            print pullRequest.review_comments
            comments = pullRequest.get_comments()
            print comments
            for aComment in comments:
                print "Comment Text:"
                print aComment.body
    except Exception as e:
        print "This repo does not have a ROBOT.md file"
        print e