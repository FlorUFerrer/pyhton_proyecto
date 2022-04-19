
from django.urls import path
#from .views import nuevo_usuario , formulario , busqueda ,usuarios
from . import views
urlpatterns = [
    path('usser_new/',views.nuevo_usuario, name='nuevo_usuario'),
    path('form/',views.formulario, name='formulario'),
    path('search/', views.busqueda , name= 'busqueda'),
    
    path('usuarios/', views.listado_usuarios, name ='listado_usuarios'),
    # path('usuario', views.usuario, name ='usuario'),
    path('usuario/registrar/', views.crear_usuario, name ='crear_usuario'),
    # path('usuario/borrar', views.borrar_usuario, name ='borrar_usuario'),
    path('usuario/actualizar', views.actualizar_usuario, name ='actualizar_usuario')
]
