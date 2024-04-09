from django import forms
from .models import *
from django.contrib.auth.models import *

class ActividadEconomicaForm(forms.Form):
    class Meta: 
        model = ActividadEconomica
        fields = '__all__'

class UserForm(forms.ModelForm):

    class meta:
        model = User
        fields = '__all__'
        
class RolForm(forms.ModelForm):

    class meta:
        model = Group
        fields = '__all__'

class DocumentoIdentidadForm(forms.ModelForm):
    class Meta:
        model = DocumentoIdentidad
        fields = '__all__'
        label = {
            'tipo': 'Tipo de Documento',
            'homologado': 'Homologacion',
            'numero': 'Dui sin guion',
            'user': 'Usuario'
        }
        widgets = {
           'numero': forms.TextInput(attrs={'class': 'form-control','data-mask':'00000000'}),
           'user': forms.SelectField(attrs={'class': 'form-control'}),
        }
        class Media:
            js = ['https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.10/jquery.mask.js']
    
        def __init__(self, *args, **kwargs):
            super(DocumentoIdentidadForm, self).__init__(*args, **kwargs)
            if self.initial:
                if 'numero' in self.initial:
                    self.initial['numero'] = str(self.initial['numero']).zfill(9)
        