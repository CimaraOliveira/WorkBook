from django.urls import path,include
from . import views

app_name = 'usuario'

urlpatterns = [

   path('perfil/', views.perfil, name='perfil'),
   path('submit_login/', views.submit_login, name='submit_login'),
   path('index/', views.index, name='index'),
   path('index/', views.index, name='index'),
   path('logout/', views.logout_user),


]