# Generated by Django 5.0.6 on 2024-06-26 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='razonRechazo',
            field=models.CharField(blank=True, default='', max_length=256, null=True),
        ),
    ]
