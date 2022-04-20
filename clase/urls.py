
from django.urls import path
from . import views
urlpatterns = [
    path('usser_new/',views.nuevo_usuario, name='nuevo_usuario'),
    path('form/',views.formulario, name='formulario'),
    path('search/', views.busqueda , name= 'busqueda'),
    
    path('usuarios/', views.listado_usuarios, name ='listado_usuarios'),
    path('usuario/registrar/', views.crear_usuario, name ='crear_usuario'),
    path('usuario/borrar/<int:id>/', views.borrar_usuario, name ='borrar_usuario'),
    path('usuario/actualizar/<int:pk>/', views.actualizar_usuario, name ='actualizar_usuario'),
   
    path('posteos/',views.Posteos.as_view() , name = 'posteos'),
    path('posteos/crear/',views.PosteoCrear.as_view() , name = 'posteo_crear'),
    path('posteos/<int:pk>',views.PosteoDetalle.as_view() , name = 'posteo_detalle'),
    path('posteos/<int:pk>/editar',views.PosteoEditar.as_view() , name = 'posteo_editar'),
    path('posteos/<int:pk>/borrar/',views.PosteoBorrar.as_view() , name = 'posteo_borrar')
]

