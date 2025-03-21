import firebase_admin
from firebase_admin import credentials, db
from sentiment_analysis.analyzer import analyze_subreddit
from datetime import datetime, timedelta
import os

# Initialize Firebase
cred = credentials.Certificate("firebase_credentials.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://my-website-517f8-default-rtdb.firebaseio.com'
    })

# List of subreddits to track
subreddits = ['technology', 'science', 'worldnews', 'gaming', 'python']

# Backfill range - set number of days back to push data for
days_back = 1  # Change this to desired number of days

for i in range(days_back):
    target_date = datetime.now() - timedelta(days=i)
    date_str = target_date.strftime('%Y-%m-%d')

    for subreddit in subreddits:
        sentiments, posts = analyze_subreddit(subreddit_name=subreddit)

        ref = db.reference(f'sentiment_trend/{subreddit}/{date_str}')
        ref.set({
            "sentiments": sentiments,
            "posts": posts
        })

        print(f"🔥 Data pushed for r/{subreddit} on {date_str}")
