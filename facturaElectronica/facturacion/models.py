from django.db import models
from usuarios.models import Entidad, ActividadEconomica, CustomUser, ParametrosAuthHacienda
from django.db.models import Max
import threading
import uuid
import re
from django.core.exceptions import ValidationError
import random
import string
from django.utils import timezone
# Create your models here.

class Pais(models.Model):
    
    codigo = models.CharField(verbose_name = "Codigo del pais", max_length=5)
    valor = models.CharField(verbose_name = "Nombre del pais", max_length=100, blank=False)

    class Meta:
        verbose_name_plural = "Paises"

    def __str__(self):
        return f'{self.valor}' 

class Departamento(models.Model):
    
    codigo = models.CharField(verbose_name = "Codigo del departamento", max_length=5)
    valor = models.CharField(verbose_name = "Nombre del departamento", max_length=100, blank=False)

    class Meta:
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return f'{self.valor}'

class Municipio(models.Model):
    
    codigo = models.CharField(verbose_name = "Codigo del municipio", max_length=5)
    valor = models.CharField(verbose_name = "Nombre del municipio", max_length=100, blank=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name="departamentos")

    class Meta:
        verbose_name_plural = "Municipios"

    def __str__(self):
        return f'{self.valor}'
class Direccion(models.Model):

    complementoDireccion = models.CharField(verbose_name = "Direccion complemento",max_length=100)
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
        return f'{self.codigo}'


class FormaPago(models.Model):
    codigo = models.CharField(verbose_name="Codigo", max_length=3)
    valor = models.CharField(verbose_name="Valores", max_length=50)

    class Meta:
        verbose_name_plural = "Formas de pago"

    def __str__(self):
        return f'{self.codigo}'

class Pago(models.Model):

    PLAZO = (
        ("01", "Dias"),
        ("02", "Meses"),
        ("03", "Años")
    )
    codigo = models.CharField(verbose_name= "Codigo",max_length=4)
    formaPago = models.ForeignKey(FormaPago,  on_delete=models.CASCADE)
    montoPago = models.DecimalField(verbose_name="Monto por forma de pago", max_digits=12, decimal_places=2)
    referencia = models.CharField(verbose_name="Referencia de la modalidad de pagos", max_length=50)
    plazo = models.CharField(verbose_name="Plazo", max_length=20, choices=PLAZO)
    periodo = models.IntegerField(verbose_name="Periodo de plazo")
    
    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False)
    class Meta:
        verbose_name_plural = "Pagos"

    def __str__(self):
        return f'{self.codigo}'

class TipoDocumento(models.Model):

    codigo = models.CharField(verbose_name="Codigo",max_length=3)
    valores = models.CharField(verbose_name="Valores",max_length=50)

    class Meta:
        verbose_name_plural = "Tipos de Documentos"

    def __str__(self):
        return f'{self.codigo}'

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
    tipoOperacion = models.CharField(verbose_name="Tipo de Transmicion", choices=TIPO_TRANSMICION, max_length=50)
    tipoContingencia = models.CharField(verbose_name="Tipo de Contingencia", choices=TIPO_CONTINGENCIA, max_length=50)
    motivoContin = models.CharField(verbose_name="Motivo de Contingencia", max_length=500)
    tipoMoneda = models.CharField(verbose_name="Tipo de Moneda", max_length=30) 
    
    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False) 
    
    class Meta:
        verbose_name_plural = "Identificaciones"

    def __str__(self):
        return f'{self.version}'

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
    numero = models.CharField(verbose_name="Numero del documento sin guion",max_length=20)
    nrc = models.CharField(verbose_name="NRC",max_length=20, null=True)
    nombre = models.CharField(verbose_name="Nombre, Denominacion o Razon Social del contribuyente", max_length=250)
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
        ("22", "Retencion IVA 1%"),
        ("C4", "Retencion IVA 13%"),
        ("C9", "Otras retenciones IVA casos especiales")
    )
   
    #Identificador
    identificador = models.ForeignKey(Identificador, on_delete=models.CASCADE)
    
    #Emisor
    emisor = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False)
    
    #Sujeto Excluido
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    
    #Resumen
    totalCompra = models.DecimalField(verbose_name="Total de operaciones", max_digits=12, decimal_places=2)
    descu = models.DecimalField(verbose_name="Monto global de Descuento, Bonificacion, Rebajas", max_digits=12, decimal_places=2)
    totalDescu = models.DecimalField(verbose_name="Total del monto de Descuento, Bonificacion, Rebajas", max_digits=12, decimal_places=2)
    subTotal = models.DecimalField(verbose_name="Subtotal", max_digits=12, decimal_places=2)
    retencionIVAMH = models.CharField(verbose_name="Retencion IVA MH", choices=RETENCION_IVA_MH, max_length=30)
    ivaRete1 = models.DecimalField(verbose_name="IVA Retenido", max_digits=12, decimal_places=2)
    reteRenta = models.DecimalField(verbose_name= "Rentencion de Renta", max_digits=12, decimal_places=2)
    totalPagar = models.DecimalField(verbose_name="Total a Pagar", max_digits=12, decimal_places=2)
    totalLetras = models.CharField(verbose_name="Total en letras", max_length=200)
    condicionOperacion = models.CharField(verbose_name="Condicion de la Operacion", choices=CONDICION_OPERACION, max_length=25)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    observaciones = models.TextField(verbose_name="Observaciones")
    fecha = models.DateField(verbose_name="Fecha", auto_now_add=True)
    fechaTransmicion = models.DateTimeField(verbose_name="Fecha de Transmicion",auto_now_add=True)
    #Si ya fue transmitido el sujeto excluido
    transmitido = models.BooleanField(default=False,editable=False)

    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="sujetosExcluidos")    
    class Meta:
        verbose_name_plural = "Sujetos Excluidos"

    def __str__(self):
        return f'{self.identificador}'
    
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

class OperacionesSujetoExcluido(models.Model):
    
    TIPO_ITEM = (
        ("1", "Bienes"),
        ("2", "Servicios"),
        ("3", "Ambos (Bienes y servicios)"),
        ("4", "Otros tributos por item")
    )

    numItem = models.IntegerField(verbose_name = "N° item")
    tipoItem = models.CharField(verbose_name = "Tipo de item", choices=TIPO_ITEM, max_length=25)
    codigo = models.CharField(verbose_name = "Codigo", max_length=25, null=True)
    uniMedida = models.ForeignKey(UnidadMedida,  on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name = "Cantidad")
    montoDescu = models.DecimalField(verbose_name = "Monto", max_digits=12, decimal_places=2)
    compra = models.DecimalField(verbose_name = "Ventas", max_digits=12, decimal_places=2)
    retencion = models.DecimalField(verbose_name="Retencion", max_digits=12, decimal_places=2)
    descripccion = models.TextField(verbose_name="Descripccion", max_length=1000)
    precioUni = models.DecimalField(verbose_name="Precio Unitario", max_digits=12, decimal_places=2)
    
    sujetoExcluido = models.ForeignKey(SujetoExcluido, on_delete=models.CASCADE, editable=False, related_name="operacionesSujetoExcluido")
    
    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="operaciones")
    class Meta:
        verbose_name_plural = "Operaciones"

    def __str__(self):
        return f'{self.codigo}'

class PagoDonacion(models.Model):

    codigo = models.CharField(verbose_name="Codigo de Forma de pago", max_length=2)
    montoPago = models.DecimalField(verbose_name="Monto por Forma de pago", max_digits=12, decimal_places=2)
    referencia = models.CharField(verbose_name="Referencia de la modalidad de pago", max_length=50)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="pagos")

    class Meta:
        verbose_name_plural = "Pagos de donacion"

    def __str__(self):
        return f'{self.codigo}'

class ComprobanteDonacion(models.Model):
    DOMICILIO_FISCAL = (
        ("1", "Domiciliado"),
        ("2", "No Domiciliado"),
    )
    #Identificador
    identificador = models.ForeignKey(Identificador, on_delete=models.CASCADE) 

    #Donatorio
    emisor = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    
    #Donante
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    codDomiciliado = models.CharField(verbose_name="Domicilio Fiscal", choices=DOMICILIO_FISCAL, max_length=25)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    #Resumen
    valorTotal = models.DecimalField(verbose_name="Total de la donacion", max_digits=12, decimal_places=2)
    totalLetras = models.CharField(verbose_name="Total en letras", max_length=200)
    pago = models.ForeignKey(PagoDonacion, on_delete=models.CASCADE)
    fechaTransmicion = models.DateTimeField(verbose_name="Fecha de Transmicion",auto_now_add=True)
    #Si ya fue transmitido el comprobante de donacion
    transmitido = models.BooleanField(default=False, editable=False)
    
    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="comprobantes")
    class Meta:
        verbose_name_plural = "Comprobantes de Donaciones"

    def __str__(self):
        return f'{self.identificador}'

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
     
    numItem = models.IntegerField(verbose_name="N° item")
    tipoDonacion = models.CharField(verbose_name="Tipo de donacion",  max_length=20, choices=TIPO_DONACION)
    cantidad = models.IntegerField(verbose_name="Cantidad")
    codigo = models.CharField(verbose_name="Codigo", max_length=25)
    uniMedida = models.ForeignKey(UnidadMedida,  on_delete=models.CASCADE)
    descripccion = models.CharField(verbose_name="Descripccion", max_length=1000)
    depreciacion = models.IntegerField(verbose_name="Depreciacion")
    montoDescu = models.DecimalField(verbose_name="Monto", max_digits=12, decimal_places=2)
    valorUni = models.DecimalField(verbose_name="Valor Unitario", max_digits=12, decimal_places=2)
    valor = models.DecimalField(verbose_name="Valor Donado", max_digits=12, decimal_places=2)

    comprobanteDonacion = models.ForeignKey(ComprobanteDonacion, on_delete=models.CASCADE, editable=False, related_name="cuerpoDocumentos")

    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, related_name="cuerpos")
    class Meta:
        verbose_name_plural = "Cuerpos del documento"

    def __str__(self):
        return f'{self.numItem}'
    
class Apendice(models.Model):

    campo = models.CharField(verbose_name="Nombre del campo", max_length=25)
    etiqueta = models.TextField(verbose_name="Descripccion", max_length=50)
    valor = models.CharField(verbose_name="Valor/Dato", max_length=150)
    
    #Facturas Asociadas
    sujetoExcluido = models.ForeignKey(SujetoExcluido, null=True, blank=True, on_delete=models.CASCADE, related_name="apendices")
    comprobanteDonacion = models.ForeignKey(ComprobanteDonacion, null=True, blank=True, on_delete=models.CASCADE, related_name="apendicesDonacion")

    #Entidad a la que pertenece
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False)
    class Meta:
        verbose_name_plural = "Apendices"

    def __str__(self):
        return f'{self.campo}'

class ResponseHacienda(models.Model):
    
    nombre = models.CharField(max_length=100)
    datosJson = models.JSONField()
    status_code = models.IntegerField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    sujetoExcluido = models.ForeignKey(SujetoExcluido, on_delete=models.CASCADE, editable=False, null=True, blank=True, related_name="responses")
    comprobanteDonacion = models.ForeignKey(PagoDonacion, on_delete=models.CASCADE, editable=False, null=True, blank=True, related_name="responses")
    
    class Meta:
        verbose_name_plural = "Responses"