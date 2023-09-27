from database import DatabaseConnection

class Chats:
    def __init__(self, id_mensaje = None, mensaje = None, fecha = None, hora = None, usuario = None, canal = None):
        self.id_mensaje = id_mensaje
        self.mensaje = mensaje
        self.fecha = fecha
        self.hora = hora
        self.usuario = usuario
        self.canal = canal
    
    def serializar(self):
        return {
            "id_mensaje": self.id_mensaje,
            "mensaje": self.mensaje,
            "fecha": self.fecha,
            "hora": self.hora,
            "usuario": self.usuario,
            "canal": self.canal,
        }

    @classmethod
    def get_all_messages(cls, chat):
        """ Obtiene todos los mensajes escritos dentro de un canal """

        query = """ SELECT mensaje FROM servidor_app.chats WHERE canal = %s ORDER BY fecha, hora DESC """
        params = (chat.canal,)
        result = DatabaseConnection.fetch_all(query, params)
        return result
        
    @classmethod
    def new_message(cls, chat):
        """ Crea un nuevo mensaje """

        query = """ INSERT INTO sevidor_app.chats (mensaje, fecha, hora, usuario, canal) VALUES (%s, %s, %s, %s, %s) """
        params = (chat.mensaje, chat.fecha, chat.hora, chat.usuario, chat.canal)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def delete_message(cls, chat):
        """ Borrar mensaje "escrito por el usuario """

        query = """ DELETE * FROM servidor_app.chats WHERE id_mensaje=%s AND usuario=%s """
        params = (chat.id_mensaje, chat.usuario)
        DatabaseConnection.execute_query(query, params)
