from flask import Blueprint

from ..controllers.usuarioServidor_controller import UserServerController

usuarioServer_bp = Blueprint('usuarioServer_bp', __name__)

usuarioServer_bp.route('/userServer/create', methods=['POST'])(UserServerController.create)