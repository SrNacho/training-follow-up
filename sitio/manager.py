from django.contrib.auth import models

class DiscordAuthManager(models.BaseUserManager):
  def create_new_user(self,user):
    discord_tag = '%s#%s' % (user['username'],user['discriminator'])
    new_user = self.create(
      id=user['id'],
      discord_user = discord_tag,
      avatar_id=user['avatar']
    )
    return new_user

class UsuariosManager(models.BaseUserManager):
  def crear_nuevo_usuario(self,user):
    new_user = self.model(
      username = user['usuario'],
      email = user['email'],
      
    )
    new_user.set_password(user['password'])
    new_user.save()

    return new_user