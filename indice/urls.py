from .views import inicio, about , usuario , UsuarioLogin , registrar
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
    path('', inicio , name = 'inicio'),
    path('usuario/', usuario, name = 'usuario'),
    path('sobre-mi/', about, name = 'sobre-mi'),
    path('registrar/', registrar, name = 'registrar'),
    path('login/', UsuarioLogin, name = 'login'),
    path('logout/', LogoutView.as_view(template_name ='indice/logout.html'), name = 'logout'),
 
]
