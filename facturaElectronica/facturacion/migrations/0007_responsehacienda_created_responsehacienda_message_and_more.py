# Generated by Django 5.0.1 on 2024-07-01 21:50

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0006_alter_identificador_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsehacienda',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='responsehacienda',
            name='message',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='responsehacienda',
            name='status',
            field=models.CharField(max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apendice',
            name='comprobanteDonacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apendicesDonacion', to='facturacion.comprobantedonacion'),
        ),
        migrations.AlterField(
            model_name='apendice',
            name='sujetoExcluido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apendices', to='facturacion.sujetoexcluido'),
        ),
        migrations.AlterField(
            model_name='sujetoexcluido',
            name='fecha',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha'),
        ),
    ]
