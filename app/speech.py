import requests

url = "https://api.sarvam.ai/text-to-speech"

payload = {
    "inputs": [text], 
    "target_language_code": "hi-IN",
    "speaker": "meera",
    "pitch": 0,
    "pace": 1.65,
    "loudness": 1.5,
    "speech_sample_rate": 8000,
    "enable_preprocessing": True,
    "model": "bulbul:v1"
}
headers = {"Content-Type": "application/json", "api-subscription-key":"a4d97b92-9fbd-4346-8870-178df79b1515"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response)