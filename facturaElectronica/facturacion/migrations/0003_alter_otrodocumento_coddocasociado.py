# Generated by Django 5.0.1 on 2024-12-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otrodocumento',
            name='codDocAsociado',
            field=models.IntegerField(verbose_name='Documento Asociado'),
        ),
    ]
