from django import forms
from django.contrib.auth.models import User


class Registro(forms.Form):
    username = forms.CharField(required=True, min_length=5, max_length=40, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nombre de usuario',
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'ejemplo@gamil.com'
    }))
    password = forms.CharField(required=True, min_length=3, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña'
    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nombre de usuario ya existe')
