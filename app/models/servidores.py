from ..database import DatabaseConnection

class Server:
    def __init__(self, id_servidor = None, nombre = None, descripcion = None):
        self.id_servidor = id_servidor
        self.nombre = nombre
        self.descripcion = descripcion

    def serializar(self):
        return {
            "id_servidor": self.id_servidor,
            "nombre": self.nombre,
            "descripción": self.descripcion
        }

    @classmethod
    def create(cls, server):
        """ Crear un nuevo servidor """

        query = """ INSERT INTO servidor_app.servidores (nombre, descripcion) VALUES (%s, %s) """
        params = (server.nombre, server.descripcion)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def search(cls, server):
        """ Buscador de servidores """

        query = """ SELECT * FROM servidor_app.servidores WHERE nombre = %s """
        params = (server.nombre,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is None:
            return False
        else:
            return True
    
    @classmethod
    def get_all_server(cls):
        """ Obtiene todos los servidores existentes """

        query = """ SELECT * FROM servidor_app.servidores """
        params = None
        result = DatabaseConnection.fetch_all(query, params)
        return result
    
    @classmethod
    def delete(cls, server):
        """ Eliminar servidor """

        query = "DELETE FROM servidor_app.servidores WHERE id_servidor = %s"
        params = (server.id_servidor,)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def update(cls, server):
        """ Modificar servidor """

        query = "UPDATE servidor_app.servidores SET nombre = %s, descripcion = %s WHERE id_servidor = %s"
        params = (server.nombre, server.descripcion, server.id_servidor)
        DatabaseConnection.execute_query(query, params)
    
