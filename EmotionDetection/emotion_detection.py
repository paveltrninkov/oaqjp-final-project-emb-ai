import requests
import json
    
def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    obj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = obj, headers = header)

    formatted_res = json.loads(response.text)

    anger = formatted_res['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_res['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_res['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_res['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_res['emotionPredictions'][0]['emotion']['sadness']
    dominant = sorted(formatted_res['emotionPredictions'][0]['emotion'], key = lambda x: x[1])[-1]

    return {'anger' : anger, 'disgust' : disgust, 'fear' : fear, 'joy': joy, 'sadness' : sadness, 'dominant_emotion' : dominant}


