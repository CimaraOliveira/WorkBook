from django.db import models

from usuario.models import Usuario


class Mensagem(models.Model):
    texto = models.CharField('texto',max_length=500)
    #remetente = models.IntegerField('remetente', blank=True, null=True)
    #destinatario = models.IntegerField('destinatario', blank=True, null=True)
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=False, related_name='destinatario')
    remetente = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=False, related_name='remetente')
    #nomeRemetente = models.CharField('nomeRemetente',max_length=100)
    data = models.CharField(null=True, name='data_mensagem', blank=False, max_length=20)


    class Meta:
        db_table = 'Mensagen'
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'

