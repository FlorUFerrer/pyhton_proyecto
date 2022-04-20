from .views import inicio, about , usuario ,  UsuarioEditar

from django.urls import path

urlpatterns = [
    path('', inicio , name = 'inicio'),
    path('usuario/', usuario, name = 'usuario'),
    path('about/', about, name = 'about'),
    path('editar/', UsuarioEditar, name = 'editar_usuario'),
    
 
]
