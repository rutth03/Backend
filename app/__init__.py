from flask import Flask
from config import Config

from .routes.usuarios_bp import usuario_bp

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)

    app.config.from_object(Config)
    app.register_blueprint(usuario_bp)

    return app