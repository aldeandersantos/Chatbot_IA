import json
import os
from config import Config

class PromptService:
    def __init__(self):
        self.ia_roles_dir = os.path.join(os.path.dirname(__file__), "..", "ia_roles")
        self.roles_file = os.path.join(self.ia_roles_dir, "roles.json")
        self.personality_file = os.path.join(self.ia_roles_dir, "personality.json")
        
        self._roles_data = None
        self._personality_data = None
    
    def _load_roles(self):
        if self._roles_data is None:
            try:
                with open(self.roles_file, "r", encoding="utf-8") as f:
                    self._roles_data = json.load(f)
            except FileNotFoundError:
                self._roles_data = {"general_rules": [], "conversation_guidelines": {}, "ethical_constraints": []}
        return self._roles_data
    
    def _load_personalities(self):
        if self._personality_data is None:
            try:
                with open(self.personality_file, "r", encoding="utf-8") as f:
                    self._personality_data = json.load(f)
            except FileNotFoundError:
                self._personality_data = {}
        return self._personality_data
    
    def get_system_prompt(self, personality_type="nutricionista"):
        roles_data = self._load_roles()
        personalities_data = self._load_personalities()
        
        general_rules = roles_data.get("general_rules", [])
        conversation_guidelines = roles_data.get("conversation_guidelines", {})
        ethical_constraints = roles_data.get("ethical_constraints", [])
        
        personality = personalities_data.get(personality_type, {})
        
        if not personality:
            return Config.SYSTEM_PROMPT
        
        prompt_parts = []
        
        prompt_parts.append(f"Você é um {personality.get('role', 'assistente de IA')}.")
        prompt_parts.append(personality.get('description', ''))
        
        if personality.get('expertise'):
            prompt_parts.append("\\n**Suas áreas de especialização incluem:**")
            for expertise in personality['expertise']:
                prompt_parts.append(f"- {expertise}")
        
        if personality.get('personality_traits'):
            prompt_parts.append("\\n**Como assistente, você deve ser:**")
            for trait in personality['personality_traits']:
                prompt_parts.append(f"- {trait}")
        
        if general_rules:
            prompt_parts.append("\\n**Regras gerais que você deve sempre seguir:**")
            for rule in general_rules:
                prompt_parts.append(f"- {rule}")
        
        if conversation_guidelines:
            prompt_parts.append("\\n**Diretrizes de conversa:**")
            for key, value in conversation_guidelines.items():
                prompt_parts.append(f"- {key.replace('_', ' ').title()}: {value}")
        
        if ethical_constraints:
            prompt_parts.append("\\n**Restrições éticas importantes:**")
            for constraint in ethical_constraints:
                prompt_parts.append(f"- {constraint}")
        
        if personality.get('typical_interactions'):
            prompt_parts.append("\\n**Suas interações típicas incluem:**")
            for interaction in personality['typical_interactions']:
                prompt_parts.append(f"- {interaction}")
        
        return " ".join(prompt_parts)
    
    def get_available_personalities(self):
        personalities_data = self._load_personalities()
        return list(personalities_data.keys())
    
    def add_personality(self, personality_type, personality_data):
        personalities_data = self._load_personalities()
        personalities_data[personality_type] = personality_data
        
        with open(self.personality_file, "w", encoding="utf-8") as f:
            json.dump(personalities_data, f, ensure_ascii=False, indent=2)
        
        self._personality_data = None
    
    def update_roles(self, new_roles_data):
        with open(self.roles_file, "w", encoding="utf-8") as f:
            json.dump(new_roles_data, f, ensure_ascii=False, indent=2)
        
        self._roles_data = None
