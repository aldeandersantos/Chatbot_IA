from flask import Flask
from config import Config
from routes.chat import chat_bp
from routes.roles import roles_bp
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY
    CORS(app)
    
    app.register_blueprint(chat_bp)
    app.register_blueprint(roles_bp)
    
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)