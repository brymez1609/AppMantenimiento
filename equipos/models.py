from django.db import models
from ubicacion.models import Departamento

# Create your models here.
class Equipos(models.Model):
	id_equipos = models.AutoField(primary_key=True,max_length=5)
	nombre_equipo = models.CharField(max_length=20,blank=True,null=True)
	funcionario = models.CharField(max_length=45,blank=True,null=True)
	cuenta_usuario = models.CharField(max_length=20,blank=True,null=True)
	contrasena = models.CharField(max_length=20,blank=True,null=True)
	estado = models.CharField(max_length=10,blank=True,null=True)
	direccion_ip= models.GenericIPAddressField(max_length=15)
	id_Tipos_Equipos = models.ForeignKey('Tipos_Equipos', on_delete=models.CASCADE)
	id_Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre_equipo

class Tipos_Equipos(models.Model):
	id_tipos_equipos = models.AutoField(primary_key=True,max_length=5)
	tipo = models.CharField(max_length=20,blank=True,null=True)
    
	def __str__(self):
		return self.tipo


class Software(models.Model):
	id_software = models.AutoField(primary_key=True,max_length=5)
	fecha_instalacion = models.DateTimeField()
	nombre = models.CharField(max_length=20,blank=True,null=True)
	descripcion = models.CharField(max_length=1000,blank=True,null=True)
	licencia = models.CharField(max_length=25,blank=True,null=True)
	tipo_licencia = models.CharField(max_length=45,blank=True,null=True)
	id_equipo = models.ForeignKey('Equipos', on_delete=models.CASCADE)

class Hardware(models.Model):
	id_hardware = models.AutoField(primary_key=True,max_length=5)
	hardware = models.CharField(max_length=20,blank=True,null=True)
	marca = models.CharField(max_length=20,blank=True,null=True)
	serial = models.CharField(max_length=25,blank=True,null=True)
	id_equipos = models.ForeignKey('Equipos', on_delete=models.CASCADE)

class Modelos(models.Model):
	id_modelo = models.AutoField(primary_key=True,max_length=5)
	modelo = models.CharField(max_length=20,blank=True,null=True)
	id_equipos = models.ForeignKey('Equipos', on_delete= models.CASCADE)

class Historial(models.Model):
	id_historial = models.AutoField(primary_key=True,max_length=5)
	historial = models.CharField(max_length=100,blank=True,null=True)
	fecha= models.DateTimeField()
	descripcion = models.CharField(max_length=100,blank=True,null=True)

