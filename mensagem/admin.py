from django.contrib import admin
from .models import Mensagem

class MensagemAdmin(admin.ModelAdmin):
    list_display = ['id','nomeRemetente','texto','destinatario','remetente',]

admin.site.register(Mensagem,MensagemAdmin)

