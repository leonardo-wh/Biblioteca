from __future__ import unicode_literals

from django.db import models
from aplicaciones.autor.models import Autor
from aplicaciones.editor.models import Editor
# Create your models here.

class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	autores = models.ManyToManyField(Autor, blank=True)
	editor = models.ForeignKey(Editor, null=True, blank=True)
	fecha_publicacion = models.DateField()
	portada = models.ImageField(upload_to='portadas', null=True, blank=True)

	def __str__(self):
		return self.titulo


