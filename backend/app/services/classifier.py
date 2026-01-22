import pickle
import numpy as np
from pathlib import Path
from backend.app.services.article_mapping import ARTICLE_MAP

MODEL_DIR = Path(__file__).resolve().parents[2] / "models"

# Load vectorizer
with open(MODEL_DIR / "tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Load model
with open(MODEL_DIR / "svm_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load label encoder
with open(MODEL_DIR / "label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)


def predict_label(text: str):
    """
    Predict legal article and description (with confidence).
    """
    # Transform input text
    X = vectorizer.transform([text])

    # Predict encoded label
    encoded_label = model.predict(X)[0]
    article = label_encoder.inverse_transform([encoded_label])[0]

    # Map to human-readable description
    description = ARTICLE_MAP.get(article, "Unknown Article")

    # --- Confidence estimation (for LinearSVC) ---
    try:
        scores = model.decision_function(X)

        # Softmax for probability-like confidence
        exp_scores = np.exp(scores - np.max(scores))
        probabilities = exp_scores / exp_scores.sum(axis=1, keepdims=True)

        confidence = float(np.max(probabilities)) * 100
    except:
        confidence = None

    return {
        "article": article,
        "description": description,
        "confidence": round(confidence, 2) if confidence is not None else None
    }
