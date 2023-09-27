from database import DatabaseConnection

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
        """ Crea un nuevo servidor """

        query = """ INSERT INTO servidor_app.servidores (nombre, descripcion) VALUES (%s) """
        params = (server.nombre, server.descripcion)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def search(cls, server):
        """ Buscador de servidores """

        query = """ SELECT * FROM servidor_app_.servidores WHERE nombre = %s """
        params = (server.nombre)
        result = DatabaseConnection.fetch_one(query, params)
        return result
    
    def get_all_server(cls):
        """ Obtiene todos los servidores existentes """

        query = """ SELECT * FROM servidor_app.servidores """
        params = None
        result = DatabaseConnection.fetch_all(query, params)
        return result