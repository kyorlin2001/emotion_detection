import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_object = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=input_object, headers=header)

    anger = response.json()['emotionPredictions']['emotion']['anger']
    disgust = response.json()['emotionPredictions']['emotion']['disgust']
    fear = response.json()['emotionPredictions']['emotion']['fear']
    joy = response.json()['emotionPredictions']['emotion']['joy']
    sadness = response.json()['emotionPredictions']['emotion']['sadness']
    dominant_emotion = max(response.json()['emotionPredictions']['emotion'], key = response.json()['emotionPredictions']['emotion'].get)

    retval = {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness, "dominant_emotion": dominant_emotion}

    return retval
