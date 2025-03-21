from sentiment_analysis.sentiment_model import load_model, predict_sentiment

def test_predict_sentiment():
    model, vectorizer = load_model()
    result = predict_sentiment("This is a great day!", model, vectorizer)
    assert result in ["Positive"]
