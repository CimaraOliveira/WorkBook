from django.urls import path,include
from . import views

app_name = 'usuario'
urlpatterns = [

   path('perfil/', views.perfil, name='perfil'),

  ]