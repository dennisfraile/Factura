# Generated by Django 5.0.1 on 2024-07-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0007_responsehacienda_created_responsehacienda_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receptor',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Correo electronico de el receptor'),
        ),
    ]
