from django import forms
from .models import *
from .models import Entidad
from django.contrib.auth.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class ActividadEconomicaForm(forms.ModelForm):
    class Meta: 
        model = ActividadEconomica
        fields = '__all__'

class SystemAdminRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'lastname', 'email', 'cellphone', 'organizacion', 'nrc', 'actividadEconomica', 'is_system_superuser','is_entidad_superuser','is_staff', 'password1', 'password2']
    
    def clean(self):
        cleaned_data = super().clean()
        if User.objects.filter(is_system_superuser=True).exists():
            raise forms.ValidationError("Ya existe un administrador general en el sistema.")
        return cleaned_data

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
            'autofocus': True
        }),
        label=_("Correo electrónico"),
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError(_("Correo electrónico o contraseña incorrectos."))
        
        if not user.check_password(password):
            raise forms.ValidationError(_("Correo electrónico o contraseña incorrectos."))
        
        return cleaned_data

class CustomUserForm(UserCreationForm):
    entidad = forms.ModelChoiceField(
        queryset=Entidad.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
    is_system_superuser = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = CustomUser
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super(CustomUserForm, self).__init__(*args, **kwargs)
        if usuario:
            self.fields['entidad'].queryset = Entidad.objects.filter(usuarios=usuario)
        
        # Añadir clase 'form-control' a todos los campos del formulario automáticamente
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Select, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
        
class RolForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'

class EntidadForm(forms.ModelForm):
    class Meta:
        model= Entidad
        fields = '__all__'

class ParametrosAuthHaciendaForm(forms.ModelForm):
    class Meta:
        model = ParametrosAuthHacienda
        fields = ['userAgent','nit','pwd','privateKey','publicKey']
        label = {
            'userAgent': 'User Agent',
            'nit': 'NIT',
            'privateKey': 'Llave Privada',
            'publicKey': 'Llave Publica',
            'pwd': 'Password',
            
        }
        widgets = {
            'userAgent': forms.TextInput(attrs={'class': 'form-control'}),
            'nit': forms.TextInput(attrs={'class': 'form-control','data-mask':'00000000000000'}),
            'privateKey': forms.TextInput(attrs={'class': 'form-control'}),
            'publicKey': forms.TextInput(attrs={'class': 'form-control'}),
            'pwd': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        class Media:
            js = ['https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.10/jquery.mask.js']
    
        def __init__(self, *args, **kwargs):
            super(ParametrosAuthHaciendaForm, self).__init__(*args, **kwargs)
            if self.initial:
                if 'nit' in self.initial:
                    self.initial['nit'] = str(self.initial['nit']).zfill(9)