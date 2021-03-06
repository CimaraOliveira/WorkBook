from django.db import models

class Usuario(models.Model):
    class Meta:
        db_table = 'Usuario'
