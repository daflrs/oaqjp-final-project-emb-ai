import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json = myobj, headers=headers)
    new_resp = json.loads(response.text)
    if response.status_code == 200:
        emo_predictions = new_resp['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emo_predictions, key=emo_predictions.get)
    elif response.status_code == 400:
        emo_predictions = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None}
        dominant_emotion = None
    emo_predictions['dominant_emotion'] = dominant_emotion
    return emo_predictions