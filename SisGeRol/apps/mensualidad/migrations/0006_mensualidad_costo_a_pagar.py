# Generated by Django 4.2.7 on 2023-11-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensualidad', '0005_remove_mensualidad_costo_a_pagar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensualidad',
            name='costo_a_pagar',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
