from _ast import mod
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django import forms


from perfil.models import Perfil
class Usuario(AbstractUser):
    nome = models.CharField('nome', max_length=250)
    email = models.EmailField()
    senha = models.CharField('senha', max_length=250)
    cidade = models.CharField('cidade', max_length=250)
    estado = models.CharField('estado', max_length=250)
    telefone = models.CharField('Telefone', max_length=20)
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, null=True, blank=True)
    is_staff = models.BooleanField(default=1)
    is_superuser = models.BooleanField(default=1)
    is_active = models.BooleanField(default=True)

    LOAN_STATUS = (
        ('profissional', 'Profissional'),
        ('cliente', 'Cliente'),

    )
    status = models.CharField(max_length=15, choices=LOAN_STATUS, blank=True)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)


    def __str__(self):
        return str(self.nome or self.senha)

    class Meta:
        db_table = 'usuario'


class FormDadosUsu(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ('is_active','slug','is_staff','is_superuser','telefone','user_permissions','groups','last_login','password','status', 'date_joined',)

