
from django.http import HttpResponse


from django.http import HttpResponse

def inicio(request):
    return HttpResponse('Hola, soy la nueva página')

def otra_vista(request):
    return HttpResponse('''
                        <h1>Soy un titulo</h1>
                        
                        ''')