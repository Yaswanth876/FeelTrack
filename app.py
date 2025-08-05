from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax
import torch

app = Flask(__name__)

# ✅ Load model & tokenizer once — boltuix model
MODEL_NAME = "boltuix/bert-emotion"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# ✅ Manually defined label mapping (since boltuix doesn’t provide it)
id2label = {
    0: "anger",
    1: "fear",
    2: "joy",
    3: "love",
    4: "sadness",
    5: "surprise"
}

# ✅ Max input length supported by the model (tokenizer dependent)
MAX_LEN = tokenizer.model_max_length


# 🔍 Main Emotion Detector Function
def emotion_detector(text):
    if not text or text.strip() == "":
        raise ValueError("Text is empty. Please provide valid input.")

    # Tokenize with truncation
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=MAX_LEN)

    # Run the model
    with torch.no_grad():
        outputs = model(**inputs)
        probs = softmax(outputs.logits, dim=1)[0]

    # Convert to emotion: score dict
    emotion_scores = {id2label[i]: float(probs[i]) for i in range(len(probs))}
    top_emotion = max(emotion_scores, key=emotion_scores.get)

    # Sorted for frontend visualization
    sorted_emotions = dict(sorted(emotion_scores.items(), key=lambda item: item[1], reverse=True))
    sorted_emotions['dominant_emotion'] = top_emotion

    return sorted_emotions


# ✅ Flask Route
@app.route("/emotionDetector", methods=["GET"])
def analyze_emotion():
    try:
        text = request.args.get('textToAnalyze')
        result = emotion_detector(text)
        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": "Emotion detection failed.",
            "details": str(e)
        }), 500


# ✅ Root Route for testing
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "FeelTrack Emotion Detection API is up ✅"})


# ✅ Run server
if __name__ == '__main__':
    app.run(debug=True)
