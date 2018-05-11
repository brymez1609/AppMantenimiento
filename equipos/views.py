from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string

from equipos.forms import EquiposForm, TiposEquiposForm
from equipos.models import Equipos, Tipos_Equipos, Mantenimiento


def index(request):
    context = {
        'inicio': 'inicio'
    }
    return render(request, 'index.html', context)


def equipo_list(request):
    equipos = Equipos.objects.all()
    return render(request, 'equipos/equipo_list.html', {'equipos': equipos})


def guargar_equipo_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            equipos = Equipos.objects.all()
            data['html_equipo_list'] = render_to_string('equipos/includes/partial_equipos_list.html', {
                'equipos': equipos
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def equipo_create(request):
    if request.method == 'POST':
        form = EquiposForm(request.POST)
    else:
        form = EquiposForm()
    return guargar_equipo_form(request, form, 'equipos/includes/partial_equipos_create.html')


def equipo_update(request, pk):
    equipo = get_object_or_404(Equipos, pk=pk)
    if request.method == 'POST':
        form = EquiposForm(request.POST, instance=equipo)
    else:
        form = EquiposForm(instance=equipo)
    return guargar_equipo_form(request, form, 'equipos/includes/partial_equipos_update.html')


def equipos_delete(request, pk):
    equipo = get_object_or_404(Equipos, pk=pk)

    data = dict()
    if request.method == 'POST':
        equipo.delete()
        data['form_is_valid'] = True
        equipos = Equipos.objects.all()
        data['html_equipo_list'] = render_to_string('equipos/includes/partial_equipos_list.html', {
            'equipos': equipos
        })
    else:
        context = {'equipos': equipo}
        print(equipo.id_equipos)
        data['html_form'] = render_to_string('equipos/includes/partial_equipos_delete.html', context, request=request)
    return JsonResponse(data)


#------------------------------Tipo de Equipos --------------------------------------"
def tipo_equipos_list(request):
    tipos_equipos = Tipos_Equipos.objects.all()
    return render(request,'TipoEquipos/tipo_equipo_list.html',{'tipos_equipos':tipos_equipos})


def guargar_tipo_equipo_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            tipos_equipos = Tipos_Equipos.objects.all()
            data['html_tipo_equipo_list'] = render_to_string('TipoEquipos/includes/partial_tipo_equipos_list.html', {
                'tipos_equipos': tipos_equipos
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def tipo_equipo_create(request):
    if request.method == 'POST':
        form = TiposEquiposForm(request.POST)
    else:
        form = TiposEquiposForm()
    return guargar_tipo_equipo_form(request, form, 'TipoEquipos/includes/partial_tipo_equipos_create.html')


def tipo_equipo_update(request, pk):
    tipo_equipo = get_object_or_404(Tipos_Equipos, pk=pk)
    if request.method == 'POST':
        form = TiposEquiposForm(request.POST, instance=tipo_equipo)
    else:
        form = TiposEquiposForm(instance=tipo_equipo)
    return guargar_tipo_equipo_form(request, form, 'TipoEquipos/includes/partial_tipo_equipos_update.html')

def tipo_equipos_delete(request, pk):
    tipo_equipo = get_object_or_404(Tipos_Equipos, pk=pk)
    data = dict()
    if request.method == 'POST':
        tipo_equipo.delete()
        data['form_is_valid'] = True
        tipo_equipos = Tipos_Equipos.objects.all()
        data['html_tipo_equipo_list'] = render_to_string('TipoEquipos/includes/partial_tipo_equipos_list.html', {
            'tipos_equipos': tipo_equipos
        })
    else:
        context = {'tipos_equipos': tipo_equipo}
        data['html_form'] = render_to_string('TipoEquipos/includes/partial_tipo_equipos_delete.html', context, request=request)
    return JsonResponse(data)

# -------------------------- Mantenimiento ------------------------------- #
def mantenimiento_list(request):
    mantenimientos = Mantenimiento.objects.all()
    return render(request,'notification_panel.html',{'mantenimientos_list':mantenimientos})
