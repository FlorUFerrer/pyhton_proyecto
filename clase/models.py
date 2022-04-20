from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.


class Usuario (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)

    def __str__(self):
        return f" Nombre: {self.nombre} - Apellido: {self.apellido} - E-mail: {self.email}"

class Posteo (models.Model):
    numero = models.IntegerField
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=300)
 
  

    def __str__(self):
        return f" {self.titulo} - Mi posteo: {self.texto}"

class Mascota (models.Model):
    nombre = models.IntegerField
    edad = models.CharField(max_length=5)
    