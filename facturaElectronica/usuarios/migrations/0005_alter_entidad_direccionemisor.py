# Generated by Django 5.0.1 on 2024-06-30 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0003_alter_departamento_codigo_alter_municipio_codigo_and_more'),
        ('usuarios', '0004_alter_customuser_entidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='direccionEmisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entidades', to='facturacion.direccion'),
        ),
    ]
