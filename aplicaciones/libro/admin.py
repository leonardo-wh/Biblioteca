from django.contrib import admin
from aplicaciones.libro.models import Libro

# Register your models here.


class LibroAdmin(admin.ModelAdmin):
	list_display = ('titulo','editor','fecha_publicacion')
	list_filter = ('fecha_publicacion',)
	date_hierarchy = 'fecha_publicacion'
	ordering = ('-fecha_publicacion',)
	#fields = ('titulo','autores','editor','fecha_publicacion')
	filter_horizontal = ('autores',)
	raw_id_fields = ('editor',)

admin.site.register(Libro, LibroAdmin)