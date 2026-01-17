import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text: str) -> str:
    """
    Clean and normalize legal text.
    """
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text


def preprocess_text(text: str) -> str:
    """
    Full preprocessing pipeline.
    """
    text = clean_text(text)
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)



#---- Testing 0f PreProcessing


#test1
#if __name__ == "__main__":
 #   sample = "The Honorable Supreme Court passed the judgment in 2026."
  #  print(preprocess_text(sample))


#tes2
#if __name__ == "__main__":
 #   sample = "The next case is at 2026"
  #  print(preprocess_text(sample))