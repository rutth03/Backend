from ..database import DatabaseConnection

class Channel:
    def __init__(self, id_canal = None, nombre = None, descripcion = None, servidor = None):
        self.id_canal = id_canal 
        self.nombre = nombre 
        self.descripcion = descripcion
        self.servidor = servidor

    def serializar(self):
        return {
            "id_canal": self.id_canal,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "servidor": self.servidor
        }

    @classmethod
    def create(cls, channel):
        """ Crea un nuevo canal """

        query = """ INSERT INTO servidor_app.canales (nombre, descripcion, servidor) VALUES (%s, %s, %s) """
        params = (channel.nombre, channel.descripcion, channel.servidor)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def delete(cls, channel):
        """ Eliminar canal """

        query = "DELETE FROM servidor_app.canales WHERE id_canal = %s"
        params = (channel.id_canal,)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def update(cls, channel):
        """ Modificar canal """

        query = "UPDATE servidor_app.canales SET nombre = %s, descripcion = %s WHERE id_canal = %s"
        params = (channel.nombre, channel.descripcion, channel.id_canal)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_all_channels_from_server(cls, channel):
        """ Obtiene todos los canales de un servidor """
        
        query = """ SELECT id_canal, nombre, descripcion FROM servidor_app.canales WHERE servidor = %s """
        params = (channel.servidor,)
        result = DatabaseConnection.fetch_all(query, params)
        return result
    
    @classmethod
    def search(cls, channel):
        """ Buscador de canales """

        query = """ SELECT * FROM servidor_app.canales WHERE nombre = %s """
        params = (channel.nombre,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is None:
            return False
        else:
            return True