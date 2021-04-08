from rest_framework import serializers
from categoria.models import Categoria
from perfil.models import Perfil
from avaliacao.models import Avaliacao
from mensagem.models import Mensagem
from usuario.models import Usuario


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ('__all__')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('__all__')

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = ('__all__')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'nome', 'email', 'senha', 'cidade', 'telefone', 'status', ]


