from django.test import TestCase
from  .models import Usuario
from django.test.client import Client
from .views import perfil
import unittest



class TesteCadastro(TestCase):
    def setUp(self):
        Usuario.objects.create(
            nome='cimara', email='cimara@gmail.com', senha='123456',
            cidade='cidade', estado='estado', telefone='22222222222'

        )


    def test_return_str(self):
        p1 = Usuario.objects.get(nome='cimara')
        self.assertEquals(p1.__str__(), 'cimara')








