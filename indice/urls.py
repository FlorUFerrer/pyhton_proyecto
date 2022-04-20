from .views import inicio, about , usuario , UsuarioLogin
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
    path('', inicio , name = 'inicio'),
    path('usuario/', usuario, name = 'usuario'),
    path('sobre-mi/', about, name = 'sobre-mi'),
    path('login/', UsuarioLogin, name = 'login'),
    path('logout/', LogoutView.as_view(template_name ='indice/index.html'), name = 'logout'),
 
]
