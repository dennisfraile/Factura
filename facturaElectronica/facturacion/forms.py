from .models import *
from django import forms

class PaisForm(forms.ModelForm):

    class Meta:
        model = Pais
        fields = ['codigo', 'valor']
    def __init__(self, *args, **kwargs):
        super(PaisForm, self).__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})

class DepartamentoForm(forms.ModelForm):

    class Meta:
        model = Departamento
        fields = ['codigo', 'valor']
    
    def __init__(self, *args, **kwargs):
        super(DepartamentoForm, self).__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})

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
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(MunicipioForm, self).__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})

class DireccionForm(forms.ModelForm):
    
    class Meta:
        model = Direccion
        fields = ['complementoDireccion', 'municipio']
    
    def __init__(self, *args, **kwargs):
        super(DireccionForm, self).__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
           
    
class UnidadMedidaForm(forms.ModelForm):

    class Meta:
        model = UnidadMedida
        fields = ['codigo', 'valor']
    
    def __init__(self, *args, **kwargs):
        super(UnidadMedidaForm, self).__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})

class OperacionesSujetoExcluidoForm(forms.ModelForm):
    tipoItem: forms.ChoiceField(
            choices=[
               ("1", "Bienes"),
               ("2", "Servicios"),
               ("3", "Ambos (Bienes y servicios)"),
               ("4", "Otros tributos por item")
            ],
            widget=forms.Select(attrs={'class': 'form-control'}),
            label="Tipo de item"
        ) # type: ignore
    class Meta:
        model = OperacionesSujetoExcluido 
        fields = [
            'numItem','tipoItem','codigo','uniMedida','cantidad',
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
            'numItem': forms.NumberInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'uniMedida': forms.Select(attrs={'class': 'form-control'}),
            'cantidad' : forms.NumberInput(attrs={'class': 'form-control'}),
            'descripccion' : forms.Textarea(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput, forms.NumberInput, forms.DecimalField, forms.Textarea)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})

class FormaPagoForm(forms.ModelForm):

    class Meta:
        model = FormaPago
        fields = ['codigo', 'valor'] 
    
    def __init__(self, *args, **kwargs):
        super(FormaPagoForm, self).__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})

class PagoForm(forms.ModelForm):

    class Meta:
        model = Pago
        plazo = forms.ChoiceField(
            choices=[
                ("01", "Dias"),
                ("02", "Meses"),
                ("03", "Años")
            ],
            widget=forms.Select(attrs={'class': 'form-control'}) 
        )
        fields = ['formaPago','montoPago','referencia','plazo','periodo']
        label = {
            'formaPago': 'Forma de Pago',
            'montoPago': 'Monto por forma de Pago',
            'referencia': 'Referencia de la modalidad de pagos',
            'plazo': 'Plazo',
            'periodo': 'Periodo de plazo',
        }
        widgets ={
            'formaPago': forms.Select(attrs={'class': 'form-control'}),
            'referencia': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
    
    def __init__(self, *args, **kwargs):
        super(PagoForm, self).__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})

class ApendiceForm(forms.ModelForm):

    class Meta:
        model = Apendice
        fields =['campo','etiqueta','valor']
        widgets = {
            'campo': forms.TextInput(attrs={'class': 'form-control'}),
            'etiqueta': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
    
    def __init__(self, *args, **kwargs):
        entidad = kwargs.pop('entidad', None)
        super(ApendiceForm, self).__init__(*args, **kwargs)
        if entidad:
            self.fields['sujetoExcluido'].queryset = SujetoExcluido.objects.filter(entidad=entidad)
            self.fields['comprobanteDonacion'].queryset = ComprobanteDonacion.objects.filter(entidad=entidad)
        
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput, forms.NumberInput, forms.DecimalField, forms.Textarea)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})

class TipoDocumentoForm(forms.ModelForm):

    class Meta:
        model = TipoDocumento
        fields ='__all__'
    
    def __init__(self, *args, **kwargs):
        super(TipoDocumentoForm, self).__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})

class IdentificadorForm(forms.ModelForm):

    class Meta:
        model = Identificador
        ambiente = forms.ChoiceField(
            choices=[
                ("00","Modo Prueba"),
                ("01","Modo Produccion")
            ],
            widget=forms.Select(attrs={'class': 'form-control'})  
        )
        tipoModelo = forms.ChoiceField(
            choices=[
                ("1", "Modelo de Facturacion previo"),
                ("2", "Modelo de Facturacion diferido")
            ],
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        tipoOperacion = forms.ChoiceField(
            choices=[
               ("1", "Transmision normal"),
               ("2", "Transmision por contingencia") 
            ],
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        tipoContingencia = forms.ChoiceField(
            choices=[
               ("1", "No disponibilidad de sistema del MH"),
               ("2", "No disponibilidad de sistema del emisor"),
               ("3", "Falla en el suministro de servicio de Internet del Emisor"),
               ("4", "Falla en el suministro de servicio de energia electrica del emisor que impida la transmision de los DTE"),
               ("5", "Otro (debera digitar un maximo de 500 caracteres explicando el motivo)") 
            ],
            widget=forms.Select(attrs={'class': 'form-control'})
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
            'tipoMoneda':'Tipo de moneda'
        }
        widgets = {
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoDte': forms.Select(attrs={'class': 'form-control'}),
            'motivoContin': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoMoneda': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(IdentificadorForm, self).__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})

class ReceptorForm(forms.ModelForm):
            
    tipo = forms.ChoiceField(
        choices={
            ("13","DUI"),
            ("36","NIT"),
            ("37","Otro"),
            ("03","Pasaporte"),
            ("02","Carnet de Residente")
        },
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    homologado = forms.ChoiceField(
        choices={
            ("DUI","Documento Homologado"),
            ("NIT","Documento No Homologado")
        },
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Receptor
        fields = ['tipo', 'homologado','numero','nrc', 'nombre', 'actividadEconomica', 'direccionReceptor','cellphone', 'email']
        label ={
            'tipo': 'Tipo', 
            'homologado':'Homologado',
            'numero':'Numero',
            'nrc':'NRC',
            'nombre':'Nombre',
            'actividadEconomica':'ActividadEconomica',
            'cellphone':'Numero de Telefono',
            'email':'Email',
            }
        widgets = {
            'numero': forms.TextInput(attrs={'class':'form-control','data-mask':'000000000'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'actividadEconomica': forms.Select(attrs={'class':'form-control'}),
            'cellphone': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }
        
        class Media:
            js = ['https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.10/jquery.mask.js']
    
            
    
    def __init__(self, *args, **kwargs):
        entidad = kwargs.pop('entidad',None)
        super(ReceptorForm, self).__init__(*args, **kwargs)
        if self.initial:
                if 'numero' in self.initial:
                    self.initial['numero'] = str(self.initial['numero']).zfill(9)
        if entidad:
            self.fields['direccionReceptor'].queryset = Direccion.objects.filter(entidad=entidad)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
    

class SujetoExcluidoForm(forms.ModelForm):
    
    
    receptor = forms.ModelChoiceField(
        queryset=Receptor.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Receptor"
    )
    pago = forms.ModelChoiceField(
        queryset=Pago.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Pago"
    )
    condicionOperacion = forms.ChoiceField(
        choices=[
            ("1", "Contado"),
            ("2", "A credito"),
            ("3", "Otro")
        ],
        label="Condición de Operación",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    

    class Meta:
        model = SujetoExcluido
        fields = '__all__'
        labels = {
            'totalCompra': 'Total de Operaciones',
            'descu': 'Monto Global del Descuento',
            'totalDescu': 'Total del monto de Descuento',
            'subTotal': 'Subtotal',
            'retencionIVAMH': 'Retención IVA MH',
            'ivaRete1': 'IVA Retenido',
            'reteRenta': 'Retención de Renta',
            'totalPagar': 'Total a Pagar',
            'totalLetras': 'Total en Letras',
            'condicionOperacion': 'Condición de Operación',
            'observaciones': 'Observaciones',
        }
        widgets = {
            'totalCompra': forms.NumberInput(attrs={'class': 'form-control'}),
            'descu': forms.NumberInput(attrs={'class': 'form-control'}),
            'totalDescu': forms.NumberInput(attrs={'class': 'form-control'}),
            'ivaRete1': forms.NumberInput(attrs={'class': 'form-control'}),
            'reteRenta': forms.NumberInput(attrs={'class': 'form-control'}),
            'totalPagar': forms.NumberInput(attrs={'class': 'form-control'}),
            'totalLetras': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        entidad = kwargs.pop('entidad', None)
        super().__init__(*args, **kwargs)
        if entidad:
            self.fields['receptor'].queryset = Receptor.objects.filter(entidad=entidad)
            self.fields['pago'].queryset = Pago.objects.filter(entidad=entidad)
        
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput, forms.NumberInput, forms.DecimalField)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})

class OtroDocumentoAsociadoForm(forms.ModelForm):
    class Meta:
        model = OtroDocumentoAsociado
        codDocAsociado = forms.ChoiceField(
            choices={
                ("1", "Emisor"),
                ("2", "Receptor"),
                ("3", "Medico"),
                ("4", "Transporte")
            },
            widget=forms.Select(attrs={'class': 'form-control'}) 
        )
        fields = '__all__'
        label = {
            'codDocAsociado': 'Documento Asociado',
            'descDocumento': 'Identificacion del Documento Asociado',
            'detalleDocumento': 'Descripccion de Documento Asociado',
        }
        widgets = {
            'descDocumento': forms.TextInput(attrs={'class': 'form-control'}),
            'detalleDocumento': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(OtroDocumentoAsociadoForm, self).__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})

class CuerpoDocumentoForm(forms.ModelForm):
    class Meta:
        model = CuerpoDocumento
        tipoDonacion = forms.ChoiceField(
            choices={
                ("1", "Efectivo"),
                ("2", "Bien"),
                ("3", "Servicio"),
            },
            widget=forms.Select(attrs={'class': 'form-control'}) 
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
            
        }
        widgets = {
            'numItem': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'uniMedida': forms.Select(attrs={'class': 'form-control'}),
            'descripccion': forms.TextInput(attrs={'class': 'form-control'}),
            'comprobanteDonacion': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(CuerpoDocumentoForm, self).__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput, forms.NumberInput, forms.DecimalField)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})

class PagoDonacionForm(forms.ModelForm):
    class Meta:
        model = PagoDonacion
        fields = '__all__'
        label = {
            'codigo': 'Codigo de Forma de Pago',
            'montoPago': 'Pago de Forma de Pago',
            'referencia': 'Ferencia de Forma de la modalidad de Pago'
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'referencia': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(PagoDonacionForm, self).__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})

class ComprobanteDonacionForm(forms.ModelForm):
       
    class Meta:
        model = ComprobanteDonacion
        receptor = forms.ModelChoiceField(
            queryset=Receptor.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            label="Receptor"
        )
        codDomiciliado = forms.ChoiceField(
            choices = {
                ("1", "Domiciliado"),
                ("2", "No Domiciliado"),
            },
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        fields = '__all__'
        label = {
            'codDomiciliado': 'Domicilio Fiscal',
            'codPais': 'Codigo de Pais',
            'valorTotal': 'Total de la Donacion',
            'totalLetras': 'Total en Letras',
        }
        widgets = {
            'codPais': forms.Select(attrs={'class': 'form-control'}),
            'totalLetras': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
    
    def __init__(self, *args, **kwargs):
        entidad = kwargs.pop('entidad',None)
        super().__init__(*args, **kwargs)
        if entidad:
            self.fields['receptor'].queryset = Receptor.objects.filter(entidad=entidad)
            self.fields['pagoDonacion'].queryset = PagoDonacion.objects.filter(entidad=entidad)
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
