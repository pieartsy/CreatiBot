#python reddit api wrapper
import praw
#imports stuff to interact with reddit api
from config import REDDIT_ID, REDDIT_SECRET, REDDIT_PWD, REDDIT_USERNAME
#to choose from a random prompt
import random

#reddit instance
reddit = praw.Reddit(client_id= REDDIT_ID,
                     client_secret= REDDIT_SECRET,
                     password= REDDIT_PWD,
                     user_agent='CreatiBot',
                     username= REDDIT_USERNAME)

#gets subreddit instance
subreddit = reddit.subreddit('writingprompts')

#newest 50 writing prompts
new50prompts = []

#for submission in the Writing Prompts flair
for submission in subreddit.search('flair:"Writing Prompt"', limit=50):
    new50prompts.append(submission.title.replace("[WP]", ''))

prompt = random.choice(new50prompts)