from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector  # Your model function

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")  # Serve the HTML page

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

if __name__ == '__main__':
    app.run(debug=True)
