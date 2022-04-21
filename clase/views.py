from sre_constants import SUCCESS
from django.http import HttpResponse
from django.shortcuts import render , redirect
from clase.models import Usuario, Posteo , PosteoBlog
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
        {'buscador':buscador , 'email_buscado':email_buscado , 'dato':dato}
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
        {'formulario' : formulario}
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



class Posteos(ListView):
    model = Posteo
    template_name = 'clase/posteos.html'


class PosteoDetalle(DetailView):
    model = Posteo
    template_name = 'clase/posteo_datos.html'


class PosteoCrear(CreateView):
    model = Posteo
    success_url = '/clase/posteos'
    fields =[ 'titulo' , 'texto']


class PosteoEditar(UpdateView):
    model = Posteo
    success_url = '/clase/posteos'
    fields =[ 'titulo' , 'texto']


class PosteoBorrar(DeleteView):
    model = Posteo
    success_url= '/clase/posteos'
   

########################POSTEO BLOG#########################################


# @login_required
# def crear_blog(request):
#     if request.method == 'POST':
#         form = FormularioBlog(request.POST, request.FILES)
        
#         if form.is_valid():
#             data = form.cleaned_data
#             blog = PosteoBlog(titulo=data['titulo'], subtitulo=data['subtitulo'], mascota=request.user.username, date=datetime.date.today(), texto=data['texto'], imagen=data['imagen'])
#             blog.save()
#             return redirect('inicio')
    
#     form = FormularioBlog()
#     return render(request, "clase/blog.html", {'form': form, 'url_avatar' :  usuario_avatar(request)})

# class BlogDetalle(DetailView):
#     model = PosteoBlog
#     template_name = "index/blog.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['url_avatar'] = usuario_avatar(self.request)
#         return context


# class BlogEditar(UpdateView):
#     model = PosteoBlog
#     success_url = '/pages'
#     fields = ['titulo', 'subtitulo', 'texto', 'imagen']        
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         query_set = self.get_object()
#         if(query_set.image):
#             context['blog_image'] = query_set.image.url

#         context['url_avatar'] = usuario_avatar(self.request)
#         context['form'].fields['titulo'].label = 'Título'
#         context['form'].fields['subtitulo'].label = 'Subtítulo'
#         context['form'].fields['texto'].label = 'Contenido'
#         context['form'].fields['imagen'].label = 'Imagen'
#         # context['form'].fields['image'].widget.clear_checkbox_label = 'Eliminar'
#         # context['form'].fields['image'].widget.initial_text = 'Imagen actual'
#         # context['form'].fields['image'].widget.input_text = 'Cambiar'
#         return context


# class BlogBorrar(DeleteView):
#     model = PosteoBlog
#     success_url = '/pages'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['url_avatar'] = usuario_avatar(self.request)
#         return context