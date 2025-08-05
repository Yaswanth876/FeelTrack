from transformers import pipeline

# ✅ Updated usage with top_k=None (returns all emotion scores)
emotion_classifier = pipeline("text-classification", model="boltuix/bert-emotion", top_k=None)

def emotion_detector(text):
    results = emotion_classifier(text)[0]  # List of dicts: {'label': ..., 'score': ...}
    emotion_scores = {res["label"]: round(res["score"], 3) for res in results}

    # Get dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "dominant_emotion": dominant_emotion,
        "emotion_scores": emotion_scores
    }
