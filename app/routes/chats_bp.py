from flask import Blueprint

from ..controllers.chats_controller import ChatController

chat_bp = Blueprint('chat_bp', __name__)

chat_bp.route('/chats/<int:channel_id>', methods=['GET'])(ChatController.get_chat_from_channel)
chat_bp.route('/create/chat', methods=['POST'])(ChatController.create)
chat_bp.route('/update/chat/<int:message_id>', methods=['PUT'])(ChatController.update)
chat_bp.route('/delete/chat/<int:message_id>', methods=['DELETE'])(ChatController.delete)