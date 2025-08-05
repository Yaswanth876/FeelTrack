from transformers import pipeline

# Load once at the top (loads the model when server starts)
emotion_classifier = pipeline("text-classification", model="boltuix/bert-emotion", return_all_scores=True)

def emotion_detector(text):
    results = emotion_classifier(text)[0]  # It's a list with dicts of label & score
    emotion_scores = {res["label"]: round(res["score"], 3) for res in results}
    
    # Get top emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "emotion": dominant_emotion,
        "emotion_scores": emotion_scores
    }
