from django.db import models

# Create your models here.
from categoria.models import Categoria


class Perfil(models.Model):
    nome = models.CharField('nome',max_length=250)
    categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'perfil'