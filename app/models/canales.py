from database import DatabaseConnection

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

        query = """ INSERT INTO servidor_app.canales (nombre, servidor) VALUES (%s, %s) """
        params = (channel.nombre, channel.servidor)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_all_channels_from_server(cls, channel):
        """ Obtiene todos los canales de un servidor """
        
        query = """ SELECT nombre FROM servidor_app.canales WHERE servidor = %s """
        params = (channel.servidor, )
        result = DatabaseConnection.fetch_all(query, params)
        return result