
from django.shortcuts import render ,redirect
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import AuthenticationForm 
from .forms import CreacionUser 
from django.contrib.auth.decorators import login_required
from indice.views import usuario_avatar
from indice.models import Avatar
from indice.views  import usuario_avatar


# Create your views here.
def UsuarioLogin(request):
    if request.method =='POST':
       form = AuthenticationForm(request , data=request.POST)
    
       if form.is_valid():
              username = form.cleaned_data['username']
              password = form.cleaned_data['password'] 
              user = authenticate(username = username , password = password)    

              if user is not None:
                     login(request, user)
                     return render(request , 'indice/index.html', {'msj': f'Bienvenido {username} !', 'url_avatar' : usuario_avatar(request)})
              else:
                return render(request , 'accounts/login.html', {'form': form ,'msj': 'No se autenticó', 'url_avatar' : usuario_avatar(request)})           
       else:
          return render(request , 'accounts/login.html', {'form': form , 'msj': 'Datos incorrectos','url_avatar' : usuario_avatar(request)})   
    else:                  
       form = AuthenticationForm()
       return render(request,'accounts/login.html',{'form': form , 'msj': ' ','url_avatar' : usuario_avatar(request)})   
    


def registrar(request):

   if request.method =='POST':    
       form = CreacionUser(request.POST)

       if form.is_valid():
             username = form.cleaned_data['username']
             form.save()
             return render(request , 'indice/index.html', {'msj': f'Usuario {username} registrado correctamente! '})
       else:
           return render(request , 'accounts/registrar.html', {'form': form , 'msj': 'Datos incorrectos'})       

   form = CreacionUser()    
   return  render(request , 'accounts/registrar.html', {'form': form , 'msj': ''})  



