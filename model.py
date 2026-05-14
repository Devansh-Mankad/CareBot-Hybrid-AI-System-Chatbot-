import joblib
from model_loader import load_model , load_encoder , load_features
# LOAD PRE-TRAINED FILES
model = load_model()
le = load_encoder()
FEATURES = load_features()

def predict_disease(symptoms_dict):
    # Convert input to model format
    input_data = [symptoms_dict.get(col, 0) for col in FEATURES]
    # Get probabilities
    probs = model.predict_proba([input_data])[0]
    # Top 3 predictions
    top_indices = probs.argsort()[-3:][::-1]
    results = []
    for i in top_indices:
        results.append({
            "disease": le.inverse_transform([i])[0],
            "confidence": round(probs[i] * 100, 2)
        })
    return results