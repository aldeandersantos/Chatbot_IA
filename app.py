import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_API_URL = os.environ.get("GROQ_API_URL", "https://api.groq.com/v1/chat/completions")
MODEL_NAME = os.environ.get("MODEL_NAME", "llama3-70b-8192")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Mensagem não fornecida"}), 400

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": user_message}
        ],
        "max_tokens": 512,
        "temperature": 0.7
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        return jsonify({"error": "Erro na chamada da IA", "details": response.text}), 500

    ai_message = response.json()["choices"][0]["message"]["content"]
    return jsonify({"response": ai_message})

if __name__ == "__main__":
    app.run(debug=True)