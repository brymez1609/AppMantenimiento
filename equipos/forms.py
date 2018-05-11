from crispy_forms.bootstrap import StrictButton, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, HTML, Field
from django import forms

from equipos.models import Equipos, Tipos_Equipos


class EquiposForm(forms.ModelForm):
    class Meta:
        model = Equipos
        fields = '__all__'
        labels = {
            # 'id_equipos': 'Id equipos',
            'nombre_equipo': 'Nombre:',
            'funcionario': 'Funcionario',
            'cuenta_usuario': 'Usuario',
            'contrasena': 'Contraseña',
            'estado': 'Estado',
            'direccion_ip': 'direccion IP',
            'id_Tipos_Equipos': 'Tipo de equipo',
            'id_Departamento': 'Departamento',
        }

        widgets = {
             'estado':forms.CheckboxInput(attrs={'class':'form-control'}),
             'contrasena': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EquiposForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        helper = self.helper

        helper.form_class = 'form-vertical'
       # helper.label_class = 'col-lg-2'
        #helper.field_class = 'col-lg-8'
        helper.layout = Layout(
            Div(
                Div(Field('nombre_equipo'), css_class='col-sm-4 col-lg-4'),
                Div(Field('funcionario'), css_class='col-sm-3 col-lg-3'),
                Div(Field('cuenta_usuario'), css_class='col-sm-4'),

                css_class='row'
            ),
            Div(
                Div(Field('contrasena'), css_class='col-sm-2 col-lg-2'),
                Div(Field('direccion_ip',placeholder='0 . 0 . 0 . 0'), css_class='col-sm-3 col-lg-3'),
                Div(Field('id_Departamento'), css_class='col-sm-2 col-lg-2'),
                Div(Field('id_Tipos_Equipos'), css_class='col-sm-2 col-lg-2'),
                Div(Field('estado'), css_class='col-sm-3 col-lg-3 ',style='padding-top:35px'),
                css_class='row'
            ),

            #StrictButton('Sign in', css_class='btn-default'),
            Div(
                FormActions(
                    Submit('save', 'Guardar', css_class='btn btn-success'),
                    HTML(
                        '<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>'),
                ),
                style='float:right;padding-right:1%;'
            ),
        )



class TiposEquiposForm(forms.ModelForm):
    class Meta:
        model = Tipos_Equipos
        fields = '__all__'
        labels = {
            'tipo': 'Tipo de equipo',
        }
