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

class ActividadEconomica(models.Model):
     
     codigo = models.CharField(verbose_name="Codigo",max_length=10)
     valor = models.CharField(verbose_name="Valores",max_length=100)

     class Meta:
        verbose_name_plural = "Actividades Economicas"

     def __str__(self):
        return f'{self.codigo}'

class CustomerUser(AbstractBaseUser, PermissionsMixin):
    TIPO_USUARIO = (
         ("EMISOR","Usuario con acceso en el sistema"),
         ("RECEPTOR","Usuario sin acceso al sistema"),
    )
    type_user = models.CharField(verbose_name="Tipo de usuario", max_length=50, choices=TIPO_USUARIO)
    name = models.CharField(verbose_name="Nombre del usuario", max_length=100)
    lastname = models.CharField(verbose_name="Apellido del usuario", max_length=100)
    email = models.EmailField(verbose_name="Correo electrnico del usuario", unique=True)
    cellphone = models.CharField(verbose_name="Telefono movil del usuario", 
                                              help_text="Colocal el número sin identificador de país, sin espacios y sin guion." , 
                                              max_length=20)
    organizacion = models.CharField(verbose_name="Organizaciones a las que esta asociado", max_length=100)
    nrc = models.CharField(verbose_name="NRC", max_length=100)
    actividadEconomica = models.ForeignKey(ActividadEconomica, ondelete=models.CASCADE, editable=False)
    
    pass
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
    
    def save(self, *args, **kwargs):
         if self.type_user is "RECEPTOR":
              self.set_unusable_password()
         super().save(*args, **kwargs)

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

@receiver(post_save, sender=CustomerUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created and not instance.is_staff and not instance.type_user != "RECEPTOR":
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

class DocumentoIdentidad(models.Model):
    TIPOS_DOCUMENTO = (
        ("DUI", "Documento Unico de Identidad"),
        ("NIT","Numero de Identificacion Tributaria"),
    )
    HOMOLOGACION = (
        ("Documento Homologado", "DUI"),
        ("Documento No Homologado", "NIT"),
    )
    tipo = models.CharField(verbose_name="Tipo de Documento", max_length=25, choices=TIPOS_DOCUMENTO)
    homologado = models.CharField(verbose_name="Homologacion", max_length=30, choices=HOMOLOGACION)
    numero = models.CharField(verbose_name="Numero del documento sin guion")
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name="documentos")
     
    class Meta:
        verbose_name_plural = "Documentos de Identidad"

    def __str__(self):
        return f'{self.tipo}'

class Entidad(models.Model):
    
    razonSocial = models.CharField(verbose_name="Razon Social", max_length=100)
    documentoEntidad = models.ForeignKey(DocumentoIdentidad, on_delete=models.CASCADE, editable=False)
    
    class Meta:
        verbose_name_plural = "Entidades"

    def __str__(self):
        return f'{self.razonSocial}'

class ParametrosAuthHacienda(models.Model):
    
    userAgent = models.CharField(verbose_name="User Agent", max_length=50)
    nit = models.CharField(verbose_name="User", max_length=50)
    pwd = models.CharField(verbose_name="Password", max_length=100)
    privateKey = models.TextField(verbose_name="Clave Privada de Hacienda")
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False)
    
    class Meta:
        verbose_name_plural = "Parametros de Hacienda "

    def __str__(self):
        return f'{self.userAgent}'
    
    def set_password(self, raw_password):
        self.pwd = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.pwd)