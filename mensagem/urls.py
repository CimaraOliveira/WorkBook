from django.urls import path,include
from . import views

urlpatterns = [

   path('enviarMensagem/<id>', views.enviarMensagem, name='enviarMensagem'),
   path('responderMensagem/<int:remetente>', views.responderMensagem, name='responderMensagem'),
   path('listarMensagem/', views.listarMensagem, name='listarMensagem'),
]