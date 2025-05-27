from flask import Blueprint, request, jsonify, session
from services.groq_service import GroqService
from services.session_service import SessionService
from services.prompt_service import PromptService

chat_bp = Blueprint('chat', __name__)
groq_service = GroqService()
session_service = SessionService()
prompt_service = PromptService()


@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    personality_type = data.get("personality", "nutricionista")

    if not user_message:
        return jsonify({"error": "Mensagem não fornecida"}), 400

    req_session_id = data.get("session_id")
    session_id = session_service.handle_session_id(req_session_id, session)

    messages = session_service.load_messages(session_id, personality_type)
    messages.append({"role": "user", "content": user_message})

    ai_message, error = groq_service.get_ai_response(messages)
    
    if error:
        return jsonify({"error": "Erro na chamada da IA", "details": error}), 500

    messages.append({"role": "assistant", "content": ai_message})
    session_service.save_messages(session_id, messages)

    return jsonify({
        "response": ai_message, 
        "session_id": session_id,
        "personality": personality_type
    })


@chat_bp.route("/personalities", methods=["GET"])
def get_personalities():
    """Retorna as personalidades disponíveis"""
    try:
        personalities = prompt_service.get_available_personalities()
        return jsonify({
            "personalities": personalities,
            "default": "nutricionista"
        })
    except Exception as e:
        return jsonify({"error": "Erro ao carregar personalidades", "details": str(e)}), 500


@chat_bp.route("/personality/<personality_type>", methods=["GET"])
def get_personality_info(personality_type):
    """Retorna informações sobre uma personalidade específica"""
    try:
        prompt = prompt_service.get_system_prompt(personality_type)
        if prompt == prompt_service.get_system_prompt("nutricionista") and personality_type != "nutricionista":
            return jsonify({"error": "Personalidade não encontrada"}), 404
        
        return jsonify({
            "personality": personality_type,
            "system_prompt": prompt
        })
    except Exception as e:
        return jsonify({"error": "Erro ao carregar personalidade", "details": str(e)}), 500
