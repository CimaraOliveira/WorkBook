from django.db import models

# Create your models here.
class Categoria(models.Model):

    nome = models.CharField('nome',max_length=250)

    class Meta:
        db_table = 'categoria'