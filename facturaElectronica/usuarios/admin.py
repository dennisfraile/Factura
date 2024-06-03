from django.contrib import admin
from usuarios.models import CustomerUser, Entidad

# Register your models here.
admin.site.register(CustomerUser)
admin.site.register(Entidad)