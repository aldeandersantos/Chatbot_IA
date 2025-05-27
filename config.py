import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "supersecretkey")
    DEBUG = True
    
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    GROQ_API_URL = os.environ.get("GROQ_API_URL", "https://api.groq.com/v1/chat/completions")
    MODEL_NAME = os.environ.get("MODEL_NAME", "llama3-70b-8192")
    
    MAX_TOKENS = 512
    TEMPERATURE = 0.7
    
    SESSIONS_DIR = os.path.join(os.path.dirname(__file__), "sessions")
    
    SYSTEM_PROMPT = (
        "Você é um assistente de IA que faz o papel de um atendente de suporte a nutricionista. "
        "Onde vai atender clientes para entender suas necessidades e fornecer orientações "
        "nutricionais personalizadas."
    )
