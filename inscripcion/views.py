from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.db.models import Count


from django.http import HttpResponse

import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
this_path = os.getcwd()+'/polls/'

#Permite Login en el Sistema segun el Rol asignado por el(los) Administrador/es
def inicio(request):
	a=""
	if request.method=='POST':
		form=AuthenticationForm(request.POST)
		if form.is_valid:
			usuario=request.POST['username']
			clave=request.POST['password']
			user= authenticate(username=usuario, password=clave)
			if user is not None:
				if user.is_active:
					ente=Catequista.objects.get(id_user=user.id)
					login(request, user)
					return redirect('menu')
				else:
					return render(request, "noActivoo.html")
			else:
				a="Error al ingresar datos"
	else:
		form=AuthenticationForm()
		if request.user.is_active:
			return redirect('menu')			 
	context={
		"form":form,
		"are":a,
	} 
	return render(request, "inicio.html", context)


#Cierra el sistema ProCate
@login_required(login_url='inicio')
def cerrar(request):
	logout(request)
	return redirect('/')


@login_required(login_url='inicio')
def boleta(request):		
	coor=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	catequista=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo
	print(ente.is_Secretaria)
	if coor.is_Secretaria:
		redirect('inicio')
	else:
		if request.user.is_active:
			form=Inscribir(request.POST or None)
			catequista=Catequista.objects.get(id_user=request.user.id)
			if coor.is_Admin:
				form.fields['grupo'].queryset = Grupo.objects.all()
			else:
				form.fields['grupo'].queryset = Grupo.objects.filter(id_comunidad=catequista.id_comunidad) 
			titulo="Hola"
			if request.user.is_authenticated():
				titulo="Bienvenido %s" %(request.user)
			if form.is_valid():
				datos=form.cleaned_data
				name=datos.get('Nombre')
				name_mon=datos.get('Nombre_madre')
				name_father=datos.get('Nombre_padre')
				email=datos.get('Email')
				date=datos.get('Fecha_de_nacimiento')
				lugar=datos.get('Lugar_de_bautizo')
				date_bau=datos.get('Fecha_de_bautizo')
				fe=datos.get('fe_de_bautizo')
				partida=datos.get('partida_de_nacimiento')
				grupo=datos.get('grupo')
				Catequizando.objects.create(id_grupo=grupo, nombre=name, nombre_madre=name_mon, nombre_padre=name_father, email=email, fecha_nacimiento=date, lugar_de_bautizo=lugar, fecha_de_bautizo=date_bau ,is_activo=True, is_final=False)
				objt=Catequizando.objects.latest('id_catequizando')
				ida=grupo.id_area
				comunidad=grupo.id_comunidad
				Boleta.objects.create(id_catequizando=objt, id_area=ida,id_comunidad=comunidad,fe_de_bautizo=fe, partida_de_nacimiento=partida, id_catequista=catequista )
	context={
		"boletaForm":form,
		'coor':ente,
		'grupo':grupo,

	}
	return render(request, "inscribir.html", context)


@login_required(login_url='inicio')
def comunidad(request):
	catequista=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo

	if catequista.is_Admin:
		form=ComunidadForm(request.POST or None)
		objt=Comunidad.objects.all()
		if form.is_valid():
			form.save()
			return redirect('listaComunidad')
	else:
		return redirect('inicio')
	context={
		'comunidad':form,
		'coor':ente,
		'grupo':grupo,

	} 
	return render(request, "comunidad.html", context)

@login_required(login_url='inicio')
def comunidad_edit(request, id_com):
	comunidad=Comunidad.objects.get(id_comunidad=id_com)
	catequista=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	catequista=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo

	if catequista.is_Admin:
		if request.method== 'GET':
			form = ComunidadForm(instance=comunidad)
		else:
			form= ComunidadForm(request.POST, instance=comunidad)
			if form.is_valid():
				form.save()
			return redirect('listaComunidad')
	else:
		return redirect('inicio')
	objt=Comunidad.objects.all()
	context={
		'comunidad':form,
		'coor':ente,
		'grupo':grupo,

	}
	return render(request, 'comunidad.html', context)

@login_required(login_url='inicio')
def comunidad_eliminar(request, id_com):
	catequista=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	catequista=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo

	if catequista.is_Admin:
		comunidad=Comunidad.objects.get(id_comunidad=id_com)
		if request.method== 'POST':
			comunidad.delete()
			return redirect('listaComunidad')
	else:
		return redirect('inicio')	
	context={
		'com':comunidad,
		'coor':ente,
		'grupo':grupo,
	}
	return render(request, 'comunidad_delete.html', context )

@login_required(login_url='inicio')
def listarComunidad(request):
	catequista=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	catequista=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo

	if catequista.is_Admin:
		objt=Comunidad.objects.all()
	else:
		return redirect('inicio')
	context={
		"comunidades":objt,
		'coor':ente,
		'grupo':grupo,
	} 
	return render(request, "listarComunidad.html", context)



@login_required(login_url='inicio')
def area(request):
	catequista=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo
	context={
	}
	if catequista.is_Admin or catequista.is_Coordinador:
		form=AreaForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('listaArea')
	else:
		return redirect('inicio')
	context={
		'area':form,
		'coor':ente,
		'grupo':grupo,
	}
	return render(request, "area.html", context)

@login_required(login_url='inicio')
def listarArea(request):
	catequista=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo

	if catequista.is_Admin or catequista.is_Coordinador:
		objt=Area.objects.all()
	else:
		return redirect('inicio')
	context={
		'areas':objt,
		'coor':ente,
		'grupo':grupo,
	}
	return render(request, "listaArea.html", context)

@login_required(login_url='inicio')
def area_editar(request, id_ar):
	catequista=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo

	if catequista.is_Admin or catequista.is_Coordinador:
		are=Area.objects.get(id_area=id_ar)
		if request.method== 'GET':
			form = AreaForm(instance=are)
		else:
			form= AreaForm(request.POST, instance=are)
			if form.is_valid():
				form.save()
			return redirect('area')
	else:
		return redirect('inicio')
	context={
		'area':form,
		'coor':ente,
		'grupo':grupo,

	}
	return render(request, 'area.html', context)

@login_required(login_url='inicio')
def area_eliminar(request, id_ar):
	catequista=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	catequista=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo

	if catequista.is_Admin or catequista.is_Coordinador:
		are=Area.objects.get(id_area=id_ar)
		if request.method== 'POST':
			are.delete()
			return redirect('listaArea')
	else:
		return redirect('inicio')
	context={
		'area':are,
		'coor':ente,
		'grupo':grupo,
	}
	return render(request, 'area_delete.html', context )


def catequista_crear(request):
	if request.user.is_active:
		return redirect('menu')
	formUser=UserCreationForm(request.POST or None)
	form=CatequistaForm(request.POST or None)
	if request.POST:
		if form.is_valid() and formUser.is_valid():
			usuario=User(username=request.POST['username'], email=request.POST['Email'], is_active=False)
			usuario.set_password(request.POST['password1'])
			usuario.save()
			us=User.objects.latest('id')
			com=Comunidad.objects.get(id_comunidad=request.POST['id_comunidad'])
			catequista=Catequista(nombre=request.POST['nombre'], id_comunidad=com, id_user=us,is_Admin=False,is_Coordinador=False,is_Secretaria=False)
			catequista.save()
			return render(request, "registroCompleto.html")
	context={
		'form':form,
		'user':formUser,
	}
	return render(request, "crearCatequista.html", context)


@login_required(login_url='inicio')
def EditarCatequizando(request,id_cat):
	coor=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	catequista=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo

	if coor.is_Secretaria:
		return redirect('inicio')
	else:
		bol=Boleta.objects.get(id_catequizando=id_cat)
		cat=Catequizando.objects.get(id_catequizando=id_cat)
		

		if request.method== 'GET':
			form1=catequizandoEdit(instance=cat)
			form2=boletaEdit(instance=bol)
		else:
			form1=catequizandoEdit(request.POST, instance=cat)
			form2=boletaEdit(request.POST, instance=bol)
			if form1.is_valid():
				form1.save()
			if form2.is_valid():
				form2.save()
			return redirect('listaCatequizando')
		context={
			'form1':form1,
			'form2':form2,
			'coor':ente,
			'grupo':grupo,

		}
		return render(request, "edit_catequizando.html", context)


@login_required(login_url='inicio')
def ListCatequizando(request):
	coor=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	catequista=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo

	if coor.is_Secretaria:
		return redirect('inicio')
	else:
		catequista=Catequista.objects.get(id_user=request.user.id)
		objt=Catequizando.objects.filter(id_grupo=grupo)
		context={
			'catequizando':objt,
			'comunidad':catequista,
			'coor':ente,
			'grupo':grupo,

		}
		return render(request, "listaCatequizando.html", context)




def manejoCatequistas(request):

	catequista=Catequista.objects.get(id_catequista=request.user.id)
	if catequista.is_Admin:
		objt=Catequista.objects.all()
	else:
		if catequista.is_Coordinador:
			objt=Catequista.objects.filter(id_comunidad=catequista.id_comunidad)
		else:
			return redirect('inicio')
	context={
		'catequistas':objt,
	}
	return render(request, "catequistas.html", context)


@login_required(login_url='inicio')
def ActivarCatequista(request):
	objt=User.objects.filter(is_active=False)
	catequista=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo
	context={
	}
	list2=[]
	if catequista.is_Admin or catequista.is_Coordinador:
		for i in objt:
			catlis=Catequista.objects.get(id_user=i.id)
			if catequista.is_Admin:
				list2.append(catlis)
			else:
				if catequista.is_Coordinador:
					if catlis.id_comunidad == catequista.id_comunidad:
						list2.append(catlis)
				else:
					redirect('menu')

		context={
			'lis':list2,
			'coor':ente,
			'grupo':grupo,

		}
		return render(request, 'ActivarCatequista.html', context)
	else:
		return redirect('inicio')

@login_required(login_url='inicio')
def activar(request, id_cat):
	catequista=Catequista.objects.get(id_catequista=id_cat)
	user=catequista.id_user
	user.is_active=True
	user.save()
	return redirect('activarUser')


@login_required(login_url='inicio')
def gruponew(request):
	catequista=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	catequista=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo

	if catequista.is_Admin:
		formgrup=GrupoForms2(request.POST or None)
	else:
		if catequista.is_Coordinador:
			formgrup = GrupoForms(request.POST or None)
		else:
			return redirect('inicio')

	com=catequista.id_comunidad
	print(com)

	if request.method=='POST':
		if formgrup.is_valid():
			if catequista.is_Admin:
				formgrup.save()
			else:
				datos=formgrup.cleaned_data
				area=datos.get('id_area')
				nom=datos.get('nombre')
				g=Grupo.objects.create(id_area=area, nombre=nom, id_comunidad=com)
				g.save()
			return redirect('listgrupo')

			
	context={
		"group":formgrup,
		"comunidad":com,
		'coor':ente,
		'grupo':grupo,

	}
	return render(request,"ingresar_grupo.html",context)

@login_required(login_url='inicio')
def listgrupo(request):
	ente=Catequista.objects.get(id_user=request.user.id)
	catequista=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo
	print(ente.is_Secretaria)

	list_comunidad = Grupo.objects.all()
	if request.method == 'POST':
		return redirect('inggrupo')
	context={
		"lisgrupo":list_comunidad,
		'coor':ente,
		'grupo':grupo,
	}
	return render(request,"list_grupo.html",context)

@login_required(login_url='inicio')
def grupo_edit(request, id_gru):
	catequista=Catequista.objects.get(id_user=request.user.id)
	grupo = Grupo.objects.get(id_grupo=id_gru)

	ente=Catequista.objects.get(id_user=request.user.id)
	catequista=Catequista.objects.get(id_user=request.user.id)
	grup=catequista.id_grupo
	print(ente.is_Secretaria)
	context={
		
	}

	com=grupo.id_comunidad

	if request.method=='GET':
		if catequista.is_Admin:
			form=GrupoForms2(instance=grupo)
		else:
			if catequista.is_Coordinador:
				form=GrupoForms(instance=grupo)
	else:
		if catequista.is_Admin:
			form = GrupoForms2(request.POST, instance=grupo)
			if form.is_valid():
				form.save()
		else:
			if catequista.is_Coordinador:
				form = GrupoForms(request.POST, instance=grupo)
				if form.is_valid():
					form.save()
		return redirect('listgrupo')
	objt=Grupo.objects.all()
	context = {
		"group":form,
		"comunidad":com,
		'coor':ente,
		'grupo':grup,
	}
	return render(request, 'ingresar_grupo.html', context)

@login_required(login_url='inicio')
def grupo_eliminar(request, id_gru):
	grupo = Grupo.objects.get(id_grupo = id_gru)
	ente=Catequista.objects.get(id_user=request.user.id)
	catequista=Catequista.objects.get(id_user=request.user.id)
	grup=catequista.id_grupo
	print(ente.is_Secretaria)

	if request.method == 'POST':
		grupo.delete()
		return redirect('listgrupo')
	context = {
		'grup':grupo,
		'coor':ente,
		'grupo':grup,
	}
	return render(request, 'eliminar_grupo.html',context)


@login_required(login_url='inicio')
def menu (request):
	ente=Catequista.objects.get(id_user=request.user.id)
	catequista=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo
	print(ente.is_Secretaria)
	context={
		'coor':ente,
		'grupo':grupo,
	}
	return render (request, "menu.html",context)

@login_required(login_url='inicio')
def gestioncate (request):
	return render (request, "gestioncate.html")

@login_required(login_url='inicio')
def gestionuser (request):
	return render (request, "gestionuser.html")

@login_required(login_url='inicio')
def comunidadesges (request):
	return render (request, "comunidadges.html")


@login_required(login_url='inicio')
def list_gruposcate(request):
	catequista=Catequista.objects.get(id_user=request.user.id)
	cgrupo=Grupo.objects.get(id_grupo=catequista.id_catequista)
	allgrupo=Grupo.objects.all()
	print(cgrupo)
	casis=Asistencia.objects.get(id_asistencia=cgrupo.id_grupo)
	print(casis)
	ente=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo
	print(ente.is_Secretaria)
	context={
	}
	if catequista.is_Admin:
		context={
			'grup':allgrupo,
			'coor':ente,
			'grupo':grupo,

		}
		return render(request,"listgrupocate.html", context)
	else:
		if catequista.is_Coordinador:

			return render(request,"listgrupocate.html")
		else:
			if catequista.is_Secretaria:
				return redirect('inicio')
			else:
				return redirect('inicio')

	#if len(cgrupo.size) == 0:
	#	return redirect('errorgrupo')

	return render (request, "listgrupocate.html")


@login_required(login_url='inicio')
def asistencia(request):
	form=AsistenciaForm(request.POST or None)
	catequista=Catequista.objects.get(id_user=request.user.id)
	lis=Catequizando.objects.filter(id_grupo=catequista.id_grupo).filter(is_activo=True)
	ente=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo


	if request.method=='POST':
		if form.is_valid():
			datos=form.cleaned_data
			fecha=datos.get('fecha')
			for element in request.POST.getlist('asis'):
				grupo=grupo
				catequizando=Catequizando.objects.get(id_catequizando=element)
				Asistencia.objects.create(id_grupo=grupo, id_catequizando=catequizando, fecha=fecha)
	context={
		'asis':form,
		'cate':lis,
		'coor':ente,
		'grupo':grupo,
	}
	return render(request, "Asistencia.html", context)

@login_required(login_url='inicio')
def asis_porgrupo(request, id_gru):

	catequista=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo

	objt=Catequizando.objects.filter(id_grupo=id_gru).filter(is_activo=True)
	listaAsistencias=Asistencia.objects.filter(id_grupo=id_gru).order_by('fecha')
	listF=[]
	fechaA=None
	for a in listaAsistencias:
		if a.fecha != fechaA:
			fechaA=a.fecha
			listF.append(fechaA)
	listasA=[]
	for b in objt:
		asistir=[]
		ban=0
		for c in listF:
			asis=Asistencia.objects.filter(id_catequizando=b.id_catequizando,fecha=c)
			if asis.count()!=0:
				vino=True
				asistir.append(vino)
			else:
				vino=False
				asistir.append(vino)
				ban+=1
		if ban>3:
			btn=True
		else:
			btn=False
		objt2={
		'jv':b,
		'asis':asistir,
		'btn':btn,
		}
		listasA.append(objt2)
	context={
		'cate':listasA,
		'fechas':listF,
		'coor':ente,
		'grupo':grupo,
	}
	return render(request,"asis_por_grupo.html",context)


@login_required(login_url='inicio')
def inhabilitar(request, id_cate):
	cat=Catequizando.objects.get(id_catequizando=id_cate)
	cat.is_activo=False
	cat.save()
	return redirect('menu')


@login_required(login_url='inicio')
def asignarRol(request):
	objt=User.objects.filter(is_active=True)
	catequista=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo

	if catequista.is_Admin:
		list2=[]
		for i in objt:
			cat=Catequista.objects.get(id_user=i.id)
			if cat!=None:
				if cat.id_user!=request.user:
					list2.append(cat)
			
		context={
			'lis':list2,
			'coor':ente,
			'grupo':grupo,
		}
		return render(request, 'asignarRol.html', context)
	else:
		return redirect('menu')


@login_required(login_url='inicio')
def rolAdm(request,id_cate):
	cat=Catequista.objects.get(id_catequista=id_cate)
	print('llego')
	cat.is_Admin=True
	cat.is_Coordinador=True
	cat.is_Secretaria=False
	cat.save()
	return redirect('asignarRol')

@login_required(login_url='inicio')
def rolCoo(request,id_cate):
	cat=Catequista.objects.get(id_catequista=id_cate)
	cat.is_Admin=False
	cat.is_Coordinador=True
	cat.is_Secretaria=False
	cat.save()
	return redirect('asignarRol')

@login_required(login_url='inicio')
def rolSec(request,id_cate):
	cat=Catequista.objects.get(id_catequista=id_cate)
	cat.is_Admin=False
	cat.is_Coordinador=False
	cat.is_Secretaria=True
	cat.save()
	return redirect('asignarRol')

@login_required(login_url='inicio')
def rolCat(request,id_cate):
	cat=Catequista.objects.get(id_catequista=id_cate)
	cat.is_Admin=False
	cat.is_Coordinador=False
	cat.is_Secretaria=False
	cat.save()
	return redirect('asignarRol')


@login_required(login_url='inicio')
def asignarAreaGrupo(request):
	objt=User.objects.filter(is_active=True)
	catequista=Catequista.objects.get(id_user=request.user.id)
	ente=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo
#	grupo=catequista.id_grupo
	if catequista.is_Admin or catequista.is_Coordinador:
		list2=[]
		for i in objt:
			cat=Catequista.objects.get(id_user=i.id)
			if cat!=None:
				if cat.id_user!=request.user:
					list2.append(cat)
			
		context={
			'lis':list2,
			'grupo':grupo,
			'coor':ente,
		}
		return render(request, 'asignarAreaGrupo.html', context)
	else:
		return redirect('menu')

@login_required(login_url='inicio')
def asigareagrupo(request, id_cate):
	objt=Catequista.objects.get(id_catequista=id_cate)
	ente=Catequista.objects.get(id_user=request.user.id)
	catequista=Catequista.objects.get(id_user=request.user.id)
	grupo=catequista.id_grupo

	print(objt.id_catequista)
	if request.method=='GET':
		form=CatequistaEdit(instance=objt)
	else:
		form = CatequistaEdit(request.POST, instance=objt)
		if form.is_valid():
			form.save()
			# cat=Catequista.objects.get(id_catequista=id_cate)
			# gr=Grupo.objects.get(id_grupo=cat.id_catequista)
			# cat.id_area=Area.objects.get(id_area=gr.id_grupo)
			#cat.save()
		return redirect('asignarAreaGrupo')
	
	context = {
		"catequista":form,
		"cate":objt,
		'coor':ente,
		'grupo':grupo,

	}
	return render(request,'asigareagrupo.html',context)

@login_required(login_url='inicio')
def buscarCate(request):
	catequizandos=Catequizando.objects.all()
	ente=Catequista.objects.get(id_user=request.user.id)
	print(catequizandos)
	if request.method=='POST':
		buscar=request.POST['buscalo']
		cate=Catequizando.objects.filter(nombre__contains=buscar)
		print(cate)
		context = {
			'cate':cate,
			'coor':ente,
		}
		return render(request,'buscardorCate.html',context)	
	else:
		context = {
			'cate':catequizandos,
			'coor':ente,
		}
		return render(request,'buscardorCate.html',context)

@login_required(login_url='inicio')
def ImprimirBol(request,id_cat):
	catequizando=Catequizando.objects.get(id_catequizando=id_cat)
	print(catequizando.nombre)
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition']='attachment ; filename=Cerficado-Confirma.pdf'
	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)

	c.setFont('Helvetica',10)
	c.drawString(375,800,"Parroquia San Bartolomé Apósto")
	c.drawString(375,790,"San Bartolo, Ilopango")


	c.setFont('Helvetica',20)
	c.drawString(100,700,"CERTIFICADO DE PRIMERA COMUNION")

	c.setFont('Helvetica',13)
	c.drawString(50,620,"Por  las  presentes  letras   hago constar   que:     "+catequizando.nombre+"  ,")
	c.drawString(50,600,"bautizado  el   día   04/02/2014   en  la  parroquia,  después  de   haber  sido")
	c.drawString(50,580,"debidamente catequizada en la doctrina de Iniciación Cristiana, el sacramento de")
	c.drawString(50,560,"la  Sagrada  Comunión  en esta  Parroquia San  Bartolomé Apóstol de San  Bartolo,")
	c.drawString(50,540,"Ilopango  el día  cuatro de diciembre del año dos mil once.")

	c.drawString(50,480,"Y para los efectos que deseen y en derecho corresponda, extiende la presente")
	c.drawString(50,460,"certificación en DIA ACTUAL.")
	c.line(210,210,400,210)
	c.setFont('Helvetica',15)
	c.drawString(200,180,"Pbro. Vinicio Alejandro Orizabal")
	c.drawString(230,150,"Párroco de Somoto")
	c.save()
	pdf=buffer.getvalue()
	buffer.close()
	response.write(pdf)

	return response
