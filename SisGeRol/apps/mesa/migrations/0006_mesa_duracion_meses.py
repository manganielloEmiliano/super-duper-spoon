# Generated by Django 4.2.7 on 2023-11-11 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesa', '0005_mesa_costo_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='duracion_meses',
            field=models.PositiveIntegerField(default=3),
        ),
    ]
