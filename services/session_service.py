import os
import json
import uuid
from config import Config
from .prompt_service import PromptService
from db.session_storage import save_session, load_session


class SessionService:
    def __init__(self):
        self.sessions_dir = Config.SESSIONS_DIR
        self.prompt_service = PromptService()
        if not os.path.exists(self.sessions_dir):
            os.makedirs(self.sessions_dir)
    
    def handle_session_id(self, req_session_id, flask_session):
        if req_session_id:
            flask_session["session_id"] = req_session_id
        elif req_session_id == "":
            flask_session["session_id"] = str(uuid.uuid4())
        elif "session_id" not in flask_session:
            flask_session["session_id"] = str(uuid.uuid4())
        
        return flask_session["session_id"]
    
    def load_messages(self, session_id, personality_type="nutricionista"):
        system_prompt = self.prompt_service.get_system_prompt(personality_type)
        
        messages = load_session(session_id)
        
        if messages:
            if messages and messages[0]["role"] == "system" and messages[0]["content"] != system_prompt:
                messages[0]["content"] = system_prompt
                self.save_messages(session_id, messages)
            return messages
        else:
            return [
                {"role": "system", "content": system_prompt}            ]
    
    def save_messages(self, session_id, messages):
        save_session(session_id, messages)
