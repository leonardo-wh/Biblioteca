from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Autor(models.Model):
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=40)
	email = models.EmailField(blank=True, verbose_name='e-mail')


	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellidos)


"""
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Autores"
		
"""