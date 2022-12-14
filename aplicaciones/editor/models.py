from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Editor(models.Model):
	nombre = models.CharField(max_length=30)
	domicilio = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=60)
	estado = models.CharField(max_length=30)
	pais = models.CharField(max_length=50)
	website = models.URLField(max_length=200)


	def __str__(self):
		return '{}'.format(self.nombre)

"""
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Editores"


"""
	