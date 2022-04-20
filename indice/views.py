from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import AuthenticationForm


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
                     return render(request , 'indice/index.html', {'msj': 'Estas logueado!'})
              else:
                return render(request , 'indice/login.html', {'form': form ,'msj': 'No se autenticó'})           
       else:
          return render(request , 'indice/login.html', {'form': form , 'msj': 'Datos incorrectos'})   
    else:                  
       form = AuthenticationForm()
       return render(request,'indice/login.html',{'form': form , 'msj': ' '})   
    


