import os
import requests
from flask import Flask, request, jsonify, session
import uuid
from dotenv import load_dotenv
import json

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersecretkey")
load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_API_URL = os.environ.get("GROQ_API_URL", "https://api.groq.com/v1/chat/completions")
MODEL_NAME = os.environ.get("MODEL_NAME", "llama3-70b-8192")
SESSIONS_DIR = os.path.join(os.path.dirname(__file__), "sessions")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Mensagem não fornecida"}), 400

    if not os.path.exists(SESSIONS_DIR):
        os.makedirs(SESSIONS_DIR)

    req_session_id = data.get("session_id")
    if req_session_id:
        session["session_id"] = req_session_id
    elif req_session_id == "":
        session["session_id"] = str(uuid.uuid4())
    elif "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    session_id = session["session_id"]

    session_file = os.path.join(SESSIONS_DIR, f"{session_id}.json")
    if os.path.exists(session_file):
        with open(session_file, "r", encoding="utf-8") as f:
            messages = json.load(f)
    else:
        messages = [
            {"role": "system", "content": "Você é um assistente de IA que faz o papel de um atendente de suporte a nutricionista. Onde vai atender clientes para entender suas necessidades e fornecer orientações nutricionais personalizadas."}
        ]

    messages.append({"role": "user", "content": user_message})

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "max_tokens": 512,
        "temperature": 0.7
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        return jsonify({"error": "Erro na chamada da IA", "details": response.text}), 500

    ai_message = response.json()["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ai_message})

    with open(session_file, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

    return jsonify({"response": ai_message, "session_id": session_id})

if __name__ == "__main__":
    app.run(debug=True)