from ..models.usuarios_servidores import RelationUserServer
from flask import request

class UserServerController:
    """ Relation User-Server controller class """

    @classmethod
    def create(cls):
        """ Crear relación """

        data = request.json
        user_server = RelationUserServer(**data)
        RelationUserServer.create_relation(user_server)
        return {'message': 'Relación creada con exito'}, 201