from flask import Blueprint

from ..controllers.usuarios_controller import UserController

usuario_bp = Blueprint('usuario_bp', __name__)

usuario_bp.route('/logIn', methods=['GET'])(UserController.log_in)
usuario_bp.route('/logOut',methods=['GET'])(UserController.log_out)
usuario_bp.route('/servers/<int:user_id>', methods=['GET'])(UserController.get_all_servers)
usuario_bp.route('/info/<int:user_id>', methods=['GET'])(UserController.get_info_user)
usuario_bp.route('/signIn', methods=['POST'])(UserController.create)
usuario_bp.route('/<int:user_id>', methods=['PUT'])(UserController.update)
usuario_bp.route('/<int:user_id>', methods=['DELETE'])(UserController.delete)