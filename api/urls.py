from django.urls import include, path
from api.views import CategoriaViews, PerfilViews, AvaliacaoViews, MensagemViews, UsuarioViews
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="WorkBook API",
      default_version='v1',
      description="Documentação Swagger WorkBook",
      #terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="sistema.workbook.21@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register(r'Perfil', PerfilViews)
router.register(r'Categoria',CategoriaViews)
router.register(r'Avaliação', AvaliacaoViews)
router.register(r'Mensagem', MensagemViews)
router.register(r'Usuario', UsuarioViews)

urlpatterns = [
   path('', include(router.urls)),

   path('swagger/<format>\.json|\.yaml', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
