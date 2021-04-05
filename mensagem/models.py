from django.db import models

class Mensagem(models.Model):
    texto = models.CharField('texto',max_length=500)
    destinatario = models.IntegerField('destinatario', blank=True, null=True)
    remetente = models.IntegerField('remetente', blank=True, null=True)
    nomeRemetente = models.CharField('nomeRemetente',max_length=100)
    class Meta:
        db_table = 'Mensagen'
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'

