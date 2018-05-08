from django.db import models
from ubicacion.models import Departamento

# Create your models here.
class Usuarios(models.Model):
	id_usuarios = models.AutoField(primary_key=True, max_length=5)
	nombre = models.CharField(max_length=20, blank=True, null=True)
	apellido = models.CharField(max_length=20, blank=True, null=True)
	cargo = models.CharField(max_length=20, blank=True)
	id_rol = models.ForeignKey('Rol', on_delete= models.CASCADE)
	id_departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)

class Rol(models.Model):
	id_rol = models.AutoField(primary_key=True,max_length=5) 
	rol = models.CharField(max_length=20,blank=True,null=True)
