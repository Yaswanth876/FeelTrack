# emotion_detection.py
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax
import torch

model_name = "boltuix/bert-emotion"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

id2label = {
    0: "anger",
    1: "fear",
    2: "joy",
    3: "love",
    4: "sadness",
    5: "surprise"
}

def emotion_detector(text_to_analyse):
    inputs = tokenizer(
        text_to_analyse,
        return_tensors="pt",
        truncation=True,
        max_length=512,
        padding=True
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probs = softmax(outputs.logits, dim=1)[0]
    emotion_scores = {id2label[i]: float(probs[i]) for i in range(len(probs))}
    sorted_emotions = dict(sorted(emotion_scores.items(), key=lambda item: item[1], reverse=True))
    sorted_emotions['dominant_emotion'] = max(emotion_scores, key=emotion_scores.get)
    return sorted_emotions
