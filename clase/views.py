from django.http import HttpResponse
from django.shortcuts import render
from clase.models import Usuario
from clase.forms import BusquedaUsuario, UsuarioFormulario

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
    #SIN FORMULARIO DE DJANGO
    #   if request.method == 'POST':
    #     print(request.POST)
    #     nuevo_usuario = Usuario(nombre =request.POST['nombre'], apellido = request.POST['apellido'], email= request.POST['email'])    
    #     nuevo_usuario.save()  
    #     return render(request, 'indice/usuario.html',{'nuevo_usuario': nuevo_usuario})
    #   return render(request, 'clase/formulario.html',{})
    #Con formulario de django



def busqueda(request):
    email_buscado = []
    dato = request.GET.get('partial_email', None) 
    if dato is not None:
        email_buscado = Usuario.objects.filter(email__icontains = dato)

    buscador = BusquedaUsuario()
    return render (request, "clase/busqueda.html", {'buscador':buscador , 'email_buscado':email_buscado , 'dato':dato})