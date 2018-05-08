from django.contrib import admin

# Register your models here.
from equipos.models import Equipos, Tipos_Equipos


class EquiposAdmin(admin.ModelAdmin):
	list_display = ('id_equipos','nombre_equipo','funcionario','cuenta_usuario','contrasena','estado','direccion_ip','id_Tipos_Equipos','id_Departamento')

class TiposEquiposAdmin(admin.ModelAdmin):
	list_display = ('id_tipos_equipos','tipo')

admin.site.register(Equipos,EquiposAdmin)
admin.site.register(Tipos_Equipos,TiposEquiposAdmin)