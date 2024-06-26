from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Servicio(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=128, null=True, blank=True, default=1)
    imagen = models.ImageField(upload_to="core/static/img/serviciosImg")
    precio = models.IntegerField(default=999999)
    fechaSolicitado = models.DateField(null=True, blank=True)
    def __str__(self) -> str:
        return super().__str__()

class Publicacion(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=128, null=True, blank=True, default=1)
    imagen = models.ImageField(upload_to='core/static/img/postsImg')
    trabajo = models.ForeignKey(Servicio, related_name="servicioRealizado", on_delete=models.CASCADE, blank=True, null=True)
    idMecanico = models.ForeignKey(User, related_name="mecanicoActivo", on_delete=models.CASCADE, blank=True, null=True)
    ESTADO_DROP = (
        ('R', 'Rechazado'),
        ('P', 'Pendiente'),
        ('A', 'Aprobado'),)
    estado = models.CharField(max_length=10, choices=ESTADO_DROP, default='P')
    razonRechazo = models.CharField(max_length=256, null=True, blank=True, default=1)
    fecha = models.DateField()
    def __str__(self) -> str:
        return super().__str__()
    
    
    
