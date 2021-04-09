from django.urls import path,include
from . import views

app_name = 'avaliacao'

urlpatterns = [

   path('avaliacao/<id>', views.avaliar, name='avaliar'),
   path('listAvaliacao/', views.listAvaliacao, name='listAvaliacao'),
   path('<id>', views.avaliacao, name='avaliacao'),
]