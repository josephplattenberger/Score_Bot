import praw

client_id = 'YOUR APP ID'
client_secret = 'YOUR APP SECRET'
user_agent = 'Brigade_Detector by u/joeymp'
redirect_uri = 'http://localhost:8080'
app_refresh = 'YOUR APP REFRESH CODE'

def login():
    r = praw.Reddit(user_agent)
    r.set_oauth_app_info(client_id, client_secret, redirect_uri)
    r.refresh_access_information(app_refresh)
    return r
    
