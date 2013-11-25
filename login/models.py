from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
# Create your models here.

class Perfil(TimeStampedModel):
	user = models.OneToOneField(User)
	biografia = models.TextField()
	fecha_nacimiento = models.DateField()
	email = models.EmailField(max_length=100)
	telefono = models.IntegerField(max_length=10)

	def __unicode__(self):
		return self.biografia