import joblib
import os


# Get absolute path to current file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one level to project root, then into 'models'
MODEL_PATH = os.path.join(BASE_DIR, '..', 'models', 'sentiment_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, '..', 'models', 'vectorizer.pkl')

# Resolve to absolute path
MODEL_PATH = os.path.abspath(MODEL_PATH)
VECTORIZER_PATH = os.path.abspath(VECTORIZER_PATH)

def load_model():
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    return model, vectorizer

def predict_sentiment(text, model, vectorizer):
    vectorized_text = vectorizer.transform([text])
    prediction = model.predict(vectorized_text)
    return "Positive" if prediction == 1 else "Negative"