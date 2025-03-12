import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    resp = requests.post(url, headers=headers, json=input_json)
    data = json.loads(resp.text)
    emotions = data['emotionPredictions'][0]['emotion']

    # Store info on dominant emotion
    global dominant_emotion_score
    dominant_emotion_score = -1.0
    global dominant_emotion_name
    dominant_emotion_name = ''

    # Extract value and check for dominance in one
    def check_new_emotion(name):
        val = emotions[name]
        global dominant_emotion_score
        global dominant_emotion_name
        if val > dominant_emotion_score:
            dominant_emotion_score = val
            dominant_emotion_name = name
        return val

    anger_score = check_new_emotion('anger')
    disgust_score = check_new_emotion('disgust')
    fear_score = check_new_emotion('fear')
    joy_score = check_new_emotion('joy')
    sadness_score = check_new_emotion('sadness')

    out =   {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion_name
            }
    return out

# Make callable from console for easy testing
if __name__ == "__main__":
    x = emotion_detector("I am so happy I am doing this")
    print(x)