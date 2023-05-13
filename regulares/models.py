from django.db import models

# Create your models here.

class contactos(models.Model):
    Clave_cliente = models.CharField(max_length=50)
    Nombre_Contacto = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)