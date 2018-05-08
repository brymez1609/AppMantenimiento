from django.db import models
from django.utils import timezone

# Create your models here.
class Departamento(models.Model):
	id_departamento = models.AutoField(primary_key=True, max_length= 5)
	nombre = models.CharField(max_length=20,blank=True,null=True)
	horario = models.DateTimeField(default=timezone.now)
	ubicacion = models.CharField(max_length=20,blank=True,null=True)

	def __str__(self):
		return self.ubicacion