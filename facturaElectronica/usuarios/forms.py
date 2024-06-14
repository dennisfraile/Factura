from django import forms
from .models import *
from django.contrib.auth.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class ActividadEconomicaForm(forms.Form):
    class Meta: 
        model = ActividadEconomica
        fields = '__all__'

class SystemAdminRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        if User.objects.filter(is_system_superuser=True).exists():
            raise forms.ValidationError("Ya existe un administrador general en el sistema.")
        return cleaned_data

class CustomUserForm(UserCreationForm):
    entidad = forms.ModelChoiceField(queryset=Entidad.objects.all(), required=False)
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False)
    is_system_superuser = forms.BooleanField(required=False)

    class meta:
        model = CustomUser
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