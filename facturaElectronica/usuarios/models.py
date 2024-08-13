from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,User
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy
from .managers import UserManager
import random
import string
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator


class ActividadEconomica(models.Model):
     
     codigo = models.CharField(verbose_name="Codigo",max_length=10, validators=[
            RegexValidator(
                regex='^[0-9]{2,6}$',
                message='El el codigo debe tener entre 1 y 6 dígitos.',
                code='invalid_codigo'
            )
        ])
     valor = models.CharField(verbose_name="Valores",max_length=150)

     class Meta:
        verbose_name_plural = "Actividades Economicas"

     def __str__(self):
        return f'{self.valor}'

class Entidad(models.Model):
    
    razonSocial = models.CharField(verbose_name="Razon Social", max_length=100)
    direccionEmisor = models.ForeignKey('facturacion.Direccion', on_delete=models.CASCADE, related_name='entidades', null=True, blank=True)
    cellphone = models.CharField(verbose_name="Telefono movil del usuario", 
                                              help_text="Colocar el número sin identificador de país, sin espacios y sin guion." , 
                                              max_length=30)
    codEstableMH = models.CharField(verbose_name="Codigo del establecimiento asignado por el MH", max_length=4, blank=True, null=True, validators=[MinLengthValidator(4)])
    codEstable = models.CharField(verbose_name="Codigo del establecimiento asignado por el contribuyente", max_length=10, blank=True, null=True, validators=[MinLengthValidator(1)])
    codPuntoVentaMH = models.CharField(verbose_name="Codigo del punto de venta (Emisor) asignado por el MH", max_length=4, blank=True, null=True, validators=[MinLengthValidator(4)])
    codPuntoVenta = models.CharField(verbose_name="Codigo del punto de venta (Emisor) asignado por el Contribuyente", max_length=15, blank=True, null=True, validators=[MinLengthValidator(1)])
    email = models.EmailField(verbose_name="Correo electronico de la entidad", unique=True)
    nit = models.CharField(verbose_name="Numero de NIT sin guiones",max_length=30, unique=True, validators=[
            RegexValidator(
                regex='^([0-9]{14}|[0-9]{9})$',
                message='El nit debe tener exactamente 14 o 9 dígitos.',
                code='invalid_nit'
            )
        ])
    nrc = models.CharField(verbose_name="NRC", max_length=100, null=True, blank=True, validators=[
            RegexValidator(
                regex='^[0-9]{1,8}$',
                message='El nrc debe tener entre 1 y 8 dígitos.',
                code='invalid_nrc'
            )
        ])
    actividadEconomica = models.ForeignKey(ActividadEconomica, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = "Entidades"

    def __str__(self):
        return f'{self.razonSocial}'

class Permiso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    permisos = models.ManyToManyField(Permiso, related_name='roles')

    def __str__(self):
        return self.nombre

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(verbose_name="Nombre del usuario", max_length=100)
    lastname = models.CharField(verbose_name="Apellido del usuario", max_length=100)
    email = models.EmailField(verbose_name="Correo electronico del usuario", unique=True)
    cellphone = models.CharField(verbose_name="Telefono movil del usuario", 
                                              help_text="Colocar el número sin identificador de país, sin espacios y sin guion." , 
                                              max_length=20)
    organizacion = models.CharField(verbose_name="Organizaciones a las que esta asociado", max_length=100)
    nrc = models.CharField(verbose_name="NRC", max_length=100, validators=[
            RegexValidator(
                regex='^[0-9]{1,8}$',
                message='El nrc debe tener entre 1 y 8 dígitos.',
                code='invalid_nrc'
            )
        ])
    actividadEconomica = models.ForeignKey(ActividadEconomica, on_delete=models.CASCADE, null=True, blank=True)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE,null=True, related_name="usuarios")
    is_entidad_superuser = models.BooleanField(default=False)
    is_system_superuser = models.BooleanField(default=False)
    
    
    date_joined = models.DateTimeField(gettext_lazy("date joined"),auto_now_add=True)
    is_staff = models.BooleanField(
        gettext_lazy("staff status"),
        default=False,
        help_text=gettext_lazy(
            "Designates wheter the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(gettext_lazy("active"), default=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "lastname"]

    class Meta:
        verbose_name_plural = "Usuarios"
    
    def has_permission(self, permission_name):
        if self.is_system_superuser:
            return True
        return any(group.permissions.filter(codename=permission_name).exists() for group in self.groups.all())

    @property
    def full_name(self):
        """
        Returns the full name.
        """
        full_name = f"{self.name} {self.lastname}"
        return full_name.strip()

    def get_short_name(self):
        """
        Returns a short name for the user.
        """
        return self.name

    def __str__(self):
        return f'{self.full_name}'

def generate_temporary_password():
        # Genera una contraseña temporal aleatoria
        length = 8
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for i in range(length))
        return password

@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        # Asigna una contraseña temporal al usuario
        temporary_password = generate_temporary_password()
        instance.set_password(temporary_password)
        instance.save()

        # Envía un correo electrónico con la contraseña temporal
        subject = 'Contraseña Temporal - ¡Bienvenido al Sitema de Facturacion Electronica!'
        message = f'Hola {instance.name},\n\nGracias por registrarte en el Sistema de Facturacion Electronica. Tu contraseña temporal es: {temporary_password}'
        from_email = settings.EMAIL_HOST_USER  # Cambia esto al correo electrónico que desees
        to_email = [instance.email]
        send_mail(subject, message, from_email, to_email)

class ParametrosAuthHacienda(models.Model):
    
    userAgent = models.CharField(verbose_name="User Agent", max_length=50)
    nit = models.CharField(verbose_name="NIT", max_length=100, validators=[
            RegexValidator(
                regex='^([0-9]{14}|[0-9]{9})$',
                message='El nit debe tener exactamente 14 o 9 dígitos.',
                code='invalid_nit'
            )
        ])
    pwd = models.CharField(verbose_name="Password", max_length=100)
    privateKey = models.TextField(verbose_name="Clave Privada de Hacienda")
    publicKey = models.TextField(verbose_name="Clave Publica de Hacienda")
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False)
    
    class Meta:
        verbose_name_plural = "Parametros de Hacienda "

    def __str__(self):
        return f'{self.userAgent}'
    
    def set_password(self, raw_password):
        self.pwd = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.pwd)