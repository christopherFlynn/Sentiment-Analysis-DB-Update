import streamlit as st
import pandas as pd
import plotly.express as px
import firebase_admin
from firebase_admin import credentials, db
import json
from datetime import datetime

# Firebase setup
cred = credentials.Certificate("firebase_credentials.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://my-website-517f8-default-rtdb.firebaseio.com'
    })

# Subreddit selection
st.title("📊 Real-Time Sentiment Analysis")
subreddits = ['technology', 'science', 'worldnews', 'gaming', 'python']
selected_subreddit = st.selectbox("Choose a subreddit:", subreddits)

# Fetch trend data for selected subreddit
ref = db.reference(f'sentiment_trend/{selected_subreddit}')
trend_data = ref.get()

if trend_data:
    dates = []
    positive_counts = []
    negative_counts = []
    posts_today = []

    for date, data in sorted(trend_data.items()):
        dates.append(date)
        positive_counts.append(data['sentiments']['Positive'])
        negative_counts.append(data['sentiments']['Negative'])
        if date == datetime.now().strftime('%Y-%m-%d'):
            posts_today = data['posts']

    # Trend DataFrame
    df_trend = pd.DataFrame({
        'Date': pd.to_datetime(dates),
        'Positive': positive_counts,
        'Negative': negative_counts
    })

    # Bar Chart (Today)
    st.subheader(f"Today's Sentiment in r/{selected_subreddit}")
    if posts_today:
        today_sentiments = {
            'Positive': sum(1 for post in posts_today if post['sentiment'] == 'Positive'),
            'Negative': sum(1 for post in posts_today if post['sentiment'] == 'Negative')
        }

        bar_data = pd.DataFrame({
            'Sentiment': list(today_sentiments.keys()),
            'Count': list(today_sentiments.values())
        })
        fig_bar = px.bar(bar_data, x='Sentiment', y='Count', color='Sentiment')
        st.plotly_chart(fig_bar)

        # Posts List
        st.subheader("Today's Posts")
        for post in posts_today:
            st.markdown(f"**{post['title']}**")
            st.markdown(post['cleaned_text'])
            st.markdown(f"*Sentiment: {post['sentiment']}*")
            st.markdown("---")

    # Trend Line
    st.subheader(f"Sentiment Trend Over Time in r/{selected_subreddit}")
    fig_line = px.line(df_trend, x='Date', y=['Positive', 'Negative'],
                       labels={'value': 'Count', 'variable': 'Sentiment'})
    st.plotly_chart(fig_line)

else:
    st.warning(f"No data found for r/{selected_subreddit}. Try running the sentiment analysis script.")
