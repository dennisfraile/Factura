# Generated by Django 5.0.1 on 2024-06-30 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0004_alter_direccion_entidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='sujetoexcluido',
            name='fecha',
            field=models.DateField(auto_now=True, verbose_name='Fecha'),
        ),
    ]