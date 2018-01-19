"""csb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from inscripcion import views
admin.autodiscover()

 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^inicio/$', views.inicio, name='inicio'),
    url(r'^cerrar/$', views.cerrar, name='cerrar'),



    url(r'^inscribir/$', views.boleta, name='inscribir'),
    url(r'^inhabilitar/(?P<id_cate>\d+)/$', views.inhabilitar, name='inhabilitar'),


    url(r'^roles/$', views.asignarRol, name='asignarRol'),
    url(r'^rolAdm/(?P<id_cate>\d+)/$', views.rolAdm, name='rolAdm'),
    url(r'^rolCoo/(?P<id_cate>\d+)/$', views.rolCoo, name='rolCoo'),
    url(r'^rolSec/(?P<id_cate>\d+)/$', views.rolSec, name='rolSec'),
    url(r'^rolCat/(?P<id_cate>\d+)/$', views.rolCat, name='rolCat'),

    url(r'^asignarAreaGrupo/$', views.asignarAreaGrupo, name='asignarAreaGrupo'),
    url(r'^asigareagrupo/(?P<id_cate>\d+)/$', views.asigareagrupo, name='asigareagrupo'),
    

    #COMUNIDAD#####
    url(r'^comunidadEditar/(?P<id_com>\d+)/$', views.comunidad_edit, name='comunidad_editar'),
    url(r'^comunidadDelete/(?P<id_com>\d+)/$', views.comunidad_eliminar, name='comunidad_delete'),
    url(r'^comunidad/$', views.comunidad, name='comunidad'),
    url(r'^listarComunidad/$', views.listarComunidad, name='listaComunidad'),
    


    url(r'^activarCatequista/$', views.ActivarCatequista, name='activarUser'),
    url(r'^activar/(?P<id_cat>\d+)/$', views.activar, name='activar'),
    url(r'^area/$', views.area, name='area'),
    url(r'^listaArea/$', views.listarArea, name='listaArea'),


    url(r'^areaEditar/(?P<id_ar>\d+)/$', views.area_editar, name='area_editar'),
    url(r'^areaDelete/(?P<id_ar>\d+)/$', views.area_eliminar, name='area_delete'),

    url(r'^crearCatequista/$',views.catequista_crear, name='catequistaCrear'),
    url(r'^listarCatequizando/$', views.ListCatequizando, name='listaCatequizando'),
    url(r'^catequizandoEditar/(?P<id_cat>\d+)/$', views.EditarCatequizando, name='EditarCatequizando'),

    
    url(r'^asis/$', views.asistencia, name='asis'),
    url(r'^listGrupoCat/$', views.list_gruposcate, name='listGrupoCat'),
    url(r'^asisGrupoCat/(?P<id_gru>\d+)/$', views.asis_porgrupo, name='listadoAsistencia'),
    # url(r'^listasiscate/(?P<id_gru>\d+)/$', views.listasiscate, name='listasiscate'),


    url(r'^catequistas/$', views.manejoCatequistas, name='catequistas'),

    #comentario: Next

    url(r'^inggrupo/',views.gruponew, name='inggrupo'),
    url(r'^listgrupo/',views.listgrupo, name='listgrupo'),
    url(r'^grupoEditar/(?P<id_gru>\d+)/$', views.grupo_edit, name='grupo_editar'),
    url(r'^grupoEliminar/(?P<id_gru>\d+)/$', views.grupo_eliminar, name='grupo_eliminar'),
    url(r'^menu/$', views.menu, name='menu'),


    #Menu->
    url(r'^gestioncate/$', views.gestioncate, name='gestioncate'),
    url(r'^gestionuser/$', views.gestionuser, name='gestionuser'),


    url(r'^buscarCate/$', views.buscarCate, name='buscarCate'),

    
    url(r'^ImprimirBol/(?P<id_cat>\d+)/$', views.ImprimirBol, name='imprimirbol'),
    # url(r'^accounts/', include('registration.backends.default.urls')),
]
 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)