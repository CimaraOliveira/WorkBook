from django.contrib import admin
from .models import Mensagem

class MensagemAdmin(admin.ModelAdmin):
    list_display = ['texto', 'mensageiro', 'destinatario',]

admin.site.register(Mensagem,MensagemAdmin)

