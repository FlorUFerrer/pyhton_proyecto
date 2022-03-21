from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# def inicio(self):
#    # mi_pagina = open(r"miproyecto\plantillas\template1.html")
#    # template = Template(mi_pagina.read())
#    #context = Context()
#    template = loader.get_template('navbar.html')
#    documento = template.render()
#    return HttpResponse(documento)

def inicio(request):
   return render(request,'indice/index.html',{})

def usuario(request):
       return render(request,'indice/usuario.html',{})   

def about(request):
       return render(request,'indice/about.html',{})   


