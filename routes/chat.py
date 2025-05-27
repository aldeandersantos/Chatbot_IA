from flask import Blueprint, request, jsonify, session
from services.groq_service import GroqService
from services.session_service import SessionService

chat_bp = Blueprint('chat', __name__)
groq_service = GroqService()
session_service = SessionService()


@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Mensagem não fornecida"}), 400

    req_session_id = data.get("session_id")
    session_id = session_service.handle_session_id(req_session_id, session)

    messages = session_service.load_messages(session_id)
    messages.append({"role": "user", "content": user_message})

    ai_message, error = groq_service.get_ai_response(messages)
    
    if error:
        return jsonify({"error": "Erro na chamada da IA", "details": error}), 500

    messages.append({"role": "assistant", "content": ai_message})
    session_service.save_messages(session_id, messages)

    return jsonify({"response": ai_message, "session_id": session_id})
