from django.conf.urls import url, include
from django.conf.urls.static import static

from aplicaciones.editor.views import EditorList, EditorCreate, EditorUpdate, EditorDelete, editor_edit, editor_view, editor_list, editor_delete


urlpatterns = [
   #url(r'^buscar/$', buscar, name='buscar'),
   url(r'^editor/$', EditorList.as_view(), name='editor_listar_class'),
   url(r'^editor/nuevo/$', EditorCreate.as_view(), name='editor_crear_class'),
   url(r'^editor/editar/(?P<pk>\d+)$', EditorUpdate.as_view(), name='editor_editar_class'),
   url(r'^editor/eliminar/(?P<pk>\d+)$', EditorDelete.as_view(), name='editor_eliminar_class'),

   url(r'^editordef/nuevo$', editor_view, name='editor_crear_def'),
   url(r'^editordef/listar$', editor_list, name='editor_listar_def'),
   url(r'^editordef/editar/(?P<pk>\d+)$', editor_edit, name='editor_editar_def'),
   url(r'^editordef/eliminar/(?P<pk>\d+)$', editor_delete, name='editor_eliminar_def'),
]
