def validate_prediction(model_output, gemini_text):
    """
    Ensures Gemini did NOT modify ML prediction
    """
    gemini_text = gemini_text.lower()

    for disease in model_output:
        if disease.lower() not in gemini_text:
            return False
    return True