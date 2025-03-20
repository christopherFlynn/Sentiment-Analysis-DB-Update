from sentiment_analysis.reddit_client import create_reddit_client
from sentiment_analysis.text_cleaner import clean_text
from sentiment_analysis.sentiment_model import load_model, predict_sentiment
import os
import logging


# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

# Configure logging once at the top of the file
logging.basicConfig(
    filename='logs/sentiment_analysis.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def analyze_subreddit(subreddit_name="technology", post_limit=5, comments_per_post=3):
    reddit = create_reddit_client()
    model, vectorizer = load_model()

    subreddit = reddit.subreddit(subreddit_name)
    sentiments = {"Positive": 0, "Negative": 0}
    post_data = []

    # Inside your function:
    logging.info(f"Analyzing subreddit: {subreddit_name}")

    for post in subreddit.hot(limit=post_limit):
        post.comments.replace_more(limit=0)
        for comment in post.comments.list()[:comments_per_post]:
            cleaned = clean_text(comment.body)
            sentiment = predict_sentiment(cleaned, model, vectorizer)
            sentiments[sentiment] += 1
            post_data.append({
                "title": post.title,
                "cleaned_text": cleaned,
                "sentiment": sentiment
            })
            logging.info(f"Sentiment: {sentiment} for comment: {cleaned[:50]}...")

    return sentiments, post_data