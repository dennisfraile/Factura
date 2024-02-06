from django.db import models

# Create your models here.
class Proveedor(models.Model):

    razon_social = models.CharField("Nombre",max_length=100),
    nit = models.PositiveBigIntegerField("Numero de NIT sin guion", unique=True, blank=False)
    dui = models.PositiveBigIntegerField("Numero de DUI sin guion", unique=True, blank=False)
    direccion = models.CharField("Direccion fisica",max_length=100)
    email = models.EmailField("Correo electronico", unique=True)
    municipio = models.PositiveSmallIntegerField("Municipio")
    departamento = models.PositiveSmallIntegerField("Departamento")

    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return f'{self.razon_social}'
    
class Organizacion(models.Model):

    razon_social = models.CharField("Nombre de la organizacion",max_length=100)
    direccion = models.CharField("Direccion fisica",max_length=100)
    nit = models.PositiveBigIntegerField("Numero de NIT sin guion", unique=True, blank=False)

    class Meta:
        verbose_name_plural = "Organizaciones"

    def __str__(self):
        return f'{self.razon_social}'

class Departamento(models.Model):
    
    codigo = models.PositiveIntegerField("Codigo del departamento", unique=True, blank=False)
    valor = models.CharField("Nombre del departamento", max_length=100, blank=False)

    class Meta:
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return f'{self.valor}'

class Municipio(models.Model):
    
    codigo = models.PositiveIntegerField("Codigo del municipio", unique=True, blank=False)
    valor = models.CharField("Nombre del municipio", max_length=100, blank=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, editable=False)

    class Meta:
        verbose_name_plural = "Municipios"

    def __str__(self):
        return f'{self.valor}'