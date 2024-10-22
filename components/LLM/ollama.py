import json
import requests
from requests.exceptions import HTTPError


class OllamaLLM:
    def __init__(self, model):
        self.model = model
        self.url = "http://ollama:11434/api/generate"
        self.headers = {
            'Content-Type': 'application/json',
        }

    def generate_response(self, prompt):
        
        data = {
        "model": self.model,
        "stream": False,
        "prompt": prompt,
        }

        response = requests.post(self.url, 
                             headers=self.headers, 
                             data=json.dumps(data))

        if response.status_code == 200:
            response_text = response.text
            data = json.loads(response_text)
            actual_response = data["response"]
            print("Response: ", actual_response)
        else:
            print("Error:", response.status_code, response.text)    