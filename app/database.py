import mysql.connector
from mysql.connector import errors

class DatabaseConnection:
    _connection = None

    _credenciales = {'user': 'root', # Introducir usuario
                'password': 'nino2021', # Introducir contraseña
                'host': '127.0.0.1',
                'port' : '3306',
                'database': 'servidor_app'}

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(**cls._credenciales)
        return cls._connection

    @classmethod
    def execute_query(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        cls._connection.commit()
        return cursor

    @classmethod
    def fetch_all(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    @classmethod
    def fetch_one(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    @classmethod
    def close_connection(cls):
        if (cls._connection is not None):
            cls._connection.close()
            cls._connection = None

    @classmethod
    def create_if_not_exists(cls):
        """ Crea la base de datos si no existe """
        create_database = "CREATE DATABASE IF NOT EXISTS %s" %cls._credenciales['database']
        create_table_usuarios = """CREATE TABLE IF NOT EXISTS `usuarios` (
            `id_usuario` INT NOT NULL AUTO_INCREMENT,
            `email` VARCHAR(45) NOT NULL,
            `constraseña` VARCHAR(45) NOT NULL,
            `nombre` VARCHAR(45) NOT NULL,
            `apellido` VARCHAR(45)  NOT NULL,
            `loggin` VARCHAR(45) NOT NULL,
            `cumpleaños` DATE NOT NULL,
            PRIMARY KEY (`id_usuario`))
            ENGINE = InnoDB; """
        create_table_servidores = """CREATE TABLE IF NOT EXISTS `servidores` (
            `id_servidor` INT NOT NULL AUTO_INCREMENT,
            `nombre` VARCHAR(45) NOT NULL,
            PRIMARY KEY (`id_servidor`))
            ENGINE = InnoDB; """
        create_table_canales = """CREATE TABLE IF NOT EXISTS `canales` (
            `id_canal` INT NOT NULL AUTO_INCREMENT,
            `nombre` VARCHAR(45) NOT NULL,
            `servidor` INT NOT NULL,
            PRIMARY KEY (`id_canal`),
            CONSTRAINT `Servidor_fk`
                FOREIGN KEY (`servidor`)
                REFERENCES `servidores` (`id_servidor`)
                ON DELETE CASCADE
                ON UPDATE CASCADE)
            ENGINE = InnoDB; """
        create_table_chats = """CREATE TABLE IF NOT EXISTS `chats` (
            `id_mensaje` INT NOT NULL,
            `mensaje` VARCHAR(250) NOT NULL,
            `fecha` DATE NOT NULL,
            `hora` TIME NOT NULL,
            `usuario` INT NOT NULL,
            `canal` INT NOT NULL,
            PRIMARY KEY (`id_mensaje`),
            CONSTRAINT `Usuario_fk`
                FOREIGN KEY (`usuario`)
                REFERENCES `usuarios` (`id_usuario`)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
            CONSTRAINT `Canal_fk`
                FOREIGN KEY (`canal`)
                REFERENCES `canales` (`id_canal`)
                ON DELETE CASCADE
                ON UPDATE CASCADE)
            ENGINE = InnoDB; """
        create_table_usuarios_servidores = """CREATE TABLE IF NOT EXISTS `usuarios_servidores` (
            `usuario` INT NOT NULL,
            `servidor` INT NOT NULL,
            CONSTRAINT `fk_Usuarios_Servidores_Usuario`
                FOREIGN KEY (`usuario`)
                REFERENCES `usuarios` (`id_usuario`)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
            CONSTRAINT `fk_Usuarios_Servidores_Servidor`
                FOREIGN KEY (`servidor`)
                REFERENCES `servidores` (`id_servidor`)
                ON DELETE CASCADE
                ON UPDATE CASCADE)
            ENGINE = InnoDB; """
        create_table_usuarios_canales = """CREATE TABLE IF NOT EXISTS `usuarios_canales` (
            `usuario` INT NOT NULL,
            `canal` INT NOT NULL,
            CONSTRAINT `fk_Usuario_Canales_Usuario`
                FOREIGN KEY (`usuario`)
                REFERENCES `usuarios` (`id_usuario`)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
            CONSTRAINT `fk_Usuario_Canales_Canal`
                FOREIGN KEY (`canal`)
                REFERENCES `canales` (`id_canal`)
                ON DELETE CASCADE
                ON UPDATE CASCADE)
            ENGINE = InnoDB; """
        try:
            db_connection = mysql.connector.connect(user=cls._credenciales["user"],
                                        password=cls._credenciales["password"],
                                        host="127.0.0.1")
            db_cursor = db_connection.cursor()
            db_cursor.execute(create_database)
            db_cursor.execute("USE %s" %cls._credenciales["database"])
            db_cursor.execute(create_table_usuarios)
            db_cursor.execute(create_table_servidores)
            db_cursor.execute(create_table_canales)
            db_cursor.execute(create_table_chats)
            db_cursor.execute(create_table_usuarios_servidores)
            db_cursor.execute(create_table_usuarios_canales)
            db_connection.commit()
            db_connection.close()
        except errors.DatabaseError as error:
            print("Error al conectar o crear la base de datos.", error)
            raise