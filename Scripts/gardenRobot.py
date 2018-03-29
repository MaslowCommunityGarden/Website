from github import Github

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
        print comments[0]
        for aComment in comments:
            print "Comment Text:"
            print aComment.body