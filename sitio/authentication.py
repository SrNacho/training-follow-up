from django.contrib.auth.backends import BaseBackend
from .models import DiscordUser,Usuario,HorasUsuario

class DiscordAuthenticationBackend(BaseBackend):
  def authenticate(self,request,user) -> DiscordUser:
    find_user_in_database = DiscordUser.objects.filter(id=user['id'])
    if len(find_user_in_database) == 0:
      new_user = DiscordUser.objects.create_new_user(user)
      print("Usuario no encontrado,creando")
      return new_user
    else:
      print("usuario ya existente")
      return find_user_in_database

  def get_user(self,user_id):
    try:
      return DiscordUser.objects.get(pk=user_id)
    except:
      return None

class UserAuthenticationBackend(BaseBackend):
  def authenticate(self,request,user,site) ->DiscordUser:
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
        print("noxd")
    else:
      print("usuario ya existente")
      #return find_user_in_database

  def get_user(self,user_id):
    try:
      print(user_id)
      return Usuario.objects.get(pk=int(user_id))
    except:
      return None

