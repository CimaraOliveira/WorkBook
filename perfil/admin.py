from django.contrib import admin
from .models import Perfil

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['nome', 'decricao', 'slogan',]

admin.site.register(Perfil,PerfilAdmin)


