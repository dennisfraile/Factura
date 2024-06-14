from .models import *
from django import forms

class PaisForm(forms.ModelForm):

    class Meta:
        model = Pais
        fields = ['codigo', 'valor']

class DepartamentoForm(forms.ModelForm):

    class Meta:
        model = Departamento
        fields = ['codigo', 'valor']

class MunicipioForm(forms.ModelForm):

    class Meta:
        model = Municipio
        fields = ['codigo', 'valor', 'departamento']
        label = {
            'codigo': 'Codigo',
            'valor': 'Valor',
            'departamento': 'Departamento',
        }
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
        }

class DireccionForm(forms.ModelForm):

    class Meta:
        model = Direccion
        fields = ['complementoDireccion', 'municipio']
        label = {
            'complementoDireccion': 'Complemento de la direccion',
            'municipio': 'Municipio',
        }
        widgets = {
            'complementoDireccion' : forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
        }

class UnidadMedidaForm(forms.ModelForm):

    class Meta:
        model = UnidadMedida
        fields = ['codigo', 'valor']

class OperacionesSujetoExcluidoForm(forms.ModelForm):

    class Meta:
        model = OperacionesSujetoExcluido 
        tipoItem: forms.ChoiceField(
            choices=[
               ("1", "Bienes"),
               ("2", "Servicios"),
               ("3", "Ambos (Bienes y servicios)"),
               ("4", "Otros tributos por item")
            ]
        ) # type: ignore
        fields = [
            'numItem','tipoItem','codigo','UniMedida','cantidad',
            'montoDescu','compra','retencion','descripccion','precioUni'
            ]
        label = {
            'numItem': 'Numero de item',
            'tipoItem': 'Tipo de item',
            'codigo': 'Codigo',
            'uniMedida': 'Unidad de medida',
            'cantidad': 'Cantidad',
            'montoDescu': 'Monto de descuento',
            'compra': 'Compra',
            'retencion': 'Retencion',
            'descripccion': 'Descripccion',
            'precioUni': 'Precio Unitario'
            }
        widgets = {
            'numItem': forms.IntegerField(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'uniMedida': forms.Select(attrs={'class': 'form-control'}),
            'cantidad' : forms.IntegerField(attrs={'class': 'form-control'}),
            'montoDescu' : forms.DecimalField(attrs={'class': 'form-control'}),
            'compra' : forms.DecimalField(attrs={'class': 'form-control'}),
            'retencion' : forms.DecimalField(attrs={'class': 'form-control'}),
            'description' : forms.TextField(attrs={'class': 'form-control'}),
            'precioUni' : forms.DecimalField(attrs={'class': 'form-control'})
        }
class FormaPagoForm(forms.ModelForm):

    class Meta:
        model: FormaPago
        fields = ['codigo', 'valor'] 

class PagoForm(forms.ModelForm):

    class Meta:
        model = Pago
        plazo = forms.ChoiceField(
            choices=[
                ("01", "Dias"),
                ("02", "Meses"),
                ("03", "Años")
            ]
        )
        fields = ['codigo', 'formaPago','montoPago','referencia','plazo','periodo']
        label = {
            'codigo': 'Codigo',
            'formaPago': 'Forma de Pago',
            'montoPago': 'Monto por forma de Pago',
            'referencia': 'Referencia de la modalidad de pagos',
            'plazo': 'Plazo',
            'periodo': 'Periodo de plazo',
        }
        widgets ={
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'formaPago': forms.Select(attrs={'class': 'form-control'}),
            'montoPago': forms.DecimalField(attrs={'class': 'form-control'}),
            'referencia': forms.TextInput(attrs={'class': 'form-control'}),
            'periodo': forms.IntegerField(attrs={'class': 'form-control'}),
        }

class ApendiceForm(forms.ModelForm):

    class Meta:
        model = Apendice
        fields =['campo','etiqueta','valor']
        label = {
            'codigo': 'Codigo',
            'etiqueta': 'Etiqueta',
            'valor': 'Valor',
        }
        
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'etiqueta': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TipoDocumentoForm(forms.ModelForm):

    class Meta:
        models = TipoDocumento
        fields =['codigo', 'valores']

class IdentificadorForm(forms.ModelForm):

    class Meta:
        models = Identificador
        ambiente = forms.ChoiceField(
            choices=[
                ("00","Modo Prueba"),
                ("01","Modo Produccion")
            ]
        )
        tipoModelo = forms.ChoiceField(
            choices=[
                ("1", "Modelo de Facturacion previo"),
                ("2", "Modelo de Facturacion diferido")
            ]
        )
        tipoOperacion = forms.ChoiceField(
            choices=[
               ("1", "Transmision normal"),
               ("2", "Transmision por contingencia") 
            ]
        )
        tipoContingencia = forms.ChoiceField(
            choices=[
               ("1", "No disponibilidad de sistema del MH"),
               ("2", "No disponibilidad de sistema del emisor"),
               ("3", "Falla en el suministro de servicio de Internet del Emisor"),
               ("4", "Falla en el suministro de servicio de energia electrica del emisor que impida la transmision de los DTE"),
               ("5", "Otro (debera digitar un maximo de 500 caracteres explicando el motivo)") 
            ]
        )
        fields ='__all__'
        label = {
            'version': 'Version',
            'ambiente': 'Ambiente de destino',
            'tipoDte': 'Tipo de documento',
            'tipoModelo': 'Modelo de Facturacion',
            'tipoOperacion':'Tipo de transmicion',
            'tipoContingencia':'Tipo de contingencia',
            'motivoContin': 'Motivo de contingencia',
            'fechaEmi':'Fecha de generacion',
            'tipoMoneda':'Tipo de moneda'
        }
        widgets = {
            'version': forms.IntegerField(attrs={'class': 'form-control'}),
            'tipoDte': forms.Select(attrs={'class': 'form-control'}),
            'motivoContin': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaEmi': forms.DateInput(attrs={'class': 'form-control'}),
            'tipoMoneda': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ReceptorForm(forms.Form):
    
    direccionReceptor = forms.ModelChoiceField(queryset=Direccion.objects.none(), widget=forms.Select(attrs={'class': 'form-control'}), label = "Direccion del Receptor")
    def __init__(self, *args, **kwargs):
        entidad = kwargs.pop('entidad',None)
        super().__init__(*args, **kwargs)
        if entidad:
            self.fields['direccionReceptor'].queryset = Direccion.objects.filter(entidad=entidad)
            
    tipo = forms.ChoiceField(
        choices={
            ("13","DUI"),
            ("36","NIT"),
            ("37","Otro"),
            ("03","Pasaporte"),
            ("02","Carnet de Residente")
        }
    )
    homologado = forms.ChoiceField(
        choices={
            ("DUI","Documento Homologado"),
            ("NIT","Documento No Homologado")
        }
    )
    class Meta:
        models = Receptor
        fields = ['tipo', 'homologado','numero', 'nombre', 'actividadEconomica', 'direccionReceptor','cellphone', 'email']
        label ={
            'tipo': 'Tipo', 
            'homologado':'Homologado',
            'numero':'Numero',
            'nombre':'Nombre',
            'actividadEconomica':'ActividadEconomica',
            'cellphone':'Numero de Telefono',
            'email':'Email',
            }
        widgets = {
            'numero': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'actividadEconomica': forms.Select(attrs={'class':'form-control'}),
            'cellphone': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailField(attrs={'class':'form-control'}),
        }

class SujetoExcluidoForm(forms.Form):
    
    identificador = forms.ModelChoiceField(queryset=Identificador.objects.none(), widget=forms.Select(attrs={'class': 'form-control'}), label = "Identificador")
    receptor = forms.ModelChoiceField(queryset=Receptor.objects.none(), widget=forms.Select(attrs={'class': 'form-control'}), label = "Receptor")
    pago = forms.ModelChoiceField(queryset=Pago.objects.none(), widget=forms.Select(attrs={'class': 'form-control'}), label = "Pago")
    def __init__(self, *args, **kwargs):
        entidad = kwargs.pop('entidad',None)
        super().__init__(*args, **kwargs)
        if entidad:
            self.fields['identificador'].queryset = Identificador.objects.filter(entidad=entidad)
            self.fields['receptor'].queryset = Receptor.objects.filter(entidad=entidad)
            self.fields['pago'].queryset = Pago.objects.filter(identificador=entidad)
    class Meta:
        models = SujetoExcluido
        condicionOperacion = forms.ChoiceField(
            choices={
                ("1", "Contado"),
                ("2", "A credito"),
                ("3", "Otro")
            }
        )
        retencionIVAMH = forms.ChoiceField(
            choices={
                ("22", "Retencion IVA 1%"),
                ("C4", "Retencion IVA 13%"),
                ("C9", "Otras retenciones IVA casos especiales")
            }
        )
        
        fields = '__all__'
        label = {
            'totalCompra':'Total de Operaciones',
            'descu':'Monto Global del Descuento',
            'totalDescu':'Total del monto de Descuento',
            'subtotal':'Subtotal',
            'retencionIVAMH':'Retencion IVA MH',
            'ivaRete1':'Iva Retenido',
            'reteRenta': 'Retencion de Renta',
            'totalPagar':'Total a Pagar',
            'totalLetras':'Total en Letras',
            'condicionOperacion':'Condicion de Operacion',
            'observaciones':'Observaciones',
        }
        widgets = {
            'totalCompra': forms.DecimalField(attrs={'class': 'form-control'}),
            'descu': forms.DecimalField(attrs={'class': 'form-control'}),
            'totalDescu': forms.DecimalField(attrs={'class': 'form-control'}),
            'subTotal': forms.DecimalField(attrs={'class': 'form-control'}),
            'ivaRete1': forms.DecimalField(attrs={'class': 'form-control'}),
            'reteRenta': forms.DecimalField(attrs={'class': 'form-control'}),
            'totalPagar': forms.DecimalField(attrs={'class': 'form-control'}),
            'totalLetras': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones':forms.TextInput(attrs={'class': 'form-control'}),
        }

class OtroDocumentoAsociadoForm(forms.Form):
    class Meta:
        models = OtroDocumentoAsociado
        codDocAsociado = forms.ChoiceField(
            choices={
                ("1", "Emisor"),
                ("2", "Receptor"),
                ("3", "Medico"),
                ("4", "Transporte")
            }
        )
        fields = '__all__'
        label = {
            'codDocAsociado': 'Documento Asociado',
            'descDocumento': 'Identificacion del Documento Asociado',
            'detalleDocumento': 'Descripccion de Documento Asociado',
            'comprobanteDonacion': 'Comprobante de Donacion',
        }
        widgets = {
            'descDocumento': forms.TextInput(attrs={'class': 'form-control'}),
            'detalleDocumento': forms.TextInput(att={'class': 'form-control'}),
            'comprobanteDonacion': forms.Select(att={'class': 'form-control'}),
        }

class CuerpoDocumentoForm(forms.Form):
    class Meta:
        models = CuerpoDocumento
        tipoDonacion = forms.ChoiceField(
            choices={
                ("1", "Efectivo"),
                ("2", "Bien"),
                ("3", "Servicio"),
            }
        )
        fields = '__all__'
        label = {
            'numItem': 'N° item',
            'tipoDonacion': 'Tipo de Donacion',
            'cantidad': 'Cantidad',
            'codigo': 'Codigo',
            'uniMedida': 'Unidad de medida',
            'descripccion': 'Descripccion',
            'depreciacion': 'Depreciacion',
            'montoDescu': 'Monto',
            'valorUni': 'Valor Unitario',
            'valor': 'Valor Donado',
            'comprobanteDonacion': 'Comprobante de Donacion',
            
        }
        widgets = {
            'numItem': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.IntegerField(att={'class': 'form-control'}),
            'codigo': forms.TextInput(att={'class': 'form-control'}),
            'uniMedida': forms.Select(att={'class': 'form-control'}),
            'descripccion': forms.TextInput(att={'class': 'form-control'}),
            'depreciacion': forms.IntegerField(att={'class': 'form-control'}),
            'montoDescu': forms.DecimalField(att={'class': 'form-control'}),
            'valorUni': forms.DecimalField(att={'class': 'form-control'}),
            'valor': forms.DecimalField(att={'class': 'form-control'}),
            'comprobanteDonacion': forms.Select(att={'class': 'form-control'}),
        }

class PagoDonacionForm(forms.Form):
    class Meta:
        models = PagoDonacion
        fields = '__all__'
        label = {
            'codigo': 'Codigo de Forma de Pago',
            'montoPago': 'Pago de Forma de Pago',
            'referencia': 'Ferencia de Forma de la modalidad de Pago'
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'montoPago': forms.DecimalField(attrs={'class': 'form-control'}),
            'referencia': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ComprobanteDonacionForm(forms.Form):
    identificador = forms.ModelChoiceField(queryset=Identificador.objects.none(), widget=forms.Select(attrs={'class': 'form-control'}), label = "Identificador")
    receptor = forms.ModelChoiceField(queryset=Receptor.objects.none(), widget=forms.Select(attrs={'class': 'form-control'}), label = "Receptor")
    pagoDonacion = forms.ModelChoiceField(queryset=PagoDonacion.objects.none(), widget=forms.Select(attrs={'class': 'form-control'}), label = "Pago Donacion")
    def __init__(self, *args, **kwargs):
        entidad = kwargs.pop('entidad',None)
        super().__init__(*args, **kwargs)
        if entidad:
            self.fields['identificador'].queryset = Identificador.objects.filter(entidad=entidad)
            self.fields['receptor'].queryset = Receptor.objects.filter(entidad=entidad)
            self.fields['pagoDonacion'].queryset = PagoDonacion.objects.filter(identificador=entidad)
    class Meta:
        models = ComprobanteDonacion
        codDomiciliado = forms.ChoiceField(
            choices = {
                ("1", "Domiciliado"),
                ("2", "No Domiciliado"),
            }
        )
        fields = '__all__'
        label = {
            'identificador': 'Identificador',
            'emisor': 'Donatorio',
            'codDomiciliado': 'Domicilio Fiscal',
            'codPais': 'Codigo de Pais',
            'valorTotal': 'Total de la Donacion',
            'totalLetras': 'Total en Letras',
        }
        widgets = {
            'identificador': forms.Select(att={'class': 'form-control'}),
            'emisor':forms.Select(att={'class': 'form-control'}),
            'codPais': forms.Select(att={'class': 'form-control'}),
            'valorTotal': forms.DateTimeField(attrs={'class': 'form-control'}),
            'totalLetras': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
