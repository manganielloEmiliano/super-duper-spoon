# Generated by Django 4.2.5 on 2023-09-12 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesa', '0003_remove_mesa_rol_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='costo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='mesa',
            name='regularidad',
            field=models.CharField(choices=[('semanal', 'Semanal'), ('quincenal', 'Quincenal')], default='semanal', max_length=50),
        ),
    ]
