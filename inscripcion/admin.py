from django.contrib import admin

# Register your models here.
from .models import *

class AdminCatequizando(admin.ModelAdmin):
	list_display=["id_catequizando","nombre","email","lugar_de_bautizo"]
	list_display_links=["nombre"]
	list_filter=["lugar_de_bautizo"]
	list_editable=["email"]
	search_fields=["nombre","email"]
	class Meta:
		model=Catequizando
		
class AdminCatequista(admin.ModelAdmin):
	list_display=["id_catequista","username","nombre","email","id_comunidad","id_area"]
	list_filter=["id_comunidad","id_area"]
	list_display_links=["username"]
	list_editable=["nombre"]
	search_fields=["usename","nombre"]
	class Meta:
		model=Catequista



admin.site.register(Catequizando, AdminCatequizando)
admin.site.register(Catequista)
admin.site.register(Comunidad)
admin.site.register(Area)
admin.site.register(Asistencia)
admin.site.register(Grupo)
admin.site.register(Boleta)
