# Generated by Django 5.0.1 on 2024-02-01 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='cellphone',
            field=models.CharField(help_text='Colocal el número sin identificador de país, sin espacios y sin guion.', max_length=20, verbose_name='Telefono movil del usuario'),
        ),
    ]
