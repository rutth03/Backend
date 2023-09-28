from flask import Blueprint

from ..controllers.servidores_controller import ServerController

servidor_bp = Blueprint('servidor_bp', __name__)

servidor_bp.route('/servers', methods=['GET'])(ServerController.get_servers)
servidor_bp.route('/create/server', methods=['POST'])(ServerController.create)
servidor_bp.route('/update/server/<int:server_id>', methods=['PUT'])(ServerController.update)
servidor_bp.route('/delete/server/<int:server_id>', methods=['DELETE'])(ServerController.delete)