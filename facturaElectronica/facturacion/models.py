from django.db import models
from usuarios.models import Entidad, ActividadEconomica, CustomUser, ParametrosAuthHacienda
from django.db.models import Max
import threading
import uuid
import re
from django.core.exceptions import ValidationError
import random
import string
from decimal import Decimal
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator, MaxValueValidator,MinValueValidator
# Create your models here.

class Pais(models.Model):
    
    codigo = models.CharField(verbose_name = "Codigo del pais", max_length=5)
    valor = models.CharField(verbose_name = "Nombre del pais", max_length=100, blank=False)

    class Meta:
        verbose_name_plural = "Paises"

    def __str__(self):
        return f'{self.valor}' 

class Departamento(models.Model):
    
    codigo = models.CharField(verbose_name = "Codigo del departamento", max_length=5, validators=[
            RegexValidator(
                regex='^0[1-9]|1[0-4]$',
                message='El código debe ser un número del 01 al 14.',
                code='invalid_code'
            )
        ])
    valor = models.CharField(verbose_name = "Nombre del departamento", max_length=100, blank=False)

    class Meta:
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return f'{self.valor}'

class Municipio(models.Model):
    
    codigo = models.CharField(verbose_name = "Codigo del municipio", max_length=5, validators=[
            RegexValidator(
                regex='^^[0-9]{2}$',
                message='El valor debe ser un número de exactamente dos dígitos.',
                code='invalid_code'
            )
        ])
    valor = models.CharField(verbose_name = "Nombre del municipio", max_length=100, blank=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name="departamentos")

    class Meta:
        verbose_name_plural = "Municipios"

    def __str__(self):
        return f'{self.valor}'
class Direccion(models.Model):

    complementoDireccion = models.CharField(verbose_name = "Direccion complemento",max_length=100, validators=[MinLengthValidator(1)])
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name="direcciones")

    class Meta:
        verbose_name_plural = "Direcciones"

    def __str__(self):
        return f'{self.complementoDireccion}'

class UnidadMedida(models.Model):
     
     codigo = models.CharField(verbose_name = "Codigo",max_length=3)
     valor = models.CharField(verbose_name = "Valor",max_length=50)
     class Meta:
        verbose_name_plural = "Unidades de medida"

     def __str__(self):
        return f'{self.valor}'


class FormaPago(models.Model):
    codigo = models.CharField(verbose_name="Codigo", max_length=2, validators=[
            RegexValidator(
                regex='^(0[1-9]|1[0-4]|99)$',
                message='El código debe ser 01-14 o 99.',
                code='invalid_codigo'
            )
        ])
    valor = models.CharField(verbose_name="Valores", max_length=50)

    class Meta:
        verbose_name_plural = "Formas de pago"

    def __str__(self):
        return f'{self.valor}'

def validate_exclusive_max(value):
    if value >= 100000000000:
        raise ValidationError('El valor debe ser menor que 100000000000.')

def validate_multiple_of2(value):
    if value % Decimal('0.01') != 0:
        raise ValidationError('El valor debe ser múltiplo de 0.01.')

class Pago(models.Model):

    PLAZO = (
        ("","Seleccione una opccion"),
        ("01", "Dias"),
        ("02", "Meses"),
        ("03", "Años")
    )
    formaPago = models.ForeignKey(FormaPago,  on_delete=models.CASCADE)
    montoPago = models.DecimalField(verbose_name="Monto por forma de pago", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of2,  # Debe ser múltiplo de 0.01
        ],
        help_text="Monto por forma de pago. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.01."
    )
    referencia = models.CharField(verbose_name="Referencia de la modalidad de pagos", max_length=50, null=True, blank=True)
    plazo = models.CharField(verbose_name="Plazo", max_length=20, choices=PLAZO, default="",null=True, blank=True)
    periodo = models.IntegerField(verbose_name="Periodo de plazo", null=True, blank=True)
    
    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False)
    class Meta:
        verbose_name_plural = "Pagos"

    def __str__(self):
        return f'{self.formaPago}{", "}{"Monto:"}{self.montoPago}'

class TipoDocumento(models.Model):

    codigo = models.CharField(verbose_name="Codigo",max_length=3)
    valor = models.CharField(verbose_name="Valor",max_length=50)

    class Meta:
        verbose_name_plural = "Tipos de Documentos"

    def __str__(self):
        return self.valor


class Receptor(models.Model):

    TIPOS_DOCUMENTO = (
        ("13","DUI"),
        ("36","NIT"),
        ("37","Otro"),
        ("03","Pasaporte"),
        ("02","Carnet de Residente"),
    )
    HOMOLOGACION = (
        ("DUI","Documento Homologado"),
        ("NIT","Documento No Homologado"),
    )
    tipo = models.CharField(verbose_name="Tipo de Documento", max_length=25, choices=TIPOS_DOCUMENTO)
    homologado = models.CharField(verbose_name="Homologacion", max_length=30, choices=HOMOLOGACION)
    numero = models.CharField(verbose_name="Numero del documento sin guion",max_length=20, validators=[MinLengthValidator(1)])
    nrc = models.CharField(verbose_name="NRC",max_length=20, null=True, blank=True, validators=[
            RegexValidator(
                regex='^[0-9]{1,8}$',
                message='El nrc debe tener entre 1 y 8 dígitos.',
                code='invalid_nrc'
            )
        ])
    nombre = models.CharField(verbose_name="Nombre, Denominacion o Razon Social del contribuyente", max_length=250, validators=[MinLengthValidator(1)])
    actividadEconomica = models.ForeignKey(ActividadEconomica, on_delete=models.SET_NULL, null=True, blank=True)
    direccionReceptor = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    cellphone = models.CharField(verbose_name="Telefono movil del usuario", 
                                              help_text="Colocar el número sin identificador de país, sin espacios y sin guion." , 
                                              max_length=30)
    email = models.EmailField(verbose_name="Correo electronico de el receptor", unique=True)
    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="receptores")
    class Meta:
        verbose_name_plural = "Receptores"

    def __str__(self):
        return f'{self.nombre}'

class SujetoExcluido(models.Model):
    
    CONDICION_OPERACION = (
        ("1", "Contado"),
        ("2", "A credito"),
        ("3", "Otro")
    )
    RETENCION_IVA_MH = (
        ("","Seleccione una opccion"),
        ("22", "Retencion IVA 1%"),
        ("C4", "Retencion IVA 13%"),
        ("C9", "Otras retenciones IVA casos especiales")
    )
    
    #Emisor
    emisor = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False)
    
    #Sujeto Excluido
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    
    #Resumen
    totalCompra = models.DecimalField(verbose_name="Total de operaciones", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of2,  # Debe ser múltiplo de 0.01
        ],
        help_text="Total de Operaciones. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.01")
    descu = models.DecimalField(verbose_name="Monto global de Descuento, Bonificacion, Rebajas", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of2,  # Debe ser múltiplo de 0.01
        ],
        help_text="Monto global de Descuento, Bonificacion, Rebajas")
    totalDescu = models.DecimalField(verbose_name="Total del monto de Descuento, Bonificacion, Rebajas", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of2,  # Debe ser múltiplo de 0.01
        ],
        help_text="Total del monto de Descuento, Bonificación, Rebajas.")
    subTotal = models.DecimalField(verbose_name="Subtotal", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),
            validate_exclusive_max,
            validate_multiple_of2,
        ],
        help_text="Sub-Total. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.01")
    retencionIVAMH = models.CharField(verbose_name="Retencion IVA MH", choices=RETENCION_IVA_MH, max_length=30, default="", null=True, blank=True)
    ivaRete1 = models.DecimalField(verbose_name="IVA Retenido", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),
            validate_exclusive_max,
            validate_multiple_of2,
        ],
        help_text="IVA Retenido. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.01")
    reteRenta = models.DecimalField(verbose_name= "Rentencion de Renta", max_digits=22, decimal_places=2,  validators=[
            MinValueValidator(0),
            validate_exclusive_max,
            validate_multiple_of2,
        ],
        help_text="Retención Renta. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.01")
    totalPagar = models.DecimalField(verbose_name="Total a Pagar", max_digits=22, decimal_places=2,  validators=[
            MinValueValidator(0),
            validate_exclusive_max,
            validate_multiple_of2,
        ],
        help_text="Total a Pagar. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.01")
    totalLetras = models.CharField(verbose_name="Total en letras", max_length=200)
    condicionOperacion = models.CharField(verbose_name="Condicion de la Operacion", choices=CONDICION_OPERACION, max_length=25)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE, null=True, blank=True)
    observaciones = models.TextField(verbose_name="Observaciones")
    fecha = models.DateField(verbose_name="Fecha", auto_now=True)
    fechaTransmicion = models.DateTimeField(verbose_name="Fecha de Transmicion",auto_now=True)
    #Si ya fue transmitido el sujeto excluido
    transmitido = models.BooleanField(default=False,editable=False)

    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="sujetosExcluidos")    
    class Meta:
        verbose_name_plural = "Sujetos Excluidos"

    def __str__(self):
        return f'{self.condicionOperacion}'
    
    def get_formatted_time(self):
        if self.fechaTransmicion:
            return self.fechaTransmicion.strftime('%H:%M:%S')
        return None
    
    def clean(self):
        super().clean()
        pattern = re.compile(r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$')
        formatted_time = self.get_formatted_time()
        if formatted_time and not pattern.match(formatted_time):
            try:
                # Intentar ajustar la hora al formato correcto
                self.fechaTransmicion = self.fechaTransmicion.replace(second=0, microsecond=0)
                formatted_time = self.get_formatted_time()

                if not pattern.match(formatted_time):
                    raise ValidationError(f'Failed to format time correctly. Time {formatted_time} does not match the required pattern.')
            except ValueError as e:
                raise ValidationError(f'Error formatting time: {e}')

def validate_exclusive_min(value):
    if value <= 0:
        raise ValidationError('El valor debe ser mayor que 0.')

def validate_multiple_of(value):
     if (value * Decimal('100000000')) % 1 != 0:
        raise ValidationError('El valor debe ser múltiplo de 0.00000001.')

class OperacionesSujetoExcluido(models.Model):
    
    TIPO_ITEM = (
        ("1", "Bienes"),
        ("2", "Servicios"),
        ("3", "Ambos (Bienes y servicios)"),
        ("4", "Otros tributos por item")
    )

    numItem = models.IntegerField(verbose_name = "N° item",validators=[
            MinValueValidator(1),  # Valor mínimo de 1
            MaxValueValidator(2000)  # Valor máximo de 2000
        ],
        help_text="N° ítem, debe estar entre 1 y 2000")
    tipoItem = models.CharField(verbose_name = "Tipo de item", choices=TIPO_ITEM, max_length=25)
    codigo = models.CharField(verbose_name = "Codigo", max_length=25, null=True, blank=True)
    uniMedida = models.ForeignKey(UnidadMedida,  on_delete=models.CASCADE)
    cantidad = models.DecimalField(verbose_name = "Cantidad",max_digits=22,
        decimal_places=2,
        validators=[
            validate_exclusive_min,
            validate_exclusive_max,
            validate_multiple_of,
        ],
        help_text="Cantidad debe ser mayor que 0, menor que 100000000000 y múltiplo de 0.00000001")
    montoDescu = models.DecimalField(verbose_name = "Monto", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],
        help_text="Descuento, Bonificación, Rebajas por ítem. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001")
    compra = models.DecimalField(verbose_name = "Ventas", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],
        help_text="Ventas. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001")
    retencion = models.DecimalField(verbose_name="Retencion", max_digits=12, decimal_places=2)
    descripccion = models.TextField(verbose_name="Descripccion", max_length=1000)
    precioUni = models.DecimalField(verbose_name="Precio Unitario", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],
        help_text="Precio Unitario debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001")
    
    sujetoExcluido = models.ForeignKey(SujetoExcluido, on_delete=models.CASCADE, editable=False, related_name="operacionesSujetoExcluido")
    
    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="operaciones")
    class Meta:
        verbose_name_plural = "Operaciones"

    def __str__(self):
        return f'{self.numItem}'

class PagoDonacion(models.Model):

    codigo = models.CharField(verbose_name="Codigo de Forma de pago", max_length=2, null=True,blank=True)
    montoPago = models.DecimalField(verbose_name="Monto por Forma de pago", max_digits=22, decimal_places=2,validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],)
    referencia = models.CharField(verbose_name="Referencia de la modalidad de pago", max_length=50, null=True, blank=True)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="pagos_donacion")

    class Meta:
        verbose_name_plural = "Pagos de donacion"

    def __str__(self):
        return f'{self.codigo}'

class ComprobanteDonacion(models.Model):
    DOMICILIO_FISCAL = (
        ("1", "Domiciliado"),
        ("2", "No Domiciliado"),
    )
    TIPO_ESTABLECIMIENTO = (
        ("01", "Sucursal/Agencia"),
        ("02", "Casa Matriz"),
        ("04", "Bodega"),
        ("07", "Predio y/o patio"),
        ("20", "Otro")
    )
    #Donatorio
    emisor = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False)
    tipoEstblacimiento = models.CharField(verbose_name="Tipo de Establecimiento",max_length=25, choices=TIPO_ESTABLECIMIENTO)
    
    #Donante
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    codDomiciliado = models.CharField(verbose_name="Domicilio Fiscal", choices=DOMICILIO_FISCAL, max_length=25)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    #Resumen
    valorTotal = models.DecimalField(verbose_name="Total de la donacion", max_digits=22, decimal_places=2,validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],)
    totalLetras = models.CharField(verbose_name="Total en letras", max_length=200)
    pago = models.ForeignKey(PagoDonacion, on_delete=models.CASCADE,null=True, blank=True)
    fecha = models.DateField(verbose_name="Fecha", auto_now=True)
    fechaTransmicion = models.DateTimeField(verbose_name="Fecha de Transmicion",auto_now=True)
    #Si ya fue transmitido el comprobante de donacion
    transmitido = models.BooleanField(default=False, editable=False)
    
    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="comprobantes")
    class Meta:
        verbose_name_plural = "Comprobantes de Donaciones"

    def __str__(self):
        return f'{self.valorTotal}'
    
    def get_formatted_time(self):
        if self.fechaTransmicion:
            return self.fechaTransmicion.strftime('%H:%M:%S')
        return None
    
    def clean(self):
        super().clean()
        pattern = re.compile(r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$')
        formatted_time = self.get_formatted_time()
        if formatted_time and not pattern.match(formatted_time):
            try:
                # Intentar ajustar la hora al formato correcto
                self.fechaTransmicion = self.fechaTransmicion.replace(second=0, microsecond=0)
                formatted_time = self.get_formatted_time()

                if not pattern.match(formatted_time):
                    raise ValidationError(f'Failed to format time correctly. Time {formatted_time} does not match the required pattern.')
            except ValueError as e:
                raise ValidationError(f'Error formatting time: {e}')

class OtroDocumentoAsociado(models.Model):
    OTRO_DOCUMENTO_ASOCIADO = (
        ("1", "Emisor"),
        ("2", "Receptor"),
        ("3", "Medico"),
        ("4", "Transporte")
    )
    codDocAsociado = models.CharField(verbose_name="Documento asociado", choices=OTRO_DOCUMENTO_ASOCIADO, max_length=25)
    descDocumento = models.CharField(verbose_name="Identificacion del documento asociado",max_length=100)
    detalleDocumento = models.CharField(verbose_name="Descripccion de documento asociado", max_length=300)

    comprobanteDonacion = models.ForeignKey(ComprobanteDonacion, on_delete=models.CASCADE, editable=False, related_name="otrosDocumentos")
    
    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="documentos")
    class Meta:
        verbose_name_plural = "Otros documentos asociados"

    def __str__(self):
        return f'{self.codDocAsociado}'

class CuerpoDocumento(models.Model):

    TIPO_DONACION = (
        ("1", "Efectivo"),
        ("2", "Bien"),
        ("3", "Servicio"),
    )
     
    numItem = models.IntegerField(verbose_name="N° item",validators=[
            MinValueValidator(1),  # Valor mínimo de 1
            MaxValueValidator(2000)  # Valor máximo de 2000
        ],
        help_text="N° ítem, debe estar entre 1 y 2000")
    tipoDonacion = models.CharField(verbose_name="Tipo de donacion",  max_length=20, choices=TIPO_DONACION)
    cantidad = models.DecimalField(verbose_name="Cantidad", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],)
    codigo = models.CharField(verbose_name="Codigo", max_length=25, null=True, blank=True)
    uniMedida = models.ForeignKey(UnidadMedida,  on_delete=models.CASCADE)
    descripccion = models.CharField(verbose_name="Descripccion", max_length=1000)
    depreciacion = models.DecimalField(verbose_name="Depreciacion", max_digits=22, decimal_places=2,validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],)
    valorUni = models.DecimalField(verbose_name="Valor Unitario", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],)
    valor = models.DecimalField(verbose_name="Valor Donado", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],)

    comprobanteDonacion = models.ForeignKey(ComprobanteDonacion, on_delete=models.CASCADE, editable=False, related_name="cuerpoDocumentos")

    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="cuerpos")
    class Meta:
        verbose_name_plural = "Cuerpos del documento"

    def __str__(self):
        return f'{self.numItem}'

class Tributo(models.Model):
    codigo = models.CharField(verbose_name="Codigo", max_length=2)
    valor = models.CharField(verbose_name="Valores", max_length=150)
    
    class Meta:
        verbose_name_plural ="Tributos del resumen"
    
    def __str__(self):
        return f'{self.valor}'

class TributoResumen(models.Model):
    tributo = models.ForeignKey(Tributo, on_delete=models.CASCADE ,related_name="tributos")
    valor =models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100000000000
        ],
        verbose_name="Valor del Tributo"
    )
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="tributos_resumen")
    class Meta:
        verbose_name_plural ="Tributos del resumen de Facturas Electronicas"
    
    def __str__(self):
        return f'{self.tributo.valor} {self.valor}'

class PagoFactura(models.Model):

    codigo = models.CharField(
        max_length=2,
        validators=[
            RegexValidator(
                regex=r'^(0[1-9]|1[0-4]|99)$',
                message="El código debe seguir el patrón: 01-09, 10-14, o 99."
            )
        ])
    montoPago = models.DecimalField(
        max_digits=14,       # Hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # Mínimo 0
            MaxValueValidator(100000000000 - 0.01)     # Máximo exclusivo 100,000,000,000
        ])
    referencia = models.CharField(
        max_length=50,
        null=True,           # Permite valores nulos
        blank=True,          # Opcional en formularios
        verbose_name="Referencia de modalidad de pago"
    )
    plazo = models.CharField(
        max_length=2,
        validators=[
            RegexValidator(
                regex=r'^0[1-3]$',
                message="El plazo debe seguir el patrón: 01-03."
            )
        ],
        null=True,           # Permite valores nulos
        blank=True,          # Opcional en formularios
        verbose_name="Plazo"
    )
    periodo = models.DecimalField(
        max_digits=10,       # Ajusta según el rango necesario
        decimal_places=2,    # Precisión de dos decimales (ajusta según necesidad)
        null=True,           # Permite valores nulos
        blank=True,          # Opcional en formularios
        verbose_name="Período de plazo"
    )
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="pagos")

    class Meta:
        verbose_name_plural = "Pagos de Facturas"

    def __str__(self):
        return f'{self.codigo}'

class FacturaElectronica(models.Model):
    CONDICION_OPERACION = (
        ("1", "Contado"),
        ("2", "A credito"),
        ("3", "Otro")
    )
    #tipo de factura
    es_factura_electronica = models.BooleanField(
        default=True,  # Por defecto, será una factura electrónica
        verbose_name="¿Es Factura Electrónica?"
    )
    #Emisor
    emisor = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False)
    
    #Receptor
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    
    #Resumen
    totalNoSuj = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100000000000
        ],
        verbose_name="Total de Operaciones no sujetas"
    )
    totalExenta = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100000000000
        ],
        verbose_name="Total de Operaciones exentas"
    )
    totalGravada = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100000000000
        ],
        verbose_name="Total de Operaciones Gravadas"
    )
    subTotalVentas = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100000000000
        ],
        verbose_name="Suma de operaciones sin impuestos"
    )
    descuNoSuj = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100000000000
        ],
        verbose_name="Monto global de Descuento, Bonificación, Rebajas y otros a ventas no sujetas"
    )
    descuExenta = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100000000000
        ],
        verbose_name="Monto global de Descuento, Bonificación, Rebajas y otros a ventas exentas"
    )
    descuGravada = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100000000000
        ],
        verbose_name="Monto global de Descuento, Bonificación, Rebajas y otros a ventas gravadas"
    )
    porcentajeDescuento = models.DecimalField(
        max_digits=5,       # Permite hasta 999.99, suficiente para valores de porcentaje con 2 decimales
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100)                     # El valor debe ser 100 o menor
        ],
        verbose_name="Porcentaje del monto global de Descuento, Bonificación, Rebajas y otros"
    )
    totalDescu = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100000000000
        ],
        verbose_name="Total del monto de Descuento, Bonificación, Rebajas"
    )
    tributo = models.ForeignKey(Tributo, on_delete=models.CASCADE, null=True, blank=True, verbose_name="facturas")
    subTotal = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100000000000
        ],
        verbose_name="Sub-Total"
    )
    ivaRete1 = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100,000,000,000
        ],
        verbose_name="IVA Retenido"
    )
    reteRenta = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100,000,000,000
        ],
        verbose_name="Retención Renta"
    )
    montoTotalOperacion = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100,000,000,000
        ],
        verbose_name="Monto Total de la Operación"
    )
    totalNoGravado = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(-100000000000 + 0.01),   # El valor debe ser mayor que -100,000,000,000
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100,000,000,000
        ],
        verbose_name="Total Cargos/Abonos que no afectan la base imponible"
    )
    totalPagar = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100,000,000,000
        ],
        verbose_name="Total a Pagar"
    )
    totalLetras = models.CharField(verbose_name="Valor en Letras",max_length=200)
    totalIva = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MinValueValidator(0),                      # El valor debe ser 0 o mayor
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100,000,000,000
        ],
        null=True,            # Permite valores nulos en la base de datos
        blank=True,           # Permite que el campo sea opcional en los formularios
        verbose_name="IVA 13%"
    ) #Solo para facturas electronicas
    saldoFavor = models.DecimalField(
        max_digits=14,       # Permite números hasta 999,999,999,999.99
        decimal_places=2,    # Precisión de dos decimales
        validators=[
            MaxValueValidator(0),                      # El valor debe ser menor o igual a 0
            MaxValueValidator(100000000000 - 0.01)     # El valor debe ser menor que 100,000,000,000
        ],
        verbose_name="Saldo a Favor"
    )
    condicionOperacion = models.CharField(verbose_name="Condicion de la Operacion", choices=CONDICION_OPERACION, max_length=25)
    pago = models.ForeignKey(PagoFactura, null=True, blank=True, on_delete=models.CASCADE)
    numPagoElectronico = models.CharField(
        max_length=100,     # Longitud máxima de 100 caracteres
        null=True,          # Permite valores nulos en la base de datos
        blank=True,         # Permite que el campo sea opcional en los formularios
        verbose_name="Número de pago Electrónico"
    )
    fecha = models.DateField(verbose_name="Fecha", auto_now=True)
    fechaTransmicion = models.DateTimeField(verbose_name="Fecha de Transmicion",auto_now=True)
    
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="factura")

    def es_credito_fiscal(self):
        return not self.es_factura_electronica
    
    def save(self, *args, **kwargs):
        # Validar que 'totalNoSuj' sea múltiplo de 0.01 antes de guardar
        if (self.totalNoSuj % 0.01) != 0:
            raise ValueError("El valor de 'totalNoSuj' debe ser un múltiplo de 0.01.")
        # Validar que 'totalExenta' sea múltiplo de 0.01 antes de guardar
        if (self.totalExenta % 0.01) != 0:
            raise ValueError("El valor de 'totalExenta' debe ser un múltiplo de 0.01.")
        # Validar que 'totalGravada' sea múltiplo de 0.01 antes de guardar
        if (self.totalGravada % 0.01) != 0:
            raise ValueError("El valor de 'totalGravada' debe ser un múltiplo de 0.01.")
        # Validar que 'subTotalVentas' sea múltiplo de 0.01 antes de guardar
        if (self.subTotalVentas % 0.01) != 0:
            raise ValueError("El valor de 'subTotalVentas' debe ser un múltiplo de 0.01.")
        # Validar que 'descuNoSuj' sea múltiplo de 0.01 antes de guardar
        if (self.descuNoSuj % 0.01) != 0:
            raise ValueError("El valor de 'descuNoSuj' debe ser un múltiplo de 0.01.")
        # Validar que 'descuExenta' sea múltiplo de 0.01 antes de guardar
        if (self.descuExenta % 0.01) != 0:
            raise ValueError("El valor de 'descuExenta' debe ser un múltiplo de 0.01.")
        # Validar que 'descuGravada' sea múltiplo de 0.01 antes de guardar
        if (self.descuGravada % 0.01) != 0:
            raise ValueError("El valor de 'descuGravada' debe ser un múltiplo de 0.01.")
        # Validar que 'porcentajeDescuento' sea múltiplo de 0.01 antes de guardar
        if (self.porcentajeDescuento % 0.01) != 0:
            raise ValueError("El valor de 'porcentajeDescuento' debe ser un múltiplo de 0.01.")
        # Validar que 'totalDescu' sea múltiplo de 0.01 antes de guardar
        if (self.totalDescu % 0.01) != 0:
            raise ValueError("El valor de 'totalDescu' debe ser un múltiplo de 0.01.")
        # Validar que 'subTotal' sea múltiplo de 0.01 antes de guardar
        if (self.subTotal % 0.01) != 0:
            raise ValueError("El valor de 'subTotal' debe ser un múltiplo de 0.01.")
        # Validar que 'ivaRete1' sea múltiplo de 0.01 antes de guardar
        if (self.ivaRete1 % 0.01) != 0:
            raise ValueError("El valor de 'ivaRete1' debe ser un múltiplo de 0.01.")
        # Validar que 'reteRenta' sea múltiplo de 0.01 antes de guardar
        if (self.reteRenta % 0.01) != 0:
            raise ValueError("El valor de 'reteRenta' debe ser un múltiplo de 0.01.")
         # Validar que 'montoTotalOperacion' sea múltiplo de 0.01 antes de guardar
        if (self.montoTotalOperacion % 0.01) != 0:
            raise ValueError("El valor de 'montoTotalOperacion' debe ser un múltiplo de 0.01.")
        # Validar que 'totalNoGravado' sea múltiplo de 0.01 antes de guardar
        if (self.totalNoGravado % 0.01) != 0:
            raise ValueError("El valor de 'totalNoGravado' debe ser un múltiplo de 0.01.")
         # Validar que 'totalPagar' sea múltiplo de 0.01 antes de guardar
        if (self.totalPagar % 0.01) != 0:
            raise ValueError("El valor de 'totalPagar' debe ser un múltiplo de 0.01.")
        if self.totalIva is not None:
            # Validar que 'totalIva' sea múltiplo de 0.01 antes de guardar
            if (self.totalIva % 0.01) != 0:
                raise ValueError("El valor de 'totalIva' debe ser un múltiplo de 0.01.")
        # Validar que 'saldoFavor' sea múltiplo de 0.01 antes de guardar
        if (self.saldoFavor % 0.01) != 0:
            raise ValueError("El valor de 'saldoFavor' debe ser un múltiplo de 0.01.")
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Facturas Electronicas"

class Extencion(models.Model):
    nombEntrega = models.CharField(
        max_length=100,     # Longitud máxima de 100 caracteres
        null=True,          # Permite valores nulos en la base de datos
        blank=True,         # Permite que el campo sea opcional en los formularios
        verbose_name="Nombre del responsable que Genera el DTE"
    )
    docuEntrega = models.CharField(
        max_length=25,      # Longitud máxima de 25 caracteres
        null=True,          # Permite valores nulos en la base de datos
        blank=True,         # Permite que el campo sea opcional en los formularios
        verbose_name="Documento de identificación de quien genera el DTE"
    )
    nombRecibe = models.CharField(
        max_length=100,     # Longitud máxima de 100 caracteres
        null=True,          # Permite valores nulos en la base de datos
        blank=True,         # Permite que el campo sea opcional en los formularios
        verbose_name="Nombre del responsable de la operación por parte del receptor"
    )
    docuRecibe = models.CharField(
        max_length=25,      # Longitud máxima de 25 caracteres
        null=True,          # Permite valores nulos en la base de datos
        blank=True,         # Permite que el campo sea opcional en los formularios
        verbose_name="Documento de identificación del responsable de la operación por parte del receptor"
    )
    observaciones = models.TextField(
        max_length=3000,    # Longitud máxima de 3000 caracteres
        null=True,          # Permite valores nulos en la base de datos
        blank=True,         # Permite que el campo sea opcional en los formularios
        verbose_name="Observaciones"
    )
    placaVehiculo = models.CharField(
        max_length=10,      # Longitud máxima de 10 caracteres
        null=True,          # Permite valores nulos en la base de datos
        blank=True,         # Permite que el campo sea opcional en los formularios
        verbose_name="Placa de vehículo"
    )
    facturaElectronica = models.ForeignKey(FacturaElectronica, on_delete=models.CASCADE, editable=False, related_name="facturaElectronica")
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="extencion")
    class Meta:
        verbose_name_plural = "Extenciones"

class DocumentoRelacionado(models.Model):
    TIPO_DOCUMENTO = (
        ("04","Nota de remision"),
        ("08","Comprobante de liquidacion"),
        ("09","Documento contable de liquidacion"),
    )
    TIPO_GENERACION = (
        ("1","Fisico"),
        ("2","Electronico")
    )
    tipoDocumento = models.CharField(verbose_name="Tipo de Documento", max_length=20, choices=TIPO_DOCUMENTO)
    tipoGeneracion = models.CharField(verbose_name="Tipo de Generacion", max_length=20, choices=TIPO_GENERACION)
    numeroDocumento = models.CharField(verbose_name="Numero de Documento Relacionados", max_length=36)
    fechaEmision = models.DateField(verbose_name="Fecha de Generacion del documento Relacionados")
    
    facturaElectronica = models.ForeignKey(FacturaElectronica, on_delete=models.CASCADE, editable=False, related_name="documentoRelacionado")
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="documentos_relacionados") 
    class Meta:
        verbose_name_plural = "Documentos Relacionados"

class Medico(models.Model):
    
    CODIGO_SERVICIO =(
        ("1","Cirujia"),
        ("2","Operacion"),
        ("3","Tratamiento medico"),
        ("4","Cirujia instituto salvadoreño de Binestar Magisterial"),
        ("5","Operacion Instituto Salvadoreño de Binestar Magisterial"),
        ("6","Tratamiento medico Instituto Salvadoreño de Binestar Magisterial"),
    )
    
    nombre = models.CharField(verbose_name="Nombre del medico que presta el servicio", max_length=100)
    nit = models.CharField(verbose_name="NIT del medico que presta el servicio", max_length=30, unique=True, validators=[
            RegexValidator(
                regex='^([0-9]{14}|[0-9]{9})$',
                message='El nit debe tener exactamente 14 o 9 dígitos.',
                code='invalid_nit'
            )
            ])
    docIdentificacion = models.CharField(verbose_name="Documento de identificacion de medico no domiciliados", max_length=25, null=True, blank=True)
    tipoServicio = models.CharField(verbose_name="Codigo del Sevicio Realizado", max_length=6, choices=CODIGO_SERVICIO)
    
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="medicos")
    class Meta:
        verbose_name_plural = "Medicos"

class OtroDocumento(models.Model):
    
    codDocAsociado = models.IntegerField(verbose_name="Documento Asociado", max_length=4)
    descDocumento = models.CharField(verbose_name="Identificacion del documento asociado", max_length=100, null=True, blank=True)
    detalleDocumento = models.CharField(verbose_name="Detalle de documento asociado", max_length=300, null=True, blank=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True, blank=True)
    
    facturaElectronica = models.ForeignKey(FacturaElectronica, on_delete=models.CASCADE, editable=False, related_name="otroDocumento")
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="otros_documentos")
    class Meta:
        verbose_name_plural = "Otros Documentos"

class VentaTercero(models.Model):
    
    nit = models.CharField(verbose_name="Numero de NIT sin guiones",max_length=30, unique=True, validators=[
            RegexValidator(
                regex='^([0-9]{14}|[0-9]{9})$',
                message='El nit debe tener exactamente 14 o 9 dígitos.',
                code='invalid_nit'
            )
        ])
    
    facturaElectronica = models.ForeignKey(FacturaElectronica, on_delete=models.CASCADE, editable=False, related_name="ventaTercero")
    nombre = models.CharField(verbose_name="Nombre, denominacion o razon social del Tercero",max_length=250)
    class Meta:
        verbose_name_plural = "Ventas a Terceros"

class Documento(models.Model):
    
    TIPO_ITEM = (
        ("1", "Bienes"),
        ("2", "Servicios"),
        ("3", "Ambos(Bienes y Servicios)"),
        ("4", "Otros Tributos por Item"),
    )
    COD_TRIBUTO = (
        (None, 'Ninguno'),  # Representación de `null`
        ('A8', 'Impuesto Especial al Combustible (0%, 0.5%, 1%)'),
        ('57', 'Impuesto Industria de Cemento'),
        ('90', 'Impuesto Especial a la Primera Matricula'),
        ('D4', 'Otros Impuestos Casos Especiales'),
        ('D5', 'Otras Tasas Casos Especiales'),
        ('A6', 'Impuesto AD-Valorem, Armas de Fuego, Municiones Explosivas y Articulos Similares'),
    )
    numItem = models.IntegerField(verbose_name="N° item",validators=[
            MinValueValidator(1),  # Valor mínimo de 1
            MaxValueValidator(2000)  # Valor máximo de 2000
        ],
        help_text="N° ítem, debe estar entre 1 y 2000")
    tipoItem = models.CharField(verbose_name="Tipo de Item",max_length=6, choices=TIPO_ITEM)
    numeroDocumento = models.CharField(verbose_name="Numero de Documento Relacionado",max_length=36, null=True, blank=True)
    cantidad = models.DecimalField(
        max_digits=20,       # Número máximo de dígitos en total (antes y después del punto decimal)
        decimal_places=2,    # Número de dígitos después del punto decimal (precisión)
        validators=[
            MinValueValidator(1e-08),  # Valor mínimo excluido
            MaxValueValidator(100000000000 - 1e-08)  # Valor máximo excluido
        ]
    )
    codigo = models.CharField(verbose_name="Codigo",max_length=25, null=True, blank=True)
    codTributo = models.CharField(
        max_length=2,                  # Limita el campo a un máximo de 2 caracteres
        choices=COD_TRIBUTO,   # Define las opciones permitidas
        blank=True,                    # Permite que sea nulo (equivalente a null en JSON)
        null=True,                     # Permite valores nulos
        verbose_name="Tributo sujeto a cálculo de IVA"  # Descripción del campo
    )
    uniMedida = models.ForeignKey(UnidadMedida,  on_delete=models.CASCADE)
    descripccion = models.CharField(verbose_name="Descripccion", max_length=1000)
    precioUni = models.DecimalField(verbose_name="Precio Unitario", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],
        help_text="Precio Unitario debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001")
    montoDescu = models.DecimalField(verbose_name = "Descuento, Bonificacion, Rebajas por Item", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],
        help_text="Descuento, Bonificación, Rebajas por ítem. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001")
    ventaNoSuj = models.DecimalField(verbose_name = "Ventas no Sujetas", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],
        help_text="Ventas no Sujetas. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001")
    ventaExenta = models.DecimalField(verbose_name = "Ventas Exentas", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],
        help_text="Ventas Exentas. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001")
    ventaGrabada = models.DecimalField(verbose_name = "Ventas Gravadas", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],
        help_text="Ventas Gravadas. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001")
    tributos = models.CharField(verbose_name="Codigo del Tributo", max_length=2, null=True, blank=True) #consultar sobre este item
    psv = models.DecimalField(verbose_name = "Precio Sujerido de Venta", max_digits=22, decimal_places=2, validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],
        help_text="Precio Sujerido de Venta. Debe ser mayor o igual a 0, menor que 100000000000 y múltiplo de 0.00000001")
    noGravado = models.DecimalField(
        max_digits=20,       # Número máximo de dígitos en total (incluyendo decimales)
        decimal_places=2,    # Número de dígitos después del punto decimal
        validators=[
            MinValueValidator(-100000000000 + 0.00000001),  # Valor mínimo excluido
            MaxValueValidator(100000000000 - 0.00000001)    # Valor máximo excluido
        ],
        verbose_name="Cargos/Abonos que no afectan la base imponible"
    )
    ivaItem = models.DecimalField(
        max_digits=20,       # Número máximo de dígitos en total (incluyendo decimales)
        decimal_places=2,    # Número de dígitos después del punto decimal
        validators=[
            MinValueValidator(0),  # Valor mínimo inclusivo de 0
            validate_exclusive_max,  # Valor máximo exclusivo de 100000000000
            validate_multiple_of,  # Debe ser múltiplo de 0.00000001
        ],
        verbose_name="IVA por Item"
    ) # Solo para Factura Electronica
    
    facturaElectronica = models.ForeignKey(FacturaElectronica, on_delete=models.CASCADE, editable=False, related_name="document")
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="documentoss")
    
    def save(self, *args, **kwargs):
        # Validar que la cantidad sea múltiplo de 1e-08 antes de guardar
        if (self.cantidad % 1e-08) != 0:
            raise ValueError("La cantidad debe ser un múltiplo de 1e-08.")
        # Validar que 'noGravado' sea múltiplo de 0.00000001 antes de guardar
        if (self.noGravado % 0.00000001) != 0:
            raise ValueError("El valor de 'noGravado' debe ser un múltiplo de 0.00000001.")
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Documentos"

def generateNumeroControl():
    part1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    part2 = ''.join(random.choices(string.digits, k=15))
    return f'DTE-14-{part1}-{part2}'


class Identificador(models.Model):
  
    AMBIENTE_DESTINO = (
        ("00","Modo Prueba"),
        ("01","Modo Produccion")
    )
    MODELO_FACTURACION = (
        ("1", "Modelo de Facturacion previo"),
        ("2", "Modelo de Facturacion diferido")
    )
    TIPO_TRANSMICION = (
        ("1", "Transmision normal"),
        ("2", "Transmision por contingencia")
    )
    TIPO_CONTINGENCIA = (
        ("","Seleccione opcion"),
        ("1", "No disponibilidad de sistema del MH"),
        ("2", "No disponibilidad de sistema del emisor"),
        ("3", "Falla en el suministro de servicio de Internet del Emisor"),
        ("4", "Falla en el suministro de servicio de energia electrica del emisor que impida la transmision de los DTE"),
        ("5", "Otro (debera digitar un maximo de 500 caracteres explicando el motivo)")
    )
    #Identificacion
    version = models.CharField(verbose_name="Version", max_length=10)
    ambiente = models.CharField(verbose_name="Ambiente de destino", max_length=20, choices=AMBIENTE_DESTINO)
    tipoDte = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numeroControl = models.CharField(verbose_name="Numero de control", editable=False , max_length=31, default=generateNumeroControl)
    codigoGeneracion = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    tipoModelo = models.CharField(verbose_name="Modelo de facturacion", choices=MODELO_FACTURACION, max_length=50)
    tipoOperacion = models.CharField(verbose_name="Tipo de Transmicion", choices=TIPO_TRANSMICION, max_length=50, default="1")
    tipoContingencia = models.CharField(verbose_name="Tipo de Contingencia", choices=TIPO_CONTINGENCIA, max_length=50, blank=True, null=True,default="")
    motivoContin = models.CharField(verbose_name="Motivo de Contingencia", max_length=500, blank=True, null=True)
    tipoMoneda = models.CharField(verbose_name="Tipo de Moneda",default="USD",  # Valor por defecto
        help_text="Tipo de Moneda", max_length=30) 
    
    #Sujeto Excluido
    sujetoExcluido = models.ForeignKey(SujetoExcluido, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    
    #Comprobante de Donacion
    comprobanteDonacion = models.ForeignKey(ComprobanteDonacion, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    
    #Factura Electronica 
    facturaElectronica = models.ForeignKey(FacturaElectronica, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    
    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False) 
    
    class Meta:
        verbose_name_plural = "Identificaciones"

    def __str__(self):
        return f'{self.version}'

    
class Apendice(models.Model):

    campo = models.CharField(verbose_name="Nombre del campo", max_length=25)
    etiqueta = models.TextField(verbose_name="Descripccion", max_length=50)
    valor = models.CharField(verbose_name="Valor/Dato", max_length=150)
    
    #Facturas Asociadas
    sujetoExcluido = models.ForeignKey(SujetoExcluido, null=True, blank=True, editable=False,  on_delete=models.CASCADE, related_name="apendices")
    comprobanteDonacion = models.ForeignKey(ComprobanteDonacion, null=True, blank=True, editable=False,  on_delete=models.CASCADE, related_name="apendicesDonacion")
    facturaElectronica = models.ForeignKey(FacturaElectronica, on_delete=models.CASCADE, editable=False, null=True, blank=True, related_name="apendiceFacturaElectronica")
    
    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False)
    class Meta:
        verbose_name_plural = "Apendices"

    def __str__(self):
        return f'{self.campo}'

class ResponseHacienda(models.Model):
    
    nombre = models.CharField(max_length=100)
    datosJson = models.JSONField()
    status = models.CharField(max_length=30)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    sujetoExcluido = models.ForeignKey(SujetoExcluido, on_delete=models.CASCADE, editable=False, null=True, blank=True, related_name="sujetoExcluidoResponse")
    comprobanteDonacion = models.ForeignKey(PagoDonacion, on_delete=models.CASCADE, editable=False, null=True, blank=True, related_name="comprobanteDonacionResponse")
    facturaElectronica = models.ForeignKey(FacturaElectronica, on_delete=models.CASCADE, editable=False, null=True, blank=True, related_name="facturaElectronicaResponse")
    class Meta:
        verbose_name_plural = "Responses"
    
    def __str__(self):
        return f'{self.nombre}'