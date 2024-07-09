# Generated by Django 5.0.6 on 2024-07-09 16:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(blank=True, max_length=128, null=True)),
                ('imagen', models.ImageField(upload_to='core/static/img/serviciosImg')),
                ('precio', models.IntegerField(default=999999)),
                ('fechaSolicitado', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(blank=True, max_length=128, null=True)),
                ('imagen', models.ImageField(upload_to='core/static/img/postsImg')),
                ('estado', models.CharField(choices=[('R', 'Rechazado'), ('P', 'Pendiente'), ('A', 'Aprobado')], default='P', max_length=10)),
                ('razonRechazo', models.CharField(blank=True, max_length=256, null=True)),
                ('fecha', models.DateField()),
                ('idMecanico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mecanicoActivo', to=settings.AUTH_USER_MODEL)),
                ('trabajo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servicioRealizado', to='core.servicio')),
            ],
        ),
    ]