from .models import Usuario
from django import forms
from django.forms import ModelForm


class AlterUsuForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name','email','cidade','estado','telefone','senha',]



