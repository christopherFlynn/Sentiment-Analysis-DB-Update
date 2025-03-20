import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import os

# Initialize Firebase (run only once)
def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("firebase_credentials.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://my-website-517f8-default-rtdb.firebaseio.com/'
        })

# Push sentiment data
def push_data_to_firebase(sentiments, post_data):
    init_firebase()
    ref = db.reference('sentiment_trend')

    today = datetime.now().strftime('%Y-%m-%d')

    ref.child(today).set({
        "sentiments": sentiments,
        "posts": post_data
    })
    print(f"Data for {today} pushed to Firebase!")

# Example usage (tie into your main script)
if __name__ == "__main__":
    from sentiment_analysis.analyzer import analyze_subreddit

    sentiments, post_data = analyze_subreddit()
    push_data_to_firebase(sentiments, post_data)
