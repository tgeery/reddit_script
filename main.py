#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
import time
import os

reddit = praw.Reddit(client_id=os.environ['REDDIT_CLIENT_ID'], \
                     client_secret=os.environ['REDDIT_CLIENT_SECRET'], \
                     user_agent=os.environ['REDDIT_USER_AGENT'], \
                     username=os.environ['REDDIT_USERNAME'], \
                     password=os.environ['REDDIT_PASSWORD'])
subreddit_lst = ['Superstonk', 'Wallstreetbets']
for sub in subreddit_lst:
    subreddit = reddit.subreddit('Superstonk')
    top_sub = subreddit.new()
    print(sub)
    i = 1
    for submission in top_sub:
        dt_fmt = time.strftime('%m-%d-%Y %H:%M:%S', time.localtime(submission.created_utc))
        print(f'\t{i}) {submission.id} {dt_fmt}, ups: {submission.ups} up_ratio: {submission.upvote_ratio} rewards: {submission.total_awards_received}\n\t\t{submission.title[:100]}')
        i += 1
