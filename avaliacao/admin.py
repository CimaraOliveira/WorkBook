from django.contrib import admin
from .models import Avaliacao

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['id','descricao', 'cliente_id', 'proficional_id',]

admin.site.register(Avaliacao,AvaliacaoAdmin)
