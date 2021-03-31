from django.db import models

# Create your models here.
from usuario.models import Usuario


class Mensagem(models.Model):
    texto = models.CharField('texto',max_length=500)
    mensageiro = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, related_name='mensageiro')
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, related_name='destinatario')

    class Meta:
        db_table = 'Mensagen'