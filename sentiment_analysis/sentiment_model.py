import joblib
import os

MODEL_PATH = os.path.join("models", "sentiment_model.pkl")
VECTORIZER_PATH = os.path.join("models", "vectorizer.pkl")

def load_model():
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    return model, vectorizer

def predict_sentiment(text, model, vectorizer):
    vectorized_text = vectorizer.transform([text])
    prediction = model.predict(vectorized_text)
    return "Positive" if prediction == 1 else "Negative"