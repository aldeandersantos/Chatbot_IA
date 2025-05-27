from flask import Blueprint, request, jsonify
import os
import json
from config import Config

roles_bp = Blueprint('roles', __name__)

def validate_bearer_token():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return False, jsonify({"error": "Header Authorization é obrigatório"}), 401
    
    if not auth_header.startswith('Bearer '):
        return False, jsonify({"error": "Token deve ser enviado como 'Bearer <token>'"}), 401
    
    token = auth_header.replace('Bearer ', '', 1)
    if not token:
        return False, jsonify({"error": "Token não pode estar vazio"}), 401
    
    env_token = os.environ.get("UPDATE_TOKEN")
    if not env_token:
        return False, jsonify({"error": "Token de atualização não configurado no servidor"}), 500
    
    if token != env_token:
        return False, jsonify({"error": "Token inválido"}), 401
    
    return True, None

@roles_bp.route("/updateia/roles", methods=["POST", "PUT"])
def update_roles():
    """
    Endpoint para atualizar/criar o arquivo roles.json
    Requer Bearer Token no header Authorization
    """
    # Validar Bearer Token
    is_valid, error_response = validate_bearer_token()
    if not is_valid:
        return error_response
    
    # Verificar se há conteúdo JSON no body
    try:
        content = request.get_json()
        if content is None:
            return jsonify({"error": "Conteúdo JSON é obrigatório"}), 400
    except Exception as e:
        return jsonify({"error": "JSON inválido", "details": str(e)}), 400
    
    # Caminho do arquivo
    roles_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ia_roles", "roles.json")
    
    # Verificar se o arquivo existe para determinar o método
    file_exists = os.path.exists(roles_file_path)
    
    try:
        # Criar diretório se não existir
        os.makedirs(os.path.dirname(roles_file_path), exist_ok=True)
        
        # Escrever o arquivo
        with open(roles_file_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
        
        action = "atualizado" if file_exists else "criado"
        return jsonify({
            "message": f"Arquivo roles.json {action} com sucesso",
            "action": action,
            "file_path": roles_file_path
        }), 200
        
    except Exception as e:
        return jsonify({"error": "Erro ao salvar arquivo", "details": str(e)}), 500


@roles_bp.route("/updateia/personality", methods=["POST", "PUT"])
def update_personality():
    """
    Endpoint para atualizar/criar o arquivo personality.json
    Requer Bearer Token no header Authorization
    """
    # Validar Bearer Token
    is_valid, error_response = validate_bearer_token()
    if not is_valid:
        return error_response
    
    # Verificar se há conteúdo JSON no body
    try:
        content = request.get_json()
        if content is None:
            return jsonify({"error": "Conteúdo JSON é obrigatório"}), 400
    except Exception as e:
        return jsonify({"error": "JSON inválido", "details": str(e)}), 400
    
    # Caminho do arquivo
    personality_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ia_roles", "personality.json")
    
    # Verificar se o arquivo existe para determinar o método
    file_exists = os.path.exists(personality_file_path)
    
    try:
        # Criar diretório se não existir
        os.makedirs(os.path.dirname(personality_file_path), exist_ok=True)
        
        # Escrever o arquivo
        with open(personality_file_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
        
        action = "atualizado" if file_exists else "criado"
        return jsonify({
            "message": f"Arquivo personality.json {action} com sucesso",
            "action": action,
            "file_path": personality_file_path
        }), 200
        
    except Exception as e:
        return jsonify({"error": "Erro ao salvar arquivo", "details": str(e)}), 500