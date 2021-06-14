from django.test import TestCase
from usuario.models import Usuario
from django.test.client import Client
from usuario.views import perfil
import unittest
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse

class HomeViewTest(TestCase):
    def test_home_status_code(self):
        client = Client()
        response = client.get(reverse('http://127.0.0.1:8000/usuario/submit_login/'))
        self.assertEqual(response.status_code,200)

    def test_home_template_used(self):
        client=Client()
        response = client.get(reverse('usuario:index'))
        self.assertTemplateUsed(response, 'usuario:index')


    """def test_redirect_logged(self):
        response=self.client.get(reverse('submit_login'))
        self.assertRedirects(response, 'http://127.0.0.1:8000/usuario/submit_login/')

"""


"""class TesteCadastro(TestCase):
    def setUp(self):
        Usuario.objects.create(
            nome='cimara', email='cimara@gmail.com', senha='123456',
            cidade='cidade', estado='estado', telefone='22222222222'

        )

    def test_return_str(self):
        p1 = Usuario.objects.get(nome='cimara')
        self.assertEquals(p1.__str__(), 'cimara')

    def test_views_exists_home(self):
        response = self.client.get('home')
        self.assertEquals(response.status, 200)
"""







