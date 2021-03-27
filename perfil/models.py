from django.db import models

# Create your models here.
from categoria.models import Categoria


class Perfil(models.Model):
    nome = models.CharField('nome',max_length=250)
    categorias = models.ManyToManyField(Categoria)
    decricao = models.CharField('descricao', max_length=2000)
    slogan = models.ImageField(upload_to='profissional', blank=True, null=True)

    class Meta:
        db_table = 'perfil'