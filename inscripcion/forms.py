from django import forms
from django.contrib.admin import widgets
from .models import *
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 

class Login(forms.Form):
	Nombre_de_Usuario=forms.CharField(max_length=25)
	Contraseña=forms.CharField(max_length=25)

class ComunidadForm(forms.ModelForm):
	class Meta:
		model=Comunidad
		fields={'nombre'}
		labels={'nombre':'Nombre de la comunidad'}


class AreaForm(forms.ModelForm):
	class Meta:
		model=Area
		fields={'nombre','descripcion'}
		labels={'nombre':'Nombre de la area',
				'descripcion':'Descripcion del area'
		}

class CatequistaForm(forms.ModelForm):
	class Meta:
		model=Catequista
		fields={
		'nombre',
		'id_comunidad',
		}
		labels={
		'nombre':'Ingrese su nombre',
		'id_comunidad':'Comunidad pertenece',
		}
	Email=forms.EmailField(max_length=100)


class Inscribir(forms.Form):
	Nombre=forms.CharField(max_length=100)
	Nombre_madre=forms.CharField(max_length=100, required=False )
	Nombre_padre=forms.CharField(max_length=100, required=False)
	Email=forms.EmailField(max_length=100, required=False) 
	Fecha_de_nacimiento=forms.DateField(required=False)
	Lugar_de_bautizo=forms.CharField(max_length=100, required=False)
	Fecha_de_bautizo=forms.DateField(required=False) 
	fe_de_bautizo=forms.BooleanField(required=False)
	partida_de_nacimiento=forms.BooleanField(required=False)
	grupo=forms.ModelChoiceField(queryset=Grupo.objects.all())

class catequizandoEdit(forms.ModelForm):
	class Meta:
		model=Catequizando
		fields={
		 'nombre',
		 'nombre_madre',
		 'nombre_padre',
		 'email',
		 'fecha_nacimiento',
		 'fecha_de_bautizo',
		 'lugar_de_bautizo',
		 'is_activo',
		}
		labels={
		'nombre':'Nombre',
		 'nombre_madre':'Nombre de la madre',
		 'nombre_padre':'Nombre de el padre',
		 'email':'Correo electronico',
		 'fecha_nacimiento':'Fecha de nacimiento',
		 'fecha_de_bautizo':'Fecha de bautizo',
		 'lugar_de_bautizo':'Lugar de bautizo',
		 'is_activo':'Habilitar o inhabilitar'
		}

class boletaEdit(forms.ModelForm):
	class Meta:
		model=Boleta
		fields={
		'id_area',
		'fe_de_bautizo',
		'partida_de_nacimiento',
		}
		labels={
		'id_area':'Area',
		'fe_de_bautizo':'Fe de bautizo',
		'partida_de_nacimiento':'Partida de nacimiento',
		}

class CatequistaEdit(forms.ModelForm):
	class Meta:
		model=Catequista
		fields={
		'id_area',
		'id_grupo',
		}
		labels={
		'id_area':'Area',
		'id_grupo':'Grupo'
		}

class AsistenciaForm(forms.Form):
	fecha=forms.DateField(required=False) 
	# arr=Catequizando.objects.all()
	# choice=[]
	# for i in arr:
	# 	choice.append(i.nombre)
	# 	print(i.nombre)
	# catequizando=forms.MultipleChoiceField(choices=choice, widget=forms.CheckboxSelectMultiple)
	# asistir=forms.BooleanField(required=False)
	
# class BoletaModel(forms.ModelForm):
# 	"""docstring for Comunidad"""
# 	class Meta:
# 		model=Boleta
# 		fields=["id_catequizando","id_catequista","id_area","id_comunidad","fe_de_bautizo","partida_de_nacimiento",]

# 	def __init__(self, arg):
# 		super(BoletaModel, self).__init__()
# 		self.arg = arg


		
#comentario: NEXT

class AsisForm(forms.Form):
	fecha=forms.DateField(required=False)
	asis=forms.BooleanField(required=False)

class GrupoForms(forms.ModelForm):
	class Meta:
		model=Grupo

		fields={
		'id_area',
		'nombre',
		}
		labels={
		'nombre':'Ingrese Nombre Grupo',
		'id_area':'Nombre Area',
		}
class GrupoForms2(forms.ModelForm):
	class Meta:
		model=Grupo

		fields={
		'id_area',
		'nombre',
		'id_comunidad',
		}
		labels={
		'nombre':'Ingrese Nombre Grupo',
		'id_area':'Nombre Area',
		'id_comunidad':'Seleccione la comunidad'
		}