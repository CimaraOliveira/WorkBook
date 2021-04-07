from rest_framework import viewsets
from categoria.models import Categoria
from perfil.models import Perfil
from avaliacao.models import Avaliacao
from mensagem.models import Mensagem
from usuario.models import Usuario
from api.serializers import CategoriaSerializer, PerfilSerializer, AvaliacaoSerializer,\
    MensagemSerializer, UsuarioSerializer


class PerfilViews(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class CategoriaViews(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class AvaliacaoViews(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class MensagemViews(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer


class UsuarioViews(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer




