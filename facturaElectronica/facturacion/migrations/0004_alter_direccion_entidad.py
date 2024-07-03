# Generated by Django 5.0.1 on 2024-07-01 01:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0003_alter_departamento_codigo_alter_municipio_codigo_and_more'),
        ('usuarios', '0007_alter_customuser_entidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direcciones', to='usuarios.entidad'),
        ),
    ]
