from django.http import HttpResponse

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.forms import EditarUser
from .models import Avatar

def inicio(request):
   return render(request,'indice/index.html',{})



def usuario(request):
       return render(request,'indice/usuario.html',{})   

def about(request):
       return render(request,'indice/about.html',{})   




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
          
             return render(request , 'indice/index.html', {'msj': msj ,'url_avatar' : buscar_url_avatar(request.user)})
       else:
           return render(request , 'indice/editar_usuario.html', {'form': form , 'msj': ' ','url_avatar' : buscar_url_avatar(request.user)})       

   form = EditarUser(
          initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'username': request.user.username
        }
   )    
   return  render(request , 'indice/editar_usuario.html', {'form': form , 'msj': 'Datos actualizados','url_avatar' : buscar_url_avatar(request.user)})  
    



def buscar_url_avatar(user):
     return Avatar.objects.filter(user=user)[0].imagen.url  