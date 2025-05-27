import os
import json
import uuid
from config import Config
from .prompt_service import PromptService


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
        session_file = os.path.join(self.sessions_dir, f"{session_id}.json")
        
        if os.path.exists(session_file):
            with open(session_file, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            system_prompt = self.prompt_service.get_system_prompt(personality_type)
            return [
                {"role": "system", "content": system_prompt}
            ]
    
    def save_messages(self, session_id, messages):
        session_file = os.path.join(self.sessions_dir, f"{session_id}.json")
        with open(session_file, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
