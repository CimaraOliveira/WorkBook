from django.contrib import admin
from .models import Categoria
#from .form import CustomUserCreationForm, CustomUserChangeForm


@admin.register(Categoria)
class UserAdmin(admin.ModelAdmin):
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    model = Categoria
    list_display = ['nome']







