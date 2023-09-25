from database import DatabaseConnection

class User:
    def __init__(self, id_usuario = None, email = None, contraseña = None, nombre = None,  apellido = None,  loggin = None, cumpleaños = None):
        self.id_usuario = id_usuario, 
        self.email = email, 
        self.contraseña = contraseña, 
        self.nombre = nombre,  
        self.apellido = apellido,  
        self.loggin = loggin, 
        self.cumpleaños = cumpleaños

    @classmethod
    def create(cls, user):
        """ Crear nuevo usuario """

        query = """INSERT INTO servidor_app.usuarios (email, contraseña, nombre,  apellido,  loggin, cumpleaños) 
        VALUES (%s, %s, %s, %s, %s, %s)"""
        params = (user.email, user.contraseña, user.nombre, user.apellido, user.loggin, user.cumpleaños)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def update(cls, user):
        """ Actualizar información de un usuario """

        query = """UPDATE servidor_app.usuarios SET email=%s, contraseña=%s, nombre=%s,  apellido=%s,  loggin=%s, cumpleaños=%s 
        WHERE id_usuario = %s"""
        params = (user.email, user.constraseña, user.nombre, user.apellido, user.loggin, user.cumpleaños, user.id_usuario)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def delete(cls, user):
        """ Eliminar un usuario """

        query = "DELETE FROM servidor_app.usuarios WHERE id_usuario = %s"
        params = user.id_usuario,
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def exist_email(cls, user):
        """ Verificar si ya existe un usuario registrado con el email """

        query = """SELECT id_usuario FROM servidor_app.usuarios WHERE email = %s"""
        params = (user.email,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return True
        else:
            return False
        
    @classmethod
    def exist_loggin(cls, user):
        """ Verificar si ya existe un usuario registrado con el nombre de usuario """

        query = """SELECT id_usuario FROM servidor_app.usuarios WHERE loggin = %s"""
        params = (user.loggin,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return True
        else:
            return False
        
    @classmethod    
    def verify_account(cls, user):
        """ Verificar que el email y la contraseña coinciden con un usuario registrado """

        query = """ SELECT id_usuario FROM servidor_app.usuarios WHERE email = %s AND contraseña = %s """
        params = (user.email, user.contraseña)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return True
        else:
            return False
        
    @classmethod
    def get_user_info(cls, user):
        """ Obtiene la información de un usuario en especifico """

        query = """ SELECT loggin, nombre, apellido, cumpleaños, foto_perfil FROM servidor_app.usuarios WHERE id_usuario = %s """
        params = (user.id_usuario,)
        result = DatabaseConnection.fetch_one(query, params)
        return result

    @classmethod
    def get_all_servers_from_user(cls, user):
        """ Obtiene los servidores a los que se ha registrado un usuario """

        query = """ SELECT servidores.nombre FROM servidor_app.servidores INNER JOIN servidor_app.usuarios_servidores ON servidores.id_servidor = usuarios_servidores.servidor 
        INNER JOIN servidor_app.usuarios ON usuarios.id_usuario = usuarios_servidores.usuario WHERE usuarios.id_usuario = %s """
        params = (user.id_usuario,)
        result = DatabaseConnection.fetch_all(query, params)
        return result