import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from evaluate import evaluate_model


from feature_extraction import build_tfidf_vectorizer, fit_transform_text, transform_text


from preprocessing import preprocess_text


def load_dataset(csv_path: str):
    """
    Load legal text dataset from CSV file.
    """
    df = pd.read_csv(csv_path)

    if "text" not in df.columns or "label" not in df.columns:
        raise ValueError("Dataset must contain 'text' and 'label' columns")

    return df


def prepare_data(df):
    """
    Preprocess text and encode labels.
    """
    df["clean_text"] = df["text"].apply(preprocess_text)

    label_encoder = LabelEncoder()
    df["label_encoded"] = label_encoder.fit_transform(df["label"])

    return df, label_encoder


def split_data(df, test_size=0.2, random_state=42):
    """
    Split dataset into train and test sets with safety checks
    for small datasets.
    """
    X = df["clean_text"]
    y = df["label_encoded"]

    num_classes = y.nunique()
    num_samples = len(df)

    # Minimum test samples needed for stratification
    min_test_samples = num_classes

    # Compute actual test size in samples
    test_samples = int(num_samples * test_size)

    # Adjust test_size if dataset is too small
    if test_samples < min_test_samples:
        test_size = min_test_samples / num_samples
        print(
            f"⚠️ Adjusted test_size to {test_size:.2f} "
            f"to support {num_classes} classes."
        )

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )



if __name__ == "__main__":
    dataset_path = "data/raw/legal_dataset.csv"

    # Load & prepare data
    df = load_dataset(dataset_path)
    df, label_encoder = prepare_data(df)

    # Split
    X_train, X_test, y_train, y_test = split_data(df)

    # TF-IDF
    vectorizer = build_tfidf_vectorizer()
    X_train_tfidf = fit_transform_text(X_train.tolist(), vectorizer)
    X_test_tfidf = transform_text(X_test.tolist())

    # Train SVM model
    # Train SVM model (only if at least 2 classes exist)
    if len(set(y_train)) < 2:
        raise ValueError(
            "Training data has only one class. "
            "Please ensure at least 2 samples per class."
        )

    model = LinearSVC()
    model.fit(X_train_tfidf, y_train)


    # Predictions
    y_pred = model.predict(X_test_tfidf)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    #print(f"SVM Test Accuracy: {accuracy:.4f}")

    # Predictions
    y_pred = model.predict(X_test_tfidf)

    # Evaluation
    evaluate_model(y_test, y_pred, label_names=label_encoder.classes_)


