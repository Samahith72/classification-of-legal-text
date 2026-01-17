import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer


def build_tfidf_vectorizer(
    max_features: int = 5000,
    ngram_range: tuple = (1, 2)
) -> TfidfVectorizer:
    return TfidfVectorizer(
        max_features=max_features,
        ngram_range=ngram_range,
        stop_words="english"
    )


def fit_transform_text(
    texts: list,
    vectorizer: TfidfVectorizer,
    save_path: str = "ml/models/tfidf_vectorizer.pkl"
):
    """
    Fit TF-IDF vectorizer and save it.
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    X = vectorizer.fit_transform(texts)

    with open(save_path, "wb") as f:
        pickle.dump(vectorizer, f)

    return X


def transform_text(
    texts: list,
    load_path: str = "ml/models/tfidf_vectorizer.pkl"
):
    """
    Transform text using saved TF-IDF vectorizer.
    """
    with open(load_path, "rb") as f:
        vectorizer = pickle.load(f)

    return vectorizer.transform(texts)


#TESTING

#Test 1
#if __name__ == "__main__":
 #   sample_texts = [
  #      "supreme court judgment delivered",
   #     "family dispute related to property"
    #]
    #vectorizer = build_tfidf_vectorizer()
    #X = fit_transform_text(sample_texts, vectorizer)
    #print("TF-IDF shape:", X.shape)
