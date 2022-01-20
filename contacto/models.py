from django.db import models

from calendar import c
from distutils.command.upload import upload
from tabnanny import verbose




# Crear el mapeo del ORM de servicio
class Contacto(models.Model):
     nombre = models.CharField( max_length=50)
     contenido = models.CharField( max_length=50)
     created = models.DateField(auto_now_add=True)
     updated = models.DateField(auto_now_add=True)

     class Meta: 
         verbose_name = 'contacto'
         verbose_name_plural = 'contactos'

     def __str__(self):
        return self.nombre


