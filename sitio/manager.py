from django.contrib.auth import models

class UsuariosManager(models.BaseUserManager):
  def crear_nuevo_usuario(self,user):
    new_user = self.model(
      username = user['usuario'],
      email = user['email'],
    )
    new_user.set_password(user['password'])
    new_user.save()
    return new_user

  def editar_clave_usuario(self,user):
    new_user = self.model(
      username = user['usuario'],
      email = user['email'],
    )
    new_user.set_password(user['password'])
    return new_user