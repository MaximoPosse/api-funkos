from django.urls import include, path
from rest_framework import routers
from .views import Inicio, ViewCategoria, ViewProductos, ViewFunkoPop

router = routers.DefaultRouter()
router.register('productos', ViewProductos, basename='productos')
router.register('categorias', ViewCategoria, basename='categorias')
router.register('funkos', ViewFunkoPop, basename='funkos')

urlpatterns = [
    path('', Inicio, name='Inicio'),
    path('api/', include(router.urls)),
]
