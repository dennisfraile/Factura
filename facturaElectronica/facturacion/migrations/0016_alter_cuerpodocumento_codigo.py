# Generated by Django 5.0.1 on 2024-08-27 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0015_alter_cuerpodocumento_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuerpodocumento',
            name='codigo',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Codigo'),
        ),
    ]
