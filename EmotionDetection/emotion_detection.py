import requests  # Import the requests library to handle HTTP requests
import json # to format response to jsony

def emotion_detector(text_to_analyze):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    json_input = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    
    response = requests.post(url, json = json_input, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text) # response formatted to json

    #extract emotion scores with error handling
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    else:
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
        # print(emotion_scores)

        return emotion_scores  # Return the response as emotion_scores dictionary from the API