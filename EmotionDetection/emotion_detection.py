import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_object = {"raw_document": {"text": text_to_analyse } }
    response = requests.post(url, json=input_object, headers=header)

    formatted_response = json.loads(response.text)

    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = response.json()['emotionPredictions'][0]['emotion']['disgust']
    fear = response.json()['emotionPredictions'][0]['emotion']['fear']
    joy = response.json()['emotionPredictions'][0]['emotion']['joy']
    sadness = response.json()['emotionPredictions'][0]['emotion']['sadness']
    dominant_emotion = max(response.json()['emotionPredictions'][0]['emotion'], key=response.json()['emotionPredictions'][0]['emotion'].get)

    retval = {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness, "dominant_emotion": dominant_emotion}

    return retval
