from github     import Github
import          urllib2
import          datetime
import          pygit2

class Robot:
    
    def voteOnPRs(self, repo):
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
                
                
                '''
                
                Check if there are any open pull requests that need to be voted on
                
                '''
                openPullRequests = repo.get_pulls()
                for pullRequest in openPullRequests:
                    
                    print "\n\n"+pullRequest.title
                    
                    pullRequestAlreadyRespondedTo = False
                    
                    #print "mergable " + str(pullRequest.mergeable)
                    #print pullRequest.user
                    #print "comments:" + str(pullRequest.comments)
                    #print "review comments:" + str(pullRequest.review_comments)
                    
                    
                    prAsIssue = repo.get_issue(pullRequest.number)
                    comments  = prAsIssue.get_comments()  #this is a work around for a bug in pygithub. We have to use the issues API :rolleyes:
                    
                    #determine if the robot has already commented"
                    robotHasAlreadyCommented = False
                    for comment in comments:
                        if 'Congratulations on the' in comment.body:
                            robotHasAlreadyCommented = True
                            
                            upVotes = 0
                            downVotes = 0
                            for reaction in comment.get_reactions():
                                if reaction.content == '+1':
                                    upVotes = upVotes + 1
                                if reaction.content == '-1':
                                    downVotes = downVotes + 1
                            
                            
                            timeOpened = pullRequest.created_at
                            
                            elapsedTime = (datetime.datetime.now() - timeOpened).total_seconds()
                            
                            
                            seventyTwoHoursInSeconds = 259200
                            if elapsedTime < seventyTwoHoursInSeconds:
                                print "not enough time has passed to merge the pull request"
                            else:
                                if upVotes > downVotes:
                                    commentText = "Woo!! Times up and we're ready to merge this pull request! Great work!"
                                    theNewComment = prAsIssue.create_comment(commentText)
                                    pullRequest.merge()
                                else:
                                    commentText = "It looks like adding these changes right now isn't a good idea. Consider any feedback that the community has given about why not and feel free to open a new pull request with the changes"
                                    theNewComment = prAsIssue.create_comment(commentText)
                                    prAsIssue.edit(state='closed')
                    
                    if not robotHasAlreadyCommented:
                        commentText = "Congratulations on the pull request @" + pullRequest.user.login + "!!\n\n Now we need to decide as a community if we want to integrate these changes. You can vote by giving this comment a thumbs up or a thumbs down. Votes are counted in 72 hours. Ties will not be merged.\n\nI'm just a silly robot, but I love to see people contributing so I'm going vote thumbs up!"
                        theNewComment = prAsIssue.create_comment(commentText)
                        theNewComment.create_reaction("+1")
                
                '''
                
                Check if there are any open pull requests that need to be voted on
                
                '''
                
                if 'delete' in robotText:
                    
                    #remove the string from the tracked projects list
                    with open("/var/www/html/trackedProjects.txt", "r+") as f:
                        text = f.read()
                        text = text.replace(repo.html_url,'')
                        f.write(text)
                    
                    #delete the repo
                    repo.delete()
                
            else:
                print "This project is not community managed"
        except Exception as e:
            print "This repo does not have a ROBOT.md file"
            print e