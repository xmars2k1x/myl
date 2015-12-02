from django.db import models
from django.template import defaultfilters

class Carta(models.Model):
	nombre = models.CharField(max_length=32, blank=False)
	numero_de_coleccionista = models.CharField(max_length=16, blank=False)
	slug = models.SlugField(max_length=16, editable=False)

	def __str__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.numero_de_coleccionista)
		super(Carta, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return '/cartas/%s/' % (self.slug)
