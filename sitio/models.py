from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .manager import DiscordAuthManager,UsuariosManager
# Create your models here.

class DiscordUser(models.Model):
  objects = DiscordAuthManager()
  id = models.BigIntegerField(primary_key=True)
  discord_user = models.CharField(max_length=100)
  avatar_id = models.CharField(max_length=100)
  last_login = models.DateTimeField(null=True)

  def is_authenticated(self,request):
    return True

  def __str__(self):
    return self.discord_user

class Usuario(AbstractBaseUser):
  objects = UsuariosManager()
  username = models.CharField(max_length=50,unique=True)
  email = models.EmailField(unique=True)
  last_login = models.DateTimeField(null=True)
  USERNAME_FIELD = 'username'
  EMAIL_FIELD = 'email'
    
class HorasUsuario(models.Model):
  email=models.EmailField(unique=True, null=True)
  lunes = models.IntegerField(default=-1)
  martes = models.IntegerField(default=-1)
  miercoles = models.IntegerField(default=-1)
  jueves = models.IntegerField(default=-1)
  viernes = models.IntegerField(default=-1)
  sabado = models.IntegerField(default=-1)
  promedio = models.IntegerField(default=0)

  def __str__(self):
    return self.email