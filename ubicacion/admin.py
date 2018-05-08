from django.contrib import admin

# Register your models here.
from ubicacion.models import Departamento


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id_departamento','nombre','horario','ubicacion')


admin.site.register(Departamento,DepartamentoAdmin)