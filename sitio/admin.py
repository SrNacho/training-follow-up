from django.contrib import admin
from .models import DiscordUser, Usuario,HorasUsuario
# Register your models here.
admin.site.register([DiscordUser,Usuario,HorasUsuario])