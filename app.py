from flask import Flask
from config import Config
from routes.chat import chat_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY
    
    app.register_blueprint(chat_bp)
    
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)