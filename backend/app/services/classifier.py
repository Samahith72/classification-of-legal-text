import pickle
from pathlib import Path

MODEL_DIR = Path(__file__).resolve().parents[2] / "models"

with open(MODEL_DIR / "tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open(MODEL_DIR / "svm_model.pkl", "rb") as f:
    model = pickle.load(f)

with open(MODEL_DIR / "label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)


def predict_label(text: str) -> str:
    """
    Predict legal category for given text.
    """
    X = vectorizer.transform([text])
    encoded_label = model.predict(X)[0]
    decoded_label = label_encoder.inverse_transform([encoded_label])[0]
    return decoded_label
