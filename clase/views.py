from django.http import HttpResponse
from django.shortcuts import render
from clase.models import Usuario
import random

# Create your views here.

def nuevo_usuario(request):
    nuevo_usuario = Usuario(nombre='florencia' , apellido ='ferrer', email='flor@gmail.com')
    nuevo_usuario.save()
    return HttpResponse(f"se creo nuevo usuario {nuevo_usuario.nombre} ")

def formulario (request):
      return render(request, 'clase/formulario.html',{})