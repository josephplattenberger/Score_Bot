import thread_database
import datetime
import time
import sys
import praw

def calculate_votes(score, upvote_ratio):
    # if ratio is .5 then function would've given a divide by zero error
    if upvote_ratio == .5:
        return sys.maxint, -sys.maxint
    down = score * (1 - upvote_ratio) / (2 * upvote_ratio - 1)
    up = score + down
    return up, down

def ratio_to_percent(ratio):
    if ratio == 1.0:
        return "100"
    ratio_str = str(ratio)[2:]
    if len(ratio_str) == 1:
        return ratio_str + '0'
    if ratio_str[0] == '0':
        return ratio_str[1:]
    return ratio_str

def post_comment(thread):
    score = thread.score
    upvote_ratio = thread.upvote_ratio
    upvote_ratio_str = ratio_to_percent(upvote_ratio)
    upvotes, downvotes = calculate_votes(score, upvote_ratio)
    upvotes = int("{:.0f}".format(upvotes))
    downvotes = int("{:.0f}".format(downvotes))
    total_votes = int("{:.0f}".format(upvotes + downvotes))
    comment = "This post is " + upvote_ratio_str + "% upvoted\n\n" \
              + "Total votes: " + str(total_votes) + "\n\n" \
                  + "Upvotes: " + str(upvotes) + "\n\n" \
                  + "Downvotes: " + str(downvotes) + "\n\n" \
                  + "Brigade_Detector_Bot made by u/joeymp"
    comment_posted = False
    comment_stored = False
    while not comment_posted:
        try:
            comment = thread.add_comment(comment)
            comment_posted = True
        except:
            print "Failed to post comment to thread %s" % mThread.permalink
            time.sleep(30)

    while not comment_stored:
        try:
            thread_database.add_comment_link(thread.permalink, comment.id)
            comment_stored = True
        except:
            print "Failed to store comment to thread %s" % thread.permalink
    
        
def edit_comment(thread, comment):
    one_day_since_creation = \
                datetime.datetime.utcfromtimestamp(thread.created_utc)\
                           + datetime.timedelta(days = 1)
    if datetime.datetime.utcnow() <= one_day_since_creation:
        score = thread.score
        upvote_ratio = thread.upvote_ratio
        upvote_ratio_str = ratio_to_percent(upvote_ratio)
        upvotes, downvotes = calculate_votes(score, upvote_ratio)
        upvotes = int("{:.0f}".format(upvotes))
        downvotes = int("{:.0f}".format(downvotes))
        total_votes = int("{:.0f}".format(upvotes + downvotes))
        comment.edit("----------Updated----------\n\n" \
                      + "This post is " + upvote_ratio_str \
                      + "% upvoted\n\n" \
                      + "Total votes: " + str(total_votes) + "\n\n" \
                      + "Upvotes: " + str(upvotes) + "\n\n" \
                      + "Downvotes: " + str(downvotes) + "\n\n" \
                      + "Brigade_Detector_Bot made by u/joeymp\n\n")
        print "updated comment: %s" % comment.permalink
        print datetime.datetime.utcnow()
        return False
    else:
        thread_database.delete_thread(thread.permalink)
        return True
            
