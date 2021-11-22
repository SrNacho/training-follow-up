from django.contrib import admin
from .models import Usuario,HorasUsuario, CuotaUsuario
# Register your models here.
admin.site.register([Usuario,HorasUsuario, CuotaUsuario])