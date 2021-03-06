"""WorkBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic import RedirectView

from WorkBook import settings
from usuario import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('login/', views.submit_login),
    path('mensagem/', include('mensagem.urls')),
    path('avaliacao/', include('avaliacao.urls')),
    path('perfil/', include('avaliacao.urls')),
    path('', RedirectView.as_view(url='usuario/home')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('api.urls')),
    path('relatorio/',include('relatorio.urls')),
    path('accounts/', include('allauth.urls')),

]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)