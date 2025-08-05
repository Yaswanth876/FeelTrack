from transformers import pipeline

# Load once at the top (loads the model when server starts)
emotion_classifier = pipeline("text-classification", model="boltuix/bert-emotion", return_all_scores=True)

def emotion_detector(text):
    results = emotion_classifier(text)[0]  # List of dicts: {'label': ..., 'score': ...}
    emotion_scores = {res["label"]: round(res["score"], 3) for res in results}

    # Get top emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "dominant_emotion": dominant_emotion,  # <-- IMPORTANT: use this key
        "emotion_scores": emotion_scores
    }
