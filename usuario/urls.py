from django.urls import path,include
from . import views

app_name = 'usuario'

urlpatterns = [

   path('perfil/', views.perfil, name='perfil'),
   path('submit_login/', views.submit_login, name='submit_login'),
   path('index/', views.index_perfil, name='index'),
   path('logout/', views.logout_user, name='logout_user'),
   path('home/', views.index_perfil, name="home"),
   path('perfilProfissional/<str:id>', views.PerfilProf, name="Profissional"),
   path('alterarUsuario/<int:id>', views.alterarUsuario, name="alterarUsuario"),
   path('detalhesusuario/<int:id>', views.detalhesusuario, name="detalhesusuario"),
   path('sobre/', views.sobre, name="sobre")




]