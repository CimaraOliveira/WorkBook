from django.contrib import admin
from .models import Usuario
#from .form import CustomUserCreationForm, CustomUserChangeForm


@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    model = Usuario
    list_display = ['username', 'first_name', 'last_name', 'email','is_superuser', 'is_active', 'is_staff', ]




