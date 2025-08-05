# 🧠 FeelTrack - Emotion Detector using BERT

FeelTrack is a lightweight NLP web app that detects emotions from user input using a fine-tuned BERT model. It processes natural language text and predicts emotional tones like joy, sadness, fear, anger, love, etc., in real-time.

![FeelTrack Demo](https://img.shields.io/badge/BERT-Emotion-blue) ![Status](https://img.shields.io/badge/Status-Prototype-green) ![License](https://img.shields.io/github/LICENSE/Yaswanth876/FeelTrack)

---

## 🚀 Features

- ✨ Detects **multiple emotions** from user text using a mini-BERT model (`boltuix/bert-emotion`)
- 🪶 Lightweight design suitable for hosting on Render, Hugging Face Spaces, or simple VMs
- 📦 Built with **Flask + Bootstrap** for a clean, responsive UI
- 🌐 No external API (e.g., IBM Watson) required — fully open-source and offline-compatible

---

## 🧪 Tech Stack

- **Model**: [`boltuix/bert-emotion`](https://huggingface.co/boltuix/bert-emotion)
- **Backend**: Python, Flask
- **Frontend**: HTML, Bootstrap 4, JavaScript
- **Deployment**: Localhost / Render / Hugging Face Spaces

---

## 📸 Sample Output

> Input:  
> *"I'm feeling hopeful but also scared about the future..."*  
>
> Output:
> - Joy: 0.76  
> - Fear: 0.43  
> - Dominant Emotion: **Joy**

---

## 📁 Project Structure
```
FeelTrack/
├── app.py # Flask backend
├── emotion_detection.py # BERT-based emotion prediction
├── templates/
│ └── index.html # Frontend page
├── static/
│ └── mywebscript.js # JS logic for UI interaction
├── requirements.txt
└── README.md
```

---

## 💻 Local Setup

### 1. Clone the repo
```
git clone https://github.com/Yaswanth876/FeelTrack.git
cd FeelTrack
```
### 2. Create virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Run the app
```
python app.py
```
- Then visit http://127.0.0.1:5000 in your browser.
---

### 🌍 Live Deployment
This app is designed to run on:

- Render
---

### 📌 Roadmap

 - Create mobile-friendly UI

 - Add emoji-based emotion visualizer

 - Log emotion history in a database

 - Add voice input support
 ---
 

### 🤝 Contributing
- Pull requests are welcome! If you find a bug or have a suggestion, feel free to open an issue.
---


### 🙋‍♂️ Author
Made with ❤️ by Yaswanth
- Undergraduate, dreamer, and AI/ML enthusiast building tech to uplift lives.
---

📄 License
- This project is licensed under the MIT License - see the LICENSE file for details.
