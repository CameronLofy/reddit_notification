from send_push import *
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
		

message = f"Top Posts links from: <a href={urls[0]}>{subreddits[0]}</a> | <a href={urls[1]}>{subreddits[1]}</a> | <a href={urls[2]}>{subreddits[2]}</a>"
	
send_push(message)
