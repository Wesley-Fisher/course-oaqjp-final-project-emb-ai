from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotionDetector():
    query = request.args['text']
    data = emotion_detector(query)

    def format_emot(name, data):
        return f"'{name}': {data[name]}"

    message = f"For the given statement, the system response is " + \
              format_emot('anger', data) + ", " + \
              format_emot('disgust', data) + ", " + \
              format_emot('fear', data) + ", " + \
              format_emot('joy', data) + ", " + \
              format_emot('sadness', data) + f". The dominant emotion is {data['dominant_emotion']}.\n"

    return message, 200


if __name__ == "__main__":
    app.run(debug=True,port=5000)
