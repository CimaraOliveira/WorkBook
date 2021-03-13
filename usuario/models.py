from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser



class Usuario(AbstractUser):
	telefone = models.CharField('Telefone', max_length=20)
	is_staff = models.BooleanField(default=1)
	is_superuser = models.BooleanField(default=1)
	is_active = models.BooleanField(default=True)

	@property
	def name(self):
		return "{} {}".format(self.first_name, self.last_name)

	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome





