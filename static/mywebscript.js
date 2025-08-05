let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value.trim();

    if (!textToAnalyze) {
        document.getElementById("system_response").innerHTML =
            "<div class='alert alert-warning'>⚠️ Please enter some text to analyze.</div>";
        return;
    }

    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200) {
                try {
                    const result = JSON.parse(xhttp.responseText);

                    const emotionScores = result.emotion_scores || {};
                    let emotionsList = "";

                    for (const [emotion, score] of Object.entries(emotionScores)) {
                        emotionsList += `<li>${emotion.charAt(0).toUpperCase() + emotion.slice(1)}: ${score.toFixed(3)}</li>`;
                    }

                    const responseHTML = `
                        <div class="card mt-4 p-3">
                            <h4><strong>Dominant Emotion:</strong> ${result.dominant_emotion?.toUpperCase()}</h4>
                            <ul>${emotionsList}</ul>
                        </div>`;
                    
                    document.getElementById("system_response").innerHTML = responseHTML;
                } catch (err) {
                    document.getElementById("system_response").innerHTML =
                        "<div class='alert alert-danger'>❌ Invalid response format from server.</div>";
                }
            } else {
                document.getElementById("system_response").innerHTML =
                    "<div class='alert alert-danger'>❌ Error: Unable to get response from the server.</div>";
            }
        }
    };

    xhttp.open("GET", `/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`, true);
    xhttp.send();
};
