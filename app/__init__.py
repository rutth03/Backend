from flask import Flask
from config import Config

from .routes.usuarios_bp import usuario_bp
from .routes.servidores_bp import servidor_bp
from .routes.usuarioServidor_bp import usuarioServer_bp
from .routes.canales_bp import canal_bp
from .routes.chats_bp import chat_bp

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)

    app.config.from_object(Config)
    
    app.register_blueprint(usuario_bp)
    app.register_blueprint(servidor_bp)
    app.register_blueprint(usuarioServer_bp)
    app.register_blueprint(canal_bp)
    app.register_blueprint(chat_bp)

    return app