import requests
from config import Config


class GroqService:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.api_url = Config.GROQ_API_URL
        self.model_name = Config.MODEL_NAME
        self.max_tokens = Config.MAX_TOKENS
        self.temperature = Config.TEMPERATURE
    
    def get_ai_response(self, messages):
        if not self.api_key:
            return None, "Chave da API Groq não configurada"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model_name,
            "messages": messages,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }
        
        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            
            if response.status_code != 200:
                return None, f"Erro na chamada da IA: {response.text}"
            
            ai_message = response.json()["choices"][0]["message"]["content"]
            return ai_message, None
            
        except Exception as e:
            return None, f"Erro: {str(e)}"
