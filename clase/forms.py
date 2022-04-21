from django import forms
from ckeditor.fields import RichTextFormField

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField( max_length= 20)
    apellido = forms.CharField( max_length= 50)
    email = forms.CharField( max_length= 30)
  #  foto = RichTextFormField(required= False)
  

class BusquedaUsuario(forms.Form):
    partial_email = forms.CharField(label= 'Search: ',max_length=20)



class FormularioBlog(forms.Form):
    titulo = forms.CharField(max_length=30, widget=forms.TextInput(), label="Título")
    subtitulo = forms.CharField(max_length=30, widget=forms.TextInput(), label="Subtítulo")
    texto = RichTextFormField()
    imagen = forms.ImageField(required=False)
    