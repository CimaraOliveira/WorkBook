from .models import Usuario
from django.test import TestCase
from django.urls import reverse

class home(TestCase):
    @classmethod
    def setUpTestData(cls):
        Usuario.objects.create(
            first_name = 'joana12',
            email='cimara@gmail.com',
            senha='123456',
            cidade='cidade',
            estado='estado',
            telefone='22222222222',
            tipo = 'cliente'

        )

        def test_views_exists_home(self):
            response = self.client.get('/index')
            self.assertEquals(response.status_code, 200)

            class LoginViewTest(TestCase):
                usiario1 = Usuario.objects.create(nome='cimara',
                                                  email='cimara@gmail.com',
                                                  senha='123456',
                                                  cidade='cidade',
                                                  estado='estado'
                                                  )
                # usiario22 = Usuario.objects.create_user(username='teste2', password='123456')

                usiario1.save()
                # usiario22.save()