from django.urls import path,include
from . import views


urlpatterns = [

   path('avaliacao/', views.avaliacao, name='avaliacao'),
   path('', views.avaliacao, name='avaliacao'),
]