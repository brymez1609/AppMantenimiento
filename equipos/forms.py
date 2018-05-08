from django import forms

from equipos.models import Equipos


class EquiposForm(forms.ModelForm):
	class Meta:
		model = Equipos

		fields = '__all__'

		labels = {
			#'id_equipos': 'Id equipos',
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
			#'id_equipos':forms.TextInput(attrs={'class':'form-control'}),
			'nombre_equipo':forms.TextInput(attrs={'class':'form-control','':''}),
			'id_Tipos_Equipos':forms.Select(attrs={'class':'form-control'}),
			'id_Departamento':forms.Select(attrs={'class':'form-control'}),
		}
	"""
	def clean_nombre_equipo(self):
		return self.cleaned_data['nombre_equipo'].upper()

	def clean_funcionario(self):
		return self.cleaned_data['funcionario'].lower()

	def clean_cuenta_usuario(self):
		return self.cleaned_data['cuenta_usuario'].lower()
	"""