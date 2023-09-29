from ..models.usuarios import User
from flask import request, session
import datetime

class UserController:
    """ User controller class """

    @classmethod
    def validar_json_post(cls, data):
        email = data.get('email')
        contraseña = data.get('contraseña')
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        loggin = data.get('loggin')
        cumpleaños = data.get('cumpleaños')
        foto_perfil = data.get('foto_perfil')
        if (email is not None and contraseña is not None and nombre is not None and apellido is not None and loggin is not None and cumpleaños is not None):
            return data
        # else:
        #     raise InvalidDataError("Hay campos obligatorios no ingresados") 

    @classmethod
    def validar_json_put(cls, data):
        email = data.get('email')
        contraseña = data.get('contraseña')
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        loggin = data.get('loggin')
        cumpleaños = data.get('cumpleaños')
        foto_perfil = data.get('foto_perfil')
        if (email is not None and contraseña is not None and nombre is not None and apellido is not None and loggin is not None and cumpleaños is not None):
            return data
    
    @classmethod
    def log_in(cls):
        """ Inicio de sesión """

        data = request.json
        data_email = data.get('email')
        data_loggin = data.get('loggin')
        data_contraseña = data.get('contraseña')
        user=User(email=data_email, loggin=data_loggin, contraseña=data_contraseña)
        usuario_registrado = User.verify_account(user)
        if usuario_registrado is not None:
            session['loggin'] = usuario_registrado.loggin
            session['email'] = usuario_registrado.email
            return {'message': 'Inicio de sesión con exito'},200
        else:
            return {'message':'El email o la contraseña son incorrectos'},401
        
    @classmethod
    def log_out(cls):
        session.pop('nickname',None)
        session.pop('email',None)
        return {"message":"Sesión cerrada"},200    
    
    @classmethod
    def create(cls):
        """ Registrar un nuevo usuario """

        data = request.json
        data = UserController.validar_json_post(data)
        user = User(**data)

        email_result = User.exist_email(user)
        loggin_result = User.exist_loggin(user)
        if not email_result:
            if not loggin_result:
                User.create(user)
            else: 
                return ("El nombre de usuario ya se encuentra utilizado")
            return {'message': 'Usuario registrado con exito'}, 201
        else:
            return ("el email ingresado ya se encuentra registrado")

    @classmethod
    def update(cls, user_id):
        """ Actualizar información de usuario """

        data = request.json
        # result= User.exists(User(id_usuario=user_id))
        # if not result:
        #     raise (f"No se encontró el usuario")

        data = UserController.validar_json_put(data)
        data['id_usuario'] = user_id

        user = User(**data)

        email_result = User.exist_email(user)
        loggin_result = User.exist_loggin(user)
        if not email_result:
            if not loggin_result:
                User.update(user)
                return {'message': 'Información actualizada con exito'}, 200
            else: 
                return ("El nombre de usuario ya se encuentra utilizado")
        else:
            return ("el email ingresado ya se encuentra registrado")

    @classmethod
    def delete(cls, user_id):
        """ Eliminar usuario """

        user = User(id_usuario=user_id)
        # if (not User.exists(user)):
        #     raise FilmNotFound(f"No se encontró el usuario con id {user.id_usuario}")
        User.delete(user)
        return {'message': 'Usuario eliminado con exito'}, 204

    @classmethod
    def get_all_servers (cls, user_id):
        """ Obtener los servidores a los que pertenece el usuario """

        user = User(id_usuario=user_id)
        server_objects = User.get_all_servers_from_user(user)
        servers = []
        if server_objects is not None:
            for server in server_objects:
                servers.append(server)
            return servers
        else:
            return None
        
    @classmethod
    def get_info_user(cls, user_id):
        """ Obtiene infomación de un usuario """

        user = User(id_usuario=user_id)
        result = User.exists(user)
        object = []
        if result:
            info_object = User.get_user_info(user)
            object.append(info_object)
            return object