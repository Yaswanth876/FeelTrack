from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector  # ✅ Import from your module

app = Flask(__name__)

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

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "FeelTrack Emotion Detection API is up ✅"})

if __name__ == '__main__':
    app.run(debug=True)
