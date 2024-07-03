from django.contrib import admin
from usuarios.models import CustomUser, Entidad

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Entidad)