from django.db import models

# Create your models here.

class Colaborador(models.Model): 
    rut = models.CharField(max_length=10,primary_key=True, verbose_name='RUT')
    foto = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    telefono = models.CharField(max_length=9, verbose_name='Telefono')
    direccion = models.CharField(max_length=40, verbose_name='Direccion')
    correo = models.CharField(max_length=40, verbose_name='Correo')
    pais = models.CharField(max_length=40, verbose_name='Pais')
    contraseña = models.CharField(max_length=100, null=True, blank=True, verbose_name='Contraseña')

    def __str__(self):
        return self.rut