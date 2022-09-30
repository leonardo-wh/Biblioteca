from django.conf.urls import url, include
from django.conf.urls.static import static

from aplicaciones.autor.views import AutorList, AutorCreate, AutorUpdate, AutorDelete, autor_edit, autor_view, autor_list, autor_delete


urlpatterns = [
   #url(r'^buscar/$', buscar, name='buscar'),
   url(r'^autor/$', AutorList.as_view(), name='autor_listar_class'),
   url(r'^autor/nuevo/$', AutorCreate.as_view(), name='autor_crear_class'),
   url(r'^libros/editar/(?P<pk>\d+)$', AutorUpdate.as_view(), name='autor_editar_class'),
   url(r'^libros/eliminar/(?P<pk>\d+)$', AutorDelete.as_view(), name='autor_eliminar_class'),


   url(r'^autordef/nuevo$', autor_view, name='autor_crear_def'),
   url(r'^autordef/listar$', autor_list, name='autor_listar_def'),
   url(r'^autordef/editar/(?P<pk>\d+)$', autor_edit, name='autor_editar_def'),
   url(r'^autordef/eliminar/(?P<pk>\d+)$', autor_delete, name='autor_eliminar_def'),
]
