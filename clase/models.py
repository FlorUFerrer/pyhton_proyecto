from mailbox import NoSuchMailboxError
from django.db import models
from django.forms import CharField
from ckeditor.fields import RichTextField
# Create your models here.


class Usuario (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
   # foto = models.RichTextField(null=True ,blank=True)

    def __str__(self):
        return f" Nombre: {self.nombre} - Apellido: {self.apellido} - E-mail: {self.email}"

class Posteo (models.Model):
    numero = models.IntegerField
    titulo = models.CharField(max_length=50)
    #subtitulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=300)
 

    def __str__(self):
        return f" {self.titulo} - Mi posteo: {self.texto}"

        
class PosteoBlog (models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    mascota = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    date = models.DateField()
    texto = RichTextField(blank=True , null=True )
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
            return f"{self.titulo} {self.texto} {self.date}{self.image} {self.mascota}"


class Mascota (models.Model):
    nombre = models.IntegerField
    edad = models.CharField(max_length=5)
    