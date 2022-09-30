from django.contrib import admin
from aplicaciones.autor.models import Autor

# Register your models here.

class AutorAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellidos','email')
	search_fields = ('nombre','apellidos')


admin.site.register(Autor,AutorAdmin)
