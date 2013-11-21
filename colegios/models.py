from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Colegios(models.Model):
    id = models.IntegerField(primary_key=True)
    rbd = models.IntegerField()
    nombre = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    regione_id = models.IntegerField()
    dependencia = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    latitud = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    nroalumnos = models.IntegerField(blank=True, null=True)
    corporacion = models.CharField(max_length=255)
    web = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    user = models.ForeignKey(User)

    def __unicode__(self):
    	return self.nombre