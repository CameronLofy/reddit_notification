from send_push import *
from send_sms import send_sms
from url_shortener import make_tiny
from config import reddit_client_id, reddit_client_secret, reddit_password, reddit_username
from config import subreddits
import praw


#send_push("Test")

reddit = praw.Reddit(client_id = reddit_client_id,
                     client_secret = reddit_client_secret,
                     password = reddit_password,
                     user_agent = "Linux device",
                     username = reddit_username)
                    
print(reddit.user.me())



urls = []
for i in subreddits:
    sub = reddit.subreddit(i)
    for post in sub.hot(limit=10):
        if(post.stickied is False):
            urls.append("https://www.reddit.com" + post.permalink)
            break
        
# Shorten URLS:
for i in range(0, len(urls)):
    urls[i] = make_tiny(urls[i])
    

        
push_message = "Top posts from:"
text_message = push_message
for i in range(0,len(subreddits)):
    push_message = push_message + f"\n<a href={urls[i]}>{subreddits[i]}</a>"
    text_message = text_message + f"\n\n{subreddits[i]} : \n{urls[i]} "

send_sms(text_message)
send_push(push_message)
