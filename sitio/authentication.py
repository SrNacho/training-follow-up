from django.contrib.auth.backends import BaseBackend
from .models import Usuario,HorasUsuario

class UserAuthenticationBackend(BaseBackend):
  def authenticate(self,request,user,site) ->Usuario:
    find_user_in_database = Usuario.objects.filter(email=user['email'])
    user_exists = len(find_user_in_database)
    if user_exists == 0 and site=='sign_up':
      new_user = Usuario.objects.crear_nuevo_usuario(user)
      HorasUsuario.objects.create(email=user['email'])
      print(new_user)
      print("Usuario no encontrado,creando")
      return new_user
    elif user_exists > 0 and site=='sign_in':
      print(find_user_in_database)
      passwo = user['password']
      usr = list(find_user_in_database).pop()
      if usr.check_password(passwo):
        print(find_user_in_database)
        return usr
      else:
        print("no")
    elif user_exists > 0 and site=='sign-in-resetpw':
      usuarioParaEditar = Usuario.objects.editar_clave_usuario(user)
      print(usuarioParaEditar.password, 'AAAAAAAA')
      find_user_in_database.update(password=usuarioParaEditar.password)
      passwo = user['password']
      
    else:
      print("usuario ya existente")
      #return find_user_in_database

  def get_user(self,user_id):
    try:
      print(user_id)
      return Usuario.objects.get(pk=int(user_id))
    except:
      return None

