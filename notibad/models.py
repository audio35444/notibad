from django.db import models
from django.utils import timezone


class Noticia(models.Model):
	#Atributos
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	tipo = models.IntegerField()
	create_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
	def getCreateDate(self):
		return self.create_date

