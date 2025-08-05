from transformers import pipeline

emotion_classifier = pipeline("text-classification", model="boltuix/bert-emotion", top_k=None)

def emotion_detector(text):
    results = emotion_classifier(text)[0]  
    emotion_scores = {res["label"]: round(res["score"], 3) for res in results}

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "dominant_emotion": dominant_emotion,
        "emotion_scores": emotion_scores
    }
