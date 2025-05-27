# 🤖 Chatbot Flask + Groq (Llama-3)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green?logo=flask)](https://flask.palletsprojects.com/)
[![Groq API](https://img.shields.io/badge/Groq-API-orange)](https://console.groq.com/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> Chatbot inteligente utilizando Flask e integração com a API Groq (Llama-3). Envie mensagens e receba respostas automáticas de IA via uma API REST simples.

---

## ✨ Funcionalidades

- 🚀 API REST para interação com o chatbot
- 🦙 Integração com o modelo Llama-3 via Groq API
- ⚙️ Configuração fácil via arquivo `.env`

---

## 📦 Requisitos

- Python 3.8+
- Conta e chave de API Groq

---

## 🛠️ Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/aldeandersantos/Chatbot_IA.git
   cd Chatbot_IA
   ```

2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente no arquivo `.env`:
   ```
   GROQ_API_KEY="sua_chave_api_groq"
   GROQ_API_URL="https://api.groq.com/openai/v1/chat/completions"
   MODEL_NAME="llama3-70b-8192"
   ```

---

## ▶️ Como usar

1. Inicie o servidor Flask:
   ```sh
   python app.py
   ```

2. Envie uma requisição POST para `http://localhost:5000/chat` com um JSON contendo a mensagem:

   ```json
   {
     "message": "Olá, tudo bem?"
   }
   ```

   Exemplo usando `curl`:
   ```sh
   curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"message": "Olá, tudo bem?"}'
   ```

3. Você receberá uma resposta JSON com a mensagem da IA:
   ```json
   {
     "response": "Olá! Como posso ajudar você hoje?"
   }
   ```

---

## 📁 Estrutura do Projeto

```
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

<p align="center">
  Feito com ❤️ por <a href="https://github.com/aldeandersantos">Aldeander Santos</a>
</p>