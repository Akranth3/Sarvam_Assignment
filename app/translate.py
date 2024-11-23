import requests
import json

def translate(text):

    url = "https://api.sarvam.ai/translate"

    payload = {
        "input": text,
        "source_language_code": "en-IN",
        "target_language_code": "hi-IN",
        "speaker_gender": "Male",
        "mode": "formal",
        "model": "mayura:v1",
        "enable_preprocessing": True
    }
    headers = {"Content-Type": "application/json", "api-subscription-key":"a4d97b92-9fbd-4346-8870-178df79b1515"}

    response = requests.request("POST", url, json=payload, headers=headers)
    ans_json = json.loads(response.text)

    return ans_json['translated_text']