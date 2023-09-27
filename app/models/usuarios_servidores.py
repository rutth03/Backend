from ..database import DatabaseConnection

class RelationUserServer:
    def __init__(self, usuario=None, servidor=None):
        self.usuario = usuario
        self.servidor = servidor
    
    def serializar(self):
        return {
        "usuario": self.usuario,
        "servidor": self.servidor,
        }

    @classmethod
    def create_relation(cls, relation):
        """ Crear relación usuario-servidor """

        query = """ INSERT INTO servidor_app.usuarios_servidores (usuario, servidor) VALUES (%s,%s) """
        params = (relation.usuario, relation.servidor)
        DatabaseConnection.execute_query(query, params)