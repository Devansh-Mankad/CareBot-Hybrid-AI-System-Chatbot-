import re
import joblib
from langdetect import detect

# Load feature names EXACTLY as in dataset
FEATURES = joblib.load("features.pkl")

# Language detection
def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

# Clean text
def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    return text

# Extract symptoms
def extract_symptoms(user_query):
    text = normalize_text(user_query)

    symptom_dict = {}
    for feature in FEATURES:
        feature_clean = feature.lower()

        # Remove commas and special chars from feature name
        feature_clean = re.sub(r"[^a-zA-Z\s]", " ", feature_clean)
        words = feature_clean.split()
        # Match if MOST words exist (not strict all)
        match_count = sum(1 for w in words if w in text)

        if len(words) > 0 and (match_count / len(words)) >= 0.6:
            symptom_dict[feature] = 1
        else:
            symptom_dict[feature] = 0

    return symptom_dict