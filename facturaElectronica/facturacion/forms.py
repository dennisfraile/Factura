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
            'numeroControl': 'Numero de control',
            'codigoGeneracion': 'Generacion de generacion',
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
            'numeroControl': forms.TextInput(attrs={'class': 'form-control'}),
            'codigoGenercacion': forms.TextInput(attrs={'class': 'form-control'}),
            'motivoContin': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaEmi': forms.DateInput(attrs={'class': 'form-control'}),
            'tipoMoneda': forms.TextInput(attrs={'class': 'form-control'}),
        }