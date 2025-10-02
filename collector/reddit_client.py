import os
from dotenv import load_dotenv
import praw

# load .env file
load_dotenv()

# set up reddit client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
)

# test login
print("Logged in as:", reddit.user.me())

print(type(reddit))
