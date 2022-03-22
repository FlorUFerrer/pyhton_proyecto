
from django.urls import path
from .views import nuevo_usuario , formulario , busqueda

urlpatterns = [
    path('usser_new/',nuevo_usuario, name='nuevo_usuario'),
    path('form/',formulario, name='formulario'),
    path('search', busqueda , name= 'busqueda')
  
]
