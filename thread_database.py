import db_login
import MySQLdb

def login():
    return MySQLdb.connect(db_login.db_host, \
                           db_login.db_username, \
                           db_login.db_password, db_login.db_name)

def insert_thread(thread_link):
    db = login()
    cursor = db.cursor()
    stmt = "INSERT INTO THREADS(THREAD_LINK) VALUES ('%s')" % \
             (thread_link) 
    try:
        cursor.execute(stmt)
        db.commit()
        print "inserted thread: %s" % (thread_link)
        print "-------------------\n"
    except:
        db.rollback()
        print "failed inserting thread: %s" % (thread_link)
        print "-------------------\n"
    db.close()

def add_comment_link(thread_link, comment):
    db = login()
    cursor = db.cursor()
    stmt = "UPDATE THREADS SET COMMENT_LINK = '" + comment + \
            "' WHERE THREAD_LINK = '" + thread_link + "'"
    try:
        cursor.execute(stmt)
        db.commit()
        print "comment: %s" % comment
        print "added to thread: %s" % thread_link
        print "-------------------\n"
    except:
        db.rollback()
        print "failed adding comment: %s" % comment
        print "to thread: %s" % thread_link
        print "-------------------\n"
    db.close()

def delete_thread(thread_link):
    db = login()
    cursor = db.cursor()
    stmt = "DELETE FROM THREADS WHERE THREAD_LINK = '%s'" % thread_link
    try:
        cursor.execute(stmt)
        db.commit()
        print "deleted thread: %s" % thread_link
        print "-------------------\n"
    except:
        db.rollback()
        print "failed to delete thread: %s" % thread_link
        print "-------------------\n"
    db.close()
    
def contains_thread(thread_link):
    db = login()
    cursor = db.cursor()
    stmt = "SELECT THREAD_LINK FROM THREADS WHERE THREAD_LINK = '%s'" % \
            (thread_link)
    contained = False
    try:
        cursor.execute(stmt)
        data = cursor.fetchone()
        if data != None:
            contained = True
            print "unable to insert, contained thread: %s" % (data)
            print "-------------------\n"
    except:
        contained = False
        print "Error: Unable to find thread: %s" % (thread_link)
        print "-------------------\n"
    db.close()
    return contained

def get_threads():
    db = login()
    cursor = db.cursor()
    stmt = "SELECT * FROM THREADS"
    results = None
    try:
        cursor.execute(stmt)
        results = cursor.fetchall()
    except:
        results = None
        print "No threads exist"
        print "-------------------\n"
    db.close()
    return results

def clear_table():
    db = login()
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS THREADS")
    stmt = """CREATE TABLE THREADS (THREAD_LINK TEXT NOT NULL,
            COMMENT_LINK TEXT)"""
    cursor.execute(stmt)
    db.close()
        
