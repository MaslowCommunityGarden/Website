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
    
    #print "\n\nRobot processing repo: " + repo.name
    
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
        
        if 'communityManaged' in robotText:
            #print "This project is community managed"
            
            openPullRequests = repo.get_pulls()
            for pullRequest in openPullRequests:
                
                print pullRequest.title
                
                pullRequestAlreadyRespondedTo = False
                
                #print "mergable " + str(pullRequest.mergeable)
                #print pullRequest.user
                #print "comments:" + str(pullRequest.comments)
                #print "review comments:" + str(pullRequest.review_comments)
                
                
                prAsIssue = repo.get_issue(pullRequest.number)
                comments  = prAsIssue.get_comments()  #this is a work around for a but in pygithub. We have to use the issues API :rolleyes:
                
                #determine if the robot has already commented"
                robotHasAlreadyCommented = False
                for comment in comments:
                    if 'Congratulations on the' in comment.body:
                        robotHasAlreadyCommented = True
                
                if robotHasAlreadyCommented:
                    print "Previous robot comment detected, should count votes and check time since comment"
                else:
                    commentText = "Congratulations on the pull request @" + pullRequest.user.login + "!!\n\n Now we need to decide as a community if we want to integrate these changes. You can vote by giving this comment a thumbs up or a thumbs down. Ties will not be merged.\n\nI'm just a silly robot, but I love to see people contributing so I'm going vote thumbs up!"
                    theNewComment = prAsIssue.create_comment(commentText)
                    theNewComment.create_reaction("+1")
        else:
            print "This project is not community managed"
    except Exception as e:
        print "This repo does not have a ROBOT.md file"
        print e