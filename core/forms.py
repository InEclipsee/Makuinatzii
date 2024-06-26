from django import forms
from .models import Publicacion
import datetime

class FormPublicacion(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = '__all__'

        labels = {
            'titulo': 'Titulo de Publicacion',
            'descripcion' : 'Descripcion de Publicacion',
            'imagen' : 'Imagen' ,
            'trabajo' : 'Servicio Realizado' ,
            'mecanico' : 'Mecanico',
            'fecha' : 'Fecha',
        }

        widgets  ={
            'titulo' : forms.TextInput(attrs={'placeholder': 'eg. Titulo'}),
            'descripcion' : forms.Textarea(attrs={'placeholder': 'eg. Descripcion'}),
            'trabajo' : forms.Select(),
            'imagen' : forms.ClearableFileInput(),
            'mecanico' : forms.Select(),
            'fecha' : forms.DateInput(attrs={'class':'datepicker', 'value': datetime.date.today()}),
        }