from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector  # Your updated function

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")  # Loads the frontend

@app.route("/emotionDetector", methods=["GET"])
def analyze_emotion():
    text = request.args.get("textToAnalyze")
    if not text:
        return jsonify({"error": "Missing 'textToAnalyze' parameter"}), 400

    try:
        result = emotion_detector(text)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Emotion detection failed", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
