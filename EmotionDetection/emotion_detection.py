from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax
import torch

# ✅ Load smaller BERT model and tokenizer only once
model_name = "boltuix/bert-emotion"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# ✅ Manually define label mapping (boltuix model doesn't have it in config)
id2label = {
    0: "anger",
    1: "fear",
    2: "joy",
    3: "love",
    4: "sadness",
    5: "surprise"
}

def emotion_detector(text_to_analyse):
    # ✅ Tokenize input text with proper truncation and padding
    inputs = tokenizer(
        text_to_analyse,
        return_tensors="pt",
        truncation=True,
        max_length=512,
        padding=True
    )

    # ✅ Run input through the model
    with torch.no_grad():  # Ensures faster inference without tracking gradients
        outputs = model(**inputs)

    # ✅ Convert logits to probabilities
    probs = softmax(outputs.logits, dim=1)[0]

    # ✅ Map predictions to emotion labels
    emotion_scores = {id2label[i]: float(probs[i]) for i in range(len(probs))}

    # ✅ Sort emotions by confidence score
    sorted_emotions = dict(sorted(emotion_scores.items(), key=lambda item: item[1], reverse=True))

    # ✅ Add dominant emotion
    top_emotion = max(emotion_scores, key=emotion_scores.get)
    sorted_emotions['dominant_emotion'] = top_emotion

    return sorted_emotions
