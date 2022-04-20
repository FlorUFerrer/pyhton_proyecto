from .views import   UsuarioLogin , registrar 
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
  
    path('registrar/', registrar, name = 'registrar'),
    path('login/', UsuarioLogin, name = 'login'),
    path('logout/', LogoutView.as_view(template_name ='indice/index.html'), name = 'logout'),
 
]
