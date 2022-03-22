from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField( max_length= 20)
    apellido = forms.CharField( max_length= 50)
    email = forms.CharField( max_length= 30)

  

class BusquedaUsuario(forms.Form):
    partial_email = forms.CharField(label= 'Search: ',max_length=20)