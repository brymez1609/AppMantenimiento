from django.contrib import admin

# Register your models here.
from equipos.models import Equipos, Tipos_Equipos, Mantenimiento


class EquiposAdmin(admin.ModelAdmin):
	list_display = ('id_equipos','nombre_equipo','funcionario','cuenta_usuario','contrasena','estado','direccion_ip','id_Tipos_Equipos','id_Departamento')

class TiposEquiposAdmin(admin.ModelAdmin):
	list_display = ('id_tipos_equipos','tipo')

class MantenimientoAdmin(admin.ModelAdmin):
	list_display = ('id_mantenimiento','fecha','revisado','id_equipos')

admin.site.register(Equipos,EquiposAdmin)
admin.site.register(Mantenimiento, MantenimientoAdmin)
admin.site.register(Tipos_Equipos,TiposEquiposAdmin)