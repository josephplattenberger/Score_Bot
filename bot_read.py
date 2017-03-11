import thread_database
from bot_comment import post_comment
import obot
import time
import datetime
import praw

###############################################
# Creates the table on the first run, however #
# comment out if bot stops running and        #
# you don't want to lose your database data   #
###############################################
thread_database.clear_table() #
########################
r = obot.login()
while True:
    # Can change subreddit and section to montior
    subreddit = r.get_subreddit('test').get_hot(limit=25)
    for submission in subreddit:
        thread = r.get_submission(submission.permalink)
        upvote_ratio = thread.upvote_ratio
        created = datetime.datetime.fromtimestamp(submission.created_utc)
        # Can edit how long to keep threads in the database
        # if changed you may want to change when it gets deleted 
        # in bot_comment.edit_comment()
        one_day_since_creation = created + datetime.timedelta(days = 1)
        # Can change upvote_ratio to monitor for
        if upvote_ratio < .9 \
           and datetime.datetime.utcnow() <= one_day_since_creation:
            print"\n------Scanned------"
            print"Link: %s" % submission.permalink
            print("\n-----DATABASE-----")
            if not thread_database.contains_thread(submission.permalink):
                thread_database.insert_thread(submission.permalink)
                post_comment(thread)
    time.sleep(600)