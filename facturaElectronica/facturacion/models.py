from django.db import models
from usuarios.models import CustomerUser
# Create your models here.

class Pais(models.Model):
    
    codigo = models.PositiveIntegerField(verbose_name = "Codigo del pais", unique=True, blank=False)
    valor = models.CharField(verbose_name = "Nombre del pais", max_length=100, blank=False)

    class Meta:
        verbose_name_plural = "Paises"

    def __str__(self):
        return f'{self.valor}' 

class Departamento(models.Model):
    
    codigo = models.PositiveIntegerField(verbose_name = "Codigo del departamento", unique=True, blank=False)
    valor = models.CharField(verbose_name = "Nombre del departamento", max_length=100, blank=False)

    class Meta:
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return f'{self.valor}'

class Municipio(models.Model):
    
    codigo = models.PositiveIntegerField(verbose_name = "Codigo del municipio", unique=True, blank=False)
    valor = models.CharField(verbose_name = "Nombre del municipio", max_length=100, blank=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name="departamentos", editable=False)

    class Meta:
        verbose_name_plural = "Municipios"

    def __str__(self):
        return f'{self.valor}'
class Direccion(models.Model):

    complementoDireccion = models.CharField(verbose_name = "Direccion complemento",max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, editable=False)
    

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

class OperacionesSujetoExcluido(models.Model):
    
    TIPO_ITEM = (
        ("1", "Bienes"),
        ("2", "Servicios"),
        ("3", "Ambos (Bienes y servicios)"),
        ("4", "Otros tributos por item")
    )

    numItem = models.IntegerField(verbose_name = "N° item", required=True)
    tipoItem = models.CharField(verbose_name = "Tipo de item", required=True, choice=TIPO_ITEM)
    codigo = models.CharField(verbose_name = "Codigo", max_length=25, required=True)
    uniMedida = models.ForeignKey(UnidadMedida,  ondelete=models.CASCADE, editable=False)
    cantidad = models.IntegerField(verbose_name = "Cantidad", max_digits=12, decimal_places=2 , required=True)
    montoDescu = models.DecimalField(verbose_name = "Monto", max_digits=12, decimal_places=2 , required=True)
    compra = models.DecimalField(verbose_name = "Ventas", max_digits=12, decimal_places=2 ,required=True)
    retencion = models.DecimalField(verbose_name="Retencion", max_digits=12, decimal_places=2)
    descripccion = models.TextField(verbose_name="Descripccion", max_length=100, required=True)
    precioUni = models.DecimalField(verbose_name="Precio Unitario", max_digits=12, decimal_places=2 ,required=True)
    
    class Meta:
        verbose_name_plural = "Operaciones"

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
    formaPago = models.ForeignKey(FormaPago,  ondelete=models.CASCADE, editable=False)
    montoPago = models.DecimalField(verbose_name="Monto por forma de pago", max_digits=12, decimal_places=2)
    referencia = models.CharField(verbose_name="Referencia de la modalidad de pagos", max_length=50)
    plazo = models.CharField(verbose_name="Plazo", max_length=20, choices=PLAZO)
    periodo = models.IntegerField(verbose_name="Periodo de plazo")
    class Meta:
        verbose_name_plural = "Pagos"

    def __str__(self):
        return f'{self.codigo}'

class Apendice(models.Model):

    campo = models.CharField(verbose_name="Nombre del campo", max_length=25)
    etiqueta = models.CharField(verbose_name="Descripccion", max_length=50)
    valor = models.CharField(verbose_name="Valor/Dato", max_length=150)

    class Meta:
        verbose_name_plural = "Apendices"

    def __str__(self):
        return f'{self.campo}'

class TipoDocumento(models.Model):

    codigo = models.CharField(verbose_name="Codigo",max_length=3)
    valores = models.CharField(verbose_name="Valores",max_length=50)

    class Meta:
        verbose_name_plural = "Tipos de Documentos"

    def __str__(self):
        return f'{self.codigo}'

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
    version = models.IntegerField("Version",required=True)
    ambiente = models.CharField(verbose_name="Ambiente de destino", required=True, max_length=20, choices=AMBIENTE_DESTINO)
    tipoDte = models.ForeignKey(TipoDocumento, ondelete=models.CASCADE, editable=False)
    numeroControl = models.CharField(verbose_name="Numero de control", required=True, max_length=31)
    codigoGeneracion = models.CharField(verbose_name="Codigo de generacion", required=True, max_length=36)
    tipoModelo = models.CharField(verbose_name="Modelo de facturacion",required=True, choices=MODELO_FACTURACION)
    tipoOperacion = models.CharField(verbose_name="Tipo de Transmision", required=True, choices=TIPO_TRANSMICION)
    tipoContingencia = models.CharField(verbose_name="Tipo de Contingencia",required=False, choices=TIPO_CONTINGENCIA)
    motivoContin = models.CharField(verbose_name="Motivo de Contingencia", required=True, max_length=500)
    fechaEmi = models.DateTimeField(verbose_name="Fecha de Generacion",required=True)
    tipoMoneda = models.CharField(verbose_name="Tipo de Moneda", required=True, max_length=30)   
    class Meta:
        verbose_name_plural = "Identificaciones"

    def __str__(self):
        return f'{self.version}'

class Emisor(models.Model):

    #Emisor
    emisor = models.ForeignKey(CustomerUser, ondelete=models.CASCADE, editable=False)
    direccionEmisor = models.ForeignKey(Direccion, on_delete=models.CASCADE, editable=False)
    codEstableMH = models.CharField(verbose_name="Codigo del establecimiento asignado por el MH", max_length=4)
    codEstable = models.CharField(verbose_name="Codigo del establecimiento asignado por el contribuyente", max_length=10)
    codPuntoVentaMH = models.CharField(verbose_name="Codigo del punto de venta (Emisor) asignado por el MH", max_length=4)
    codPuntoVenta = models.CharField(verbose_name="Codigo del punto de venta (Emisor) asignado por el Contribuyente", max_length=15)
    class Meta:
        verbose_name_plural = "Emisores"

    def __str__(self):
        return f'{self.codPuntoVentaMH}'

class Receptor(models.Model):

    receptor = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, editable=False)
    direccionReceptor = models.ForeignKey(Direccion, on_delete=models.CASCADE, editable=False)

    class Meta:
        verbose_name_plural = "Receptores"

    def __str__(self):
        return f'{self.receptor_name}'
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
    identificador = models.ForeignKey(Identificador, ondelete=models.CASCADE, editable=False)
    
    #Emisor
    emisor = models.ForeignKey(Emisor, ondelete=models.CASCADE, editable=False)
    
    #Sujeto Excluido
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE, editable=False)
    
    #Cuerpo del Documento
    operaciones = models.ForeignKey(OperacionesSujetoExcluido, on_delete=models.CASCADE , editable=False)
    
    #Resumen
    totalCompra = models.DecimalField(verbose_name="Total de operaciones",max_digits=12, decimal_places=2)
    descu = models.DecimalField(verbose_name="Monto global de Descuento, Bonificacion, Rebajas", max_digits=12, decimal_places=2)
    totalDescu = models.DecimalField(verbose_name="Total del monto de Descuento, Bonificacion, Rebajas", max_digits=12, decimal_places=2)
    subTotal = models.DecimalField(verbose_name="Subtotal", max_digits=12, decimal_places=2)
    retencionIVAMH = models.CharField(verbose_name="Retencion IVA MH", required=True, choices=RETENCION_IVA_MH)
    ivaRete1 = models.DecimalFieldField(verbose_name="IVA Retenido", max_digits=12, decimal_places=2)
    reteRenta = models.DecimalField(verbose_name= "Rentencion de Renta", max_digits=12, decimal_places=2)
    totalPagar = models.DecimalField(verbose_name="Total a Pagar", max_digits=12, decimal_places=2)
    totalLetras = models.CharField(verbose_name="Total en letras", max_length=200)
    condicionOperacion = models.CharField(verbose_name="Condicion de la Operacion", choice=CONDICION_OPERACION)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE, editable=False)
    observaciones = models.CharField(verbose_name="Observaciones", max_length=3000)

    #Apendice
    apendice = models.ForeignKey(Apendice, on_delete=models.CASCADE, editable=False)
    
    #Si ya fue transmitido el sujeto excluido
    transmitido = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Sujetos Excluidos"

    def __str__(self):
        return f'{self.version}'


class OtroDocumentoAsociado(models.Model):
    OTRO_DOCUMENTO_ASOCIADO = (
        ("1", "Emisor"),
        ("2", "Receptor"),
        ("3", "Medico"),
        ("4", "Transporte")
    )
    codDocAsociado = models.CharField(verbose_name="Documento asociado", required=True, choices=OTRO_DOCUMENTO_ASOCIADO)
    descDocumento = models.CharField(verbose_name="Identificacion del documento asociado",max_length=100)
    detalleDocumento = models.CharField(verbose_name="Descripccion de documento asociado", max_length=300)

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
     
    numItem = models.IntegerField(verbose_name="N° item", min=1, max=2000 , required=True)
    tipoDonacion = models.CharField(verbose_name="Tipo de donacion", required=True, choice=TIPO_DONACION)
    cantidad = models.IntegerField(verbose_name="Cantidad", required=True)
    codigo = models.CharField(verbose_name="Codigo", max_length=25, required=True)
    uniMedida = models.ForeignKey(UnidadMedida,  ondelete=models.CASCADE, editable=False)
    descripccion = models.CharField(verbose_name="Descripccion", max_length=1000, required=True)
    depreciacion = models.IntegerField(verbose_name="Depreciacion", required=True)
    montoDescu = models.DecimalField(verbose_name="Monto", max_digits=12, decimal_places=2 , required=True)
    valorUni = models.DecimalField(verbose_name="Valor Unitario", max_digits=12, decimal_places=2 , required=True)
    valor = models.DecimalField(verbose_name="Valor Donado", max_digits=12, decimal_places=2)

    class Meta:
        verbose_name_plural = "Cuerpos del documento"

    def __str__(self):
        return f'{self.codDocAsociado}'

class PagoDonacion(models.Model):

    codigo = models.CharField(verbose_name="Codigo de Forma de pago", max_length=2)
    montoPago = models.DecimalField(verbose_name="Monto por Forma de pago", max_digits=12, decimal_places=2)
    referencia = models.CharField(verbose_name="Referencia de la modalidad de pago", max_length=50)

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
    identificador = models.ForeignKey(Identificador, ondelete=models.CASCADE, editable=False) 

    #Donatorio
    emisor = models.ForeignKey(Emisor, ondelete=models.CASCADE, editable=False)
    
    #Donante
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE, editable=False)
    codDomiciliado = models.CharField(verbose_name="Domicilio Fiscal", required=True, choices=DOMICILIO_FISCAL)
    codPais = models.ForeignKey(Pais, on_delete=models.CASCADE, editable=False)

    #Otros Documentos Asociados
    otrosDocumentos = models.ForeignKey(OtroDocumentoAsociado, ondelete=models.CASCADE, editable=False)

    #Cuerpo del Documento
    cuerpoDocumento = models.ForeignKey(CuerpoDocumento, ondelete=models.CASCADE, editable=False)

    #Resumen
    valorTotal = models.DecimalField(verbose_name="Total de la donacion", max_digits=12, decimal_places=2)
    totalLetras = models.CharField(verbose_name="Total en letras", max_length=200)
    pago = models.ForeignKey(PagoDonacion, on_delete=models.CASCADE, editable=False)

    #Apendice
    apendice = models.ForeignKey(Apendice, on_delete=models.CASCADE, editable=False)
    
    #Si ya fue transmitido el comprobante de donacion
    transmitido = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Comprobantes de Donaciones"

    def __str__(self):
        return f'{self.version}'