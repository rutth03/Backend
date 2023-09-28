from ..models.chats import Chats
from flask import request

class ChatController:
    """ Chat controller class """

    @classmethod
    def validar_json_post(cls, data):
        mensaje = data.get('mensaje')
        if mensaje is not None:
            return data
        
    @classmethod
    def validar_json_put(cls, data):
        mensaje = data.get('mensaje')
        if mensaje is not None:
            return data

    @classmethod
    def create(cls):
        data = request.json
        data = ChatController.validar_json_post(data)
        mensaje = Chats(**data)
        Chats.new_message(mensaje)
        return {'message': 'Mensaje enviado'}, 201

    @classmethod
    def update(cls, message_id):
        data = request.json
        data = ChatController.validar_json_put(data)
        data['id_mensaje'] = message_id

        mensaje = Chats(**data)

        Chats.update_message(mensaje)
        return {'message': 'Mensaje modificado'}, 200

    @classmethod
    def delete(cls, message_id, user_id):
        """ Eliminar mensaje """

        mensaje = Chats(id_mensaje=message_id, usuario=user_id)
        Chats.delete_message(mensaje)
        return {'message': 'Mensaje eliminado'}, 204

    @classmethod
    def get_chat_from_channel(cls, channel_id):
        """ Obtener todos los mensajes de un canal """

        chat = Chats(canal=channel_id)
        result = Chats.get_all_messages(chat)
        return result