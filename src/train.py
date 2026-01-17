import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

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
    Split dataset into train and test sets.
    Uses stratified split only if all classes have >= 2 samples.
    """
    X = df["clean_text"]
    y = df["label_encoded"]

    class_counts = y.value_counts()

    if class_counts.min() < 2:
        print("⚠️ Warning: Some classes have less than 2 samples. Using non-stratified split.")
        return train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

    return train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )



if __name__ == "__main__":
    dataset_path = "data/raw/legal_dataset.csv"

    df = load_dataset(dataset_path)
    df, label_encoder = prepare_data(df)

    X_train, X_test, y_train, y_test = split_data(df)

    print("Train size:", len(X_train))
    print("Test size:", len(X_test))
