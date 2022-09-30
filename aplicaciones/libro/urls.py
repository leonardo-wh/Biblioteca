from django.conf.urls import url, include
from aplicaciones.libro.views import index, LibroList, LibroCreate, LibroUpdate, LibroDelete, libro_edit, libro_view, libro_list, libro_delete, buscar

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   #url(r'^buscar/$', buscar, name='buscar'),
   url(r'^$', index, name='index'),
   url(r'^libro/$', LibroList.as_view(), name='libro_listar_class'),
   url(r'^libro/nuevo/$', LibroCreate.as_view(), name='libro_crear_class'),
   url(r'^libros/editar/(?P<pk>\d+)$', LibroUpdate.as_view(), name='libro_editar_class'),
   url(r'^libros/eliminar/(?P<pk>\d+)$', LibroDelete.as_view(), name='libro_eliminar_class'),

   url(r'^buscar/$', buscar, name='buscar'),

   url(r'^librodef/nuevo$', libro_view, name='libro_crear_def'),
   url(r'^librodef/listar$', libro_list, name='libro_listar_def'),
   url(r'^librodef/editar/(?P<pk>\d+)$', libro_edit, name='libro_editar_def'),
   url(r'^librodef/eliminar/(?P<pk>\d+)$', libro_delete, name='libro_eliminar_def'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
