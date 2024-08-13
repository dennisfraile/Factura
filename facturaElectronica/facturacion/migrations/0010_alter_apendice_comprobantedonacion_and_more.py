# Generated by Django 5.0.1 on 2024-07-08 21:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_remove_comprobantedonacion_identificador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apendice',
            name='comprobanteDonacion',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apendicesDonacion', to='facturacion.comprobantedonacion'),
        ),
        migrations.AlterField(
            model_name='apendice',
            name='sujetoExcluido',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apendices', to='facturacion.sujetoexcluido'),
        ),
    ]