from ..models.canales import Channel
from flask import request

class ChannelController:
    """ Channel controller class """

    @classmethod
    def validar_json_post(cls, data):
        nombre = data.get('nombre')
        descripcion = data.get('descripcion')
        if nombre is not None:
            return data
        
    @classmethod
    def validar_json_put(cls, data):
        nombre = data.get('nombre')
        descripcion = data.get('descripcion')
        if nombre is not None:
            return data
    
    @classmethod
    def create(cls):
        """ Crear nuevo canal """

        data = request.json
        data = ChannelController.validar_json_post(data)
        channel = Channel(**data)
        
        result = Channel.search(channel)
        if result is False:
            Channel.create(channel)
            return {'message': 'Canal creado con exito'}, 201
        else: 
            return ("El nombre del canal ya se encuentra utilizado")
        
    @classmethod
    def delete(cls, channel_id):
        """ Eliminar canal """

        channel = Channel(id_canal=channel_id)
        Channel.delete(channel)
        return {'message': 'Canal eliminado con exito'}, 204
    
    @classmethod
    def update(cls, channel_id):
        """ Actualizar canal """
        
        data = request.json
        data = ChannelController.validar_json_put(data)
        data['id_canal'] = channel_id

        channel = Channel(**data)

        result = Channel.search(channel)
        if result is False:
                Channel.update(channel)
                return {'message': 'Información actualizada con exito'}, 200
        else: 
            return ("El nombre del canal ya se encuentra utilizado")
        
    @classmethod
    def get_channels_from_server(cls, server_id):
        """ Obtener todos los canales de un servidor """

        channel = Channel(servidor=server_id)
        result = Channel.get_all_channels_from_server(channel)
        return result
