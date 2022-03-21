
from django.urls import path
from .views import nuevo_usuario , formulario

urlpatterns = [
    path('usuario/',nuevo_usuario, name='nuevo_usuario'),
    path('formulario/',formulario, name='formulario'),
   
  
]
