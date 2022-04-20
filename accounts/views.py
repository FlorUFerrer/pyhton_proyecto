
from django.shortcuts import render ,redirect
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import AuthenticationForm 
from .forms import CreacionUser 
from django.contrib.auth.decorators import login_required





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
                     return render(request , 'indice/index.html', {'msj': 'Estas logueado !'})
              else:
                return render(request , 'accounts/login.html', {'form': form ,'msj': 'No se autenticó'})           
       else:
          return render(request , 'accounts/login.html', {'form': form , 'msj': 'Datos incorrectos'})   
    else:                  
       form = AuthenticationForm()
       return render(request,'accounts/login.html',{'form': form , 'msj': ' '})   
    


def registrar(request):

   if request.method =='POST':    
       form = CreacionUser(request.POST)

       if form.is_valid():
             username = form.cleaned_data['username']
             form.save()
             return render(request , 'indice/index.html', {'msj': f'Se creo el user {username} '})
       else:
           return render(request , 'accounts/registrar.html', {'form': form , 'msj': 'Datos incorrectos'})       

   form = CreacionUser()    
   return  render(request , 'accounts/registrar.html', {'form': form , 'msj': ''})  