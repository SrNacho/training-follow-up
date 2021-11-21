from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .manager import UsuariosManager
# Create your models here.

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

class CuotaUsuario(models.Model):
  email=models.EmailField(unique=True, null=True)
  fechaExpiracion= models.DateField()
  fechaInicio=models.DateField()