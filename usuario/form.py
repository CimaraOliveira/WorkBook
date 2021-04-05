from .models import Usuario
from django import forms
from django.forms import ModelForm


class AlterUsuForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'nome','email','cidade','estado','telefone','senha',]



