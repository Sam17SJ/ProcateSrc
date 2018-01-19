from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Comunidad(models.Model):
	"""docstring for Comunidad"""
	id_comunidad=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=100)

	def __unicode__(self): #Python 2
		return self.nombre

	def __str__(self): #Python 3
		return self.nombre

class Area(models.Model):
	"""docstring for Area"""
	id_area=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=256)

	def __unicode__(self): #pyton2
		return self.nombre

	def __str__(self): #pythin 3
		return self.nombre
	
class Grupo(models.Model):
	"""docstring for Grupo"""
	id_grupo=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=100)
	id_comunidad=models.ForeignKey(Comunidad)
	id_area=models.ForeignKey(Area)
	def __unicode__(self): #Python 2
		return self.nombre

	def __str__(self): #Python 3
		return self.nombre
		#return 'Grupo: {}'.format(self.id_grupo)

class Catequista(models.Model):
	"""docstring for Catequista"""
	id_catequista=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=100, null=True)
	id_user=models.ForeignKey(User)
	id_comunidad=models.ForeignKey(Comunidad)
	id_area=models.ForeignKey(Area, null=True)
	id_grupo=models.ForeignKey(Grupo, null=True)
	is_Coordinador=models.BooleanField()
	is_Admin=models.BooleanField()
	is_Secretaria=models.BooleanField()
	
	def __str__(self):
		return '%s' %(self.nombre)

	# def __unicode__(self): #pyton2
	# 	return self.username

	# def __str__(self): #pythin 3
	# 	return self.username


class Catequizando(models.Model):
	"""docstring for Catequizando"""
	id_catequizando=models.AutoField(primary_key=True)
	id_grupo=models.ForeignKey(Grupo)
	nombre=models.CharField(max_length=100) 
	nombre_madre=models.CharField(max_length=100, blank=True, null=True )
	nombre_padre=models.CharField(max_length=100, blank=True, null=True )
	email=models.EmailField(max_length=100) 
	fecha_nacimiento=models.DateField(auto_now=False)
	lugar_de_bautizo=models.CharField(max_length=100, blank=True, null=True )
	fecha_de_bautizo=models.DateField(auto_now=False, null=True) 
	is_activo=models.BooleanField()
	is_final=models.BooleanField()

	def __unicode__(self): #pyton2
		return self.nombre

	def __str__(self): #pythin 3
		return self.nombre

class Asistencia(models.Model):
	"""docstring for Lista"""
	id_asistencia=models.AutoField(primary_key=True)
	id_grupo=models.ForeignKey(Grupo)
	id_catequizando=models.ForeignKey(Catequizando)
	fecha=models.DateField(auto_now_add=False,auto_now=False)

	def __unicode__(self):
		return str(self.fecha)

	def __str__(self):
		return str(self.fecha)

class Boleta(models.Model):
	"""docstring for Boleta"""
	id_boleta=models.AutoField(primary_key=True)
	id_catequizando=models.ForeignKey(Catequizando, related_name='+')
	id_catequista=models.ForeignKey(Catequista)
	id_area=models.ForeignKey(Area)
	id_comunidad=models.ForeignKey(Comunidad)
	fecha=models.DateTimeField(auto_now=True)
	fe_de_bautizo=models.BooleanField()
	partida_de_nacimiento=models.BooleanField()


	def __unicode__(self): #pyton2
		return str(self.id_boleta)

	def __tr__(self): #pythin 3
		return str(self.id_boleta)
