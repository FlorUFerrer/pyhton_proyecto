
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
   
   
     
     path('blogs/',views.Blogs.as_view() , name = 'blogs'),
     path('blogs/crear/',views.BlogCrear.as_view() , name = 'blog_crear'),
     path('blog/<int:pk>',views.BlogDetalle.as_view() , name = 'blog_detalle'),
     path('blog/<int:pk>/editar',views.BlogEditar.as_view() , name = 'blog_editar'),
     path('blog/<int:pk>/borrar/',views.BlogBorrar.as_view() , name = 'blog_borrar'),
  
]

