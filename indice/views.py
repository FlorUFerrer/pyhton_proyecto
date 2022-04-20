from urllib import request
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from .forms import CreacionUser , EditarUser
from django.contrib.auth.decorators import login_required


def inicio(request):
   return render(request,'indice/index.html',{})

def usuario(request):
       return render(request,'indice/usuario.html',{})   

def about(request):
       return render(request,'indice/about.html',{})   

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
                return render(request , 'indice/login.html', {'form': form ,'msj': 'No se autenticó'})           
       else:
          return render(request , 'indice/login.html', {'form': form , 'msj': 'Datos incorrectos'})   
    else:                  
       form = AuthenticationForm()
       return render(request,'indice/login.html',{'form': form , 'msj': ' '})   
    


def registrar(request):

   if request.method =='POST':    
       form = CreacionUser(request.POST)

       if form.is_valid():
             username = form.cleaned_data['username']
             form.save()
             return render(request , 'indice/index.html', {'msj': f'Se creo el user {username} '})
       else:
           return render(request , 'indice/registrar.html', {'form': form , 'msj': 'Datos incorrectos'})       

   form = CreacionUser()    
   return  render(request , 'indice/registrar.html', {'form': form , 'msj': ''})  


@login_required
def UsuarioEditar(request):
   msj = '' 
   if request.method =='POST':    
       form = EditarUser(request.POST)

       if form.is_valid():
             
             data = form.cleaned_data

             logued_user = request.user

             logued_user.email = data.get('email')
             logued_user.first_name = data.get('first_name','')
             logued_user.last_name = data.get('last_name','')
             if data.get('password1') == data.get('password2') and len(data.get('password1')) > 8:
                    logued_user.set_password(data.get('password1'))
             else:
                msj = 'No se modifico el password.'
                   
             logued_user.save()
          
             return render(request , 'indice/index.html', {'msj': msj })
       else:
           return render(request , 'indice/editar_usuario.html', {'form': form , 'msj': ' '})       

   form = EditarUser(
          initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'username': request.user.username
        }
   )    
   return  render(request , 'indice/editar_usuario.html', {'form': form , 'msj': 'Datos actualizados'})  
    