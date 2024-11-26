from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text = requests.args.get('textToAnalyze')

    res = emotion_detector(text)

    if res.status_code == 200:
        anger = res['anger']
        disgust = res['disgust']
        fear = res['fear']
        joy = res['joy']
        sadness = res['sadness']
        dominant = res['dominant_emotion']
    elif res.status_code == 500:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant = None
    
    if dominant is None:
        return "Error"
    else:
        return 'For the given statement, the system response is anger:' + anger + 'disgust:' + disgust + 'fear:' + fear + 'joy:' + joy + 'sadness:' + sadness + '. The dominant emotion is:' + dominant

@app.route("/")
def render_index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)