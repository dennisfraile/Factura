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

class EntidadForm(forms.ModelForm):
    class meta:
        model= Entidad
        fields = '__all__'

class ParametrosAuthHaciendaForm(forms.ModelForm):
    class meta:
        model = ParametrosAuthHacienda
        fields = '__all__'
        label = {
            'userAgent': 'User Agent',
            'nit': 'NIT',
            'privateKey': 'Llave Privada',
            'pwd': 'Password',
            'entidad': 'Entidad',
        }
        widgets = {
            'userAgent': forms.TextInput(attrs={'class': 'form-control'}),
            'nit': forms.TextInput(attrs={'class': 'form-control','data-mask':'00000000000000'}),
            'privateKey': forms.TextInput(attrs={'class': 'form-control'}),
            'pwd': forms.TextInput(attrs={'class': 'form-control'}),
            'entidad': forms.SelectField(attrs={'class': 'form-control'}),
        }
        class Media:
            js = ['https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.10/jquery.mask.js']
    
        def __init__(self, *args, **kwargs):
            super(ParametrosAuthHaciendaForm, self).__init__(*args, **kwargs)
            if self.initial:
                if 'nit' in self.initial:
                    self.initial['nit'] = str(self.initial['nit']).zfill(9)