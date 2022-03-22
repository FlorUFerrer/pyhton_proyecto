from .views import inicio, about , usuario
from django.urls import path

urlpatterns = [
    path('', inicio , name = 'inicio'),
    path('usser/', usuario, name = 'usuario'),
    path('about/', about, name = 'about'),
   
    
    

]
