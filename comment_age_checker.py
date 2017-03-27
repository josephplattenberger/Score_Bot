import thread_database
from bot_comment import edit_comment
import obot
import time
import praw
import requests

r = obot.login()
while True:
    threads = thread_database.get_threads()
    delete_flag = False
    if threads != None:
        for row in threads:
            thread = row[0]
            comment = row[1]
            if comment != None:
                connect_to_reddit = False
                while not connect_to_reddit:
                    try:
                        mThread = r.get_submission(thread)
                        comment_id = "t1_" + str(comment)
                        mComment = r.get_info(thing_id = comment_id)
                        connect_to_reddit = True
                    except requests.ConnectionError as e:
                        print "\n------ConnectionError------"
                        print e
                        print "---------------------------\n"
                    except requests.HTTPError as e:
                        print "\n---------HTTPError---------"
                        print e
                        print "---------------------------\n"
                delete_flag = edit_comment(mThread, mComment)
            if delete_flag:
                break
    if not delete_flag:
        time.sleep(180)
    
