from django import forms
from .models import *
from django.contrib.auth.models import *

class UserForm(forms.ModelForm):

    class meta:
        model = User
        widgets = {
            'dui': forms.TextInput(attrs={'data-mask':'0000000-0'})
        }
        fields = '__all__'
    
    class Media:
        js = ['https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.10/jquery.mask.js']
    
    def __init__(self, *args, **kwargs):
       super(UserForm, self).__init__(*args, **kwargs)
       if self.initial:
           if 'dui' in self.initial:
               self.initial['dui'] = str(self.initial['dui']).zfill(9)

class RolForm(forms.ModelForm):

    class meta:
        model = Group
        fields = '__all__'