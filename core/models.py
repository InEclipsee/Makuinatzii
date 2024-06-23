from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class publicacion(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="postsImg")   
    TRABAJO_DROP = (
        ('1', 'Servicio 1'),
        ('2', 'Servicio 2'),
        ('3', 'Servicio 3'),
        ('4', 'Servicio 4'),)
    trabajo = models.CharField(max_length=20, choices=TRABAJO_DROP, default='1')
    idMecanico = models.ForeignKey(User, related_name="mecanicoActivo", on_delete=models.CASCADE, default=1, blank=True, null=True)
    fecha = models.DateField()
    
    
class servicio(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="serviciosImg")
    fechaSolicitado = models.DateField(null=True)