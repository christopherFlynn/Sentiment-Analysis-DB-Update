import firebase_admin
from firebase_admin import credentials, db
from sentiment_analysis.analyzer import analyze_subreddit
from datetime import datetime

# Initialize Firebase
cred = credentials.Certificate("firebase_credentials.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://my-website-517f8-default-rtdb.firebaseio.com'
    })

# List of subreddits to track
subreddits = ['technology', 'science', 'worldnews', 'gaming', 'python']

# Push data for each subreddit
for subreddit in subreddits:
    sentiments, posts = analyze_subreddit(subreddit_name=subreddit)
    today = datetime.now().strftime('%Y-%m-%d')

    ref = db.reference(f'sentiment_trend/{subreddit}/{today}')
    ref.set({
        "sentiments": sentiments,
        "posts": posts
    })

    print(f"🔥 Data pushed for r/{subreddit} on {today}")
