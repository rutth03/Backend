from ..models.servidores import Server
from flask import request

class ServerController:
    """ Server controller class """

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
        """ Crear nuevo servidor """

        data = request.json
        data = ServerController.validar_json_post(data)
        server = Server(**data)
        
        result = Server.search(server)
        if result is False:
            Server.create(server)
            return {'message': 'Servidor creado con exito'}, 201
        else: 
            return ("El nombre del servidor ya se encuentra utilizado")
        
    @classmethod
    def delete(cls, server_id):
        """ Eliminar servidor """

        server = Server(id_servidor=server_id)
        Server.delete(server)
        return {'message': 'Usuario eliminado con exito'}, 204
    
    @classmethod
    def update(cls, server_id):
        """ Actualizar servidor """
        
        data = request.json
        data = ServerController.validar_json_put(data)
        data['id_servidor'] = server_id

        server = Server(**data)

        result = Server.search(server)
        if result is False:
                Server.update(server)
                return {'message': 'Información actualizada con exito'}, 200
        else: 
            return ("El nombre del servidor ya se encuentra utilizado")
        
    @classmethod
    def get_servers(cls):
        """ Obtener todos los servidores creados """

        result = Server.get_all_server()
        return result