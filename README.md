# Real-Time Sentiment Analysis with Streamlit & Firebase

This project is a real-time sentiment analysis system that collects Reddit posts, processes them with a custom-trained machine learning model, and visualizes the sentiment trends through an interactive Streamlit web app.

## 🚀 Live Demo

Check out the live demo: [Streamlit Sentiment App](https://sentiment-analysis-db-update-q58r5zr8w9vr8jgi4k53rn.streamlit.app/)

## 📌 Features

- Real-time Reddit post fetching using PRAW
- Sentiment classification with a Logistic Regression model
- Data storage and trend tracking using Firebase Realtime Database
- Interactive visualizations via Streamlit and Plotly
- Track sentiment trends over time for multiple subreddits
- Deployed live using Streamlit Cloud

## 📂 Project Structure

```
SentimentAnalysis/
├── app.py                       # App for local Streamlit testing
├── steamlit_app.py              # Streamlit app
├── firebase_push.py             # Push sentiment data to Firebase
├── sentiment_analysis/
│   ├── analyzer.py             # Fetch and organize Reddit data
│   ├── reddit_client.py        # Load and use Reddit Credentials
│   ├── sentiment_model.py      # Load and use sentiment model
│   ├── text_cleaner.py         # Input raw text, output cleaned and processed
├── models/
│   ├── sentiment_model.joblib  # Trained ML model
│   └── vectorizer.joblib       # TF-IDF vectorizer
├── tests/
│   ├── test_sentiment_model.py
│   └── test_text_cleaner
├── requirements.txt            # Project dependencies
```

## ⚙️ Tech Stack

- **Python**: Data collection, processing, and ML
- **PRAW**: Reddit API wrapper
- **scikit-learn**: Model training and prediction
- **Streamlit**: Interactive frontend and deployment
- **Firebase**: Real-time data storage and retrieval
- **Plotly**: Visualizations (bar and trend line charts)

## 📊 Subreddits Tracked

- r/technology
- r/science
- r/worldnews
- r/gaming
- r/python

## 🧠 Machine Learning Model

- Model: Logistic Regression
- Vectorizer: TF-IDF
- Trained on a labeled sentiment dataset with balanced classes

## 🔧 Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add Firebase credentials (`firebase_credentials.json`) or use Streamlit Secrets for deployment
4. Run the app locally:
   ```bash
   streamlit run app.py
   ```
5. Push data to Firebase (optional for backfilling):
   ```bash
   python firebase_push.py
   ```

## 📈 Future Enhancements

- Allow user-uploaded text for sentiment analysis
- Expand tracked subreddits dynamically
- Deploy a REST API for sentiment classification

## 🧩 Author

Christopher Flynn — Data Scientist
[Portfolio](https://christopherflynn.dev)

---

Feel free to fork, clone, or contribute. Feedback welcome!
