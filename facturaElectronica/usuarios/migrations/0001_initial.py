# Generated by Django 5.0.1 on 2024-06-27 03:44

import django.db.models.deletion
import usuarios.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadEconomica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, verbose_name='Codigo')),
                ('valor', models.CharField(max_length=100, verbose_name='Valores')),
            ],
            options={
                'verbose_name_plural': 'Actividades Economicas',
            },
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razonSocial', models.CharField(max_length=100, verbose_name='Razon Social')),
                ('cellphone', models.CharField(help_text='Colocar el número sin identificador de país, sin espacios y sin guion.', max_length=30, verbose_name='Telefono movil del usuario')),
                ('codEstableMH', models.CharField(max_length=4, null=True, verbose_name='Codigo del establecimiento asignado por el MH')),
                ('codEstable', models.CharField(max_length=10, null=True, verbose_name='Codigo del establecimiento asignado por el contribuyente')),
                ('codPuntoVentaMH', models.CharField(max_length=4, null=True, verbose_name='Codigo del punto de venta (Emisor) asignado por el MH')),
                ('codPuntoVenta', models.CharField(max_length=15, null=True, verbose_name='Codigo del punto de venta (Emisor) asignado por el Contribuyente')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electronico de la entidad')),
                ('nit', models.CharField(max_length=30, unique=True, verbose_name='Numero de NIT sin guiones')),
                ('nrc', models.CharField(max_length=100, null=True, verbose_name='NRC')),
                ('actividadEconomica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.actividadeconomica')),
                ('direccionEmisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entidades', to='facturacion.direccion')),
            ],
            options={
                'verbose_name_plural': 'Entidades',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del usuario')),
                ('lastname', models.CharField(max_length=100, verbose_name='Apellido del usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electronico del usuario')),
                ('cellphone', models.CharField(help_text='Colocar el número sin identificador de país, sin espacios y sin guion.', max_length=20, verbose_name='Telefono movil del usuario')),
                ('organizacion', models.CharField(max_length=100, verbose_name='Organizaciones a las que esta asociado')),
                ('nrc', models.CharField(max_length=100, verbose_name='NRC')),
                ('is_entidad_superuser', models.BooleanField(default=False)),
                ('is_system_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates wheter the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('actividadEconomica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.actividadeconomica')),
                ('entidad', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='usuarios.entidad')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', usuarios.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ParametrosAuthHacienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userAgent', models.CharField(max_length=50, verbose_name='User Agent')),
                ('nit', models.CharField(max_length=50, verbose_name='NIT')),
                ('pwd', models.CharField(max_length=100, verbose_name='Password')),
                ('privateKey', models.TextField(verbose_name='Clave Privada de Hacienda')),
                ('publicKey', models.TextField(verbose_name='Clave Publica de Hacienda')),
                ('entidad', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='usuarios.entidad')),
            ],
            options={
                'verbose_name_plural': 'Parametros de Hacienda ',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('permisos', models.ManyToManyField(related_name='roles', to='usuarios.permiso')),
            ],
        ),
    ]
