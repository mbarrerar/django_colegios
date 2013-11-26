from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
# Create your models here.

class ColegiosManager(models.Manager):
	def get_queryset(self):
		return super(ColegiosManager, self).get_queryset().select_related('user','regione')

class Regiones(TimeStampedModel):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return '[%s] %s' %(self.id,self.nombre)

    class Meta:
        ordering = ('id',)
	
class Colegios(TimeStampedModel):
    rbd = models.IntegerField()
    nombre = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    regione = models.ForeignKey(Regiones)
    dependencia = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    latitud = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    nroalumnos = models.IntegerField(blank=True, null=True)
    corporacion = models.CharField(max_length=255)
    web = models.CharField(max_length=255)
    user = models.ForeignKey(User,null=True)
    relacionados = ColegiosManager()

    def __unicode__(self):
    	return self.nombre


