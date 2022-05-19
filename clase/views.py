
from django.http import HttpResponse
from django.shortcuts import render , redirect
from clase.models import Usuario, PosteoBlog
from clase.forms import BusquedaUsuario, FormularioBlog, UsuarioFormulario 
from django.views.generic import ListView , DetailView
from django.views.generic.edit import UpdateView , DeleteView , CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import datetime
from indice.views import usuario_avatar

# Create your views here.

def nuevo_usuario(request):
    nuevo_usuario = Usuario(nombre='florencia' , apellido ='ferrer', email='flor@gmail.com')
    nuevo_usuario.save()
    return HttpResponse(f"se creo nuevo usuario {nuevo_usuario.nombre} ")

def formulario (request):
        if request.method == 'POST':
             formulario =UsuarioFormulario(request.POST)
             if formulario.is_valid():
                 data= formulario.cleaned_data   
                 nuevo_usuario = Usuario(nombre = data['nombre'], apellido = data['apellido'], email= data['email'])   
                 nuevo_usuario.save()  
             return render(request, 'indice/usuario.html',{'nuevo_usuario': nuevo_usuario})     
        formulario = UsuarioFormulario()
        return render(request, 'clase/formulario.html',{'formulario' : formulario})

def busqueda(request):
    email_buscado = []
    dato = request.GET.get('partial_email', None) 
    if dato is not None:
        email_buscado = Usuario.objects.filter(email__icontains = dato)

    buscador = BusquedaUsuario()
    return render (
        request, "clase/busqueda.html", 
        {'buscador':buscador , 'email_buscado':email_buscado , 'dato':dato , 'url_avatar' : usuario_avatar(request)}
    )


#CRUD
def listado_usuarios(request):
    listado_usuarios = Usuario.objects.all()
    return render (
        request, "clase/listado_usuarios.html", 
        {'listado_usuarios':listado_usuarios}
    )


@login_required
def crear_usuario(request):
    if request.method == 'POST':
             formulario = UsuarioFormulario(request.POST)
             if formulario.is_valid():
                 data= formulario.cleaned_data   
                 nuevo_usuario = Usuario(nombre = data['nombre'], apellido = data['apellido'], email= data['email'])   
                 nuevo_usuario.save()  
             return redirect('listado_usuarios')
                
    formulario = UsuarioFormulario()
    return render(
        request, 'clase/crear_usuario.html',
        {'formulario' : formulario , 'url_avatar' : usuario_avatar(request)}
    )



def actualizar_usuario(request , id):

    usuario = Usuario.objects.get(id = id)

    if request.method == 'POST':
             formulario = UsuarioFormulario(request.POST)
             if formulario.is_valid():
                 data= formulario.cleaned_data   
                 usuario.nombre = data ['nombre']
                 usuario.apellido = data ['apellido']
                 usuario.email = data ['email']
                 usuario.save()  
             return redirect('listado_usuarios')
                
    formulario = UsuarioFormulario( 
        initial ={
            'nombre' : usuario.nombre,
            'apellido' : usuario.apellido,
            'email' : usuario.email
        }
    )
    return render(
        request, 'clase/actualizar_usuario.html',
        {'formulario' : formulario, 'usuario' : usuario}
    )
   

def borrar_usuario (request , id):
     usuario = Usuario.objects.get(id = id)
     usuario.delete()
     return redirect('listado_usuarios')


####################################################




class Blogs(ListView):
    model = PosteoBlog
    template_name = 'clase/blogs.html'



class BlogCrear(LoginRequiredMixin ,CreateView ):
     model = PosteoBlog
     success_url = '/clase/blogs'
     fields =['titulo' , 'subtitulo','mascota','autor','date','image','texto']
     


class BlogDetalle(DetailView):
    model = PosteoBlog
    template_name = 'clase/blog_datos.html'



class BlogEditar(LoginRequiredMixin ,UpdateView):
    model = PosteoBlog
    success_url = '/clase/blogs'
    fields =['titulo' , 'subtitulo','mascota','autor','date','image','texto']




class BlogBorrar(DeleteView):
    model = PosteoBlog
    success_url= '/clase/blogs'
   
   ###########################################


@login_required
def crear_blog(request):
    if request.method == 'POST':
             formulario = FormularioBlog(request.POST, request.FILES)
             if formulario.is_valid():
                 data= formulario.cleaned_data   
                 nuevo_blog = PosteoBlog(titulo = data['titulo'], subtitulo = data['subtitulo'], autor= request.user.username, mascota= data['mascota'], date= datetime.date.today(), texto= data['texto'], image= data['image'])   
                 nuevo_blog.save()  
             return redirect('inicio')
                
    formulario = FormularioBlog()
    return render(
        request, 'clase/crear_blog.html',
        {'formulario' : formulario}
       
    )


