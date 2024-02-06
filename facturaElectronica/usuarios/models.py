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

class CustomerUser(AbstractBaseUser, PermissionsMixin):
    dui = models.PositiveBigIntegerField("Numero de DUI sin guion", primary_key=True)
    name = models.CharField("Nombre del usuario", max_length=100)
    lastname = models.CharField("Apellido del usuario", max_length=100)
    email = models.EmailField("Correo electrnico del usuario", unique=True)
    cellphone = models.CharField("Telefono movil del usuario", 
                                              help_text="Colocal el número sin identificador de país, sin espacios y sin guion." , 
                                              max_length=20)
    direccion = models.CharField("Direccion fisica", max_length=100)
    organizacion = models.CharField("Organizaciones a las que esta asociado", max_length=100)

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
    REQUIRED_FIELDS = ["dui","name", "lastname"]

    class Meta:
        verbose_name_plural = "Usuarios"

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
    if created and not instance.is_staff:
        # Asigna una contraseña temporal al usuario
        temporary_password = generate_temporary_password()
        instance.set_password(temporary_password)
        instance.save()

        # Envía un correo electrónico con la contraseña temporal
        subject = 'Contraseña Temporal - ¡Bienvenido a Mi Aplicación!'
        message = f'Hola {instance.name},\n\nGracias por registrarte en Mi Aplicación. Tu contraseña temporal es: {temporary_password}'
        from_email = settings.EMAIL_HOST_USER  # Cambia esto al correo electrónico que desees
        to_email = [instance.email]
        send_mail(subject, message, from_email, to_email)

