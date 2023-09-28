from flask import Blueprint

from ..controllers.canales_controller import ChannelController

canal_bp = Blueprint('canal_bp', __name__)

canal_bp.route('/channels/<int:server_id>', methods=['GET'])(ChannelController.get_channels_from_server)
canal_bp.route('/create/channel', methods=['POST'])(ChannelController.create)
canal_bp.route('/update/channel/<int:channel_id>', methods=['PUT'])(ChannelController.update)
canal_bp.route('/delete/channel/<int:channel_id>', methods=['DELETE'])(ChannelController.delete)