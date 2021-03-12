from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Usuario


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password',]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password', ]