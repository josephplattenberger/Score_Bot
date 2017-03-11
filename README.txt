Made with Python 2.7
Must install MySQL 5.7 and create a user and database
Must install 'praw 3.60' through 'pip'
Replace the login credentials for the database(db_login.py) and reddit(obot.py) with your info
Run bot_read.py to scan a section of a subreddit for submissions under a desired upvote_ratio and age and to post a comment in said submission with the "exact" number of upvotes and downvotes on it.
Run comment_age_checker.py to edit your comments with updated numbers and delete threads from your database that are older than a desired age
