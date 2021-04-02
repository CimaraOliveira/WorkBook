from django.urls import path,include
from . import views


urlpatterns = [

   path('avaliacao/', views.avaliar, name='avaliar'),
   path('', views.avaliacao, name='avaliacao'),
]