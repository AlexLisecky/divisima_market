from django import forms
from django.contrib.auth.forms import UserCreationForm

from authapp.models import UserMarket


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = UserMarket
        fields = ('username', 'email', 'avatar', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'contact-form'}),
            'email': forms.TextInput(attrs={'class': 'contact-form'}),
            'password1': forms.TextInput(attrs={'class': 'contact-form'}),
            'password2': forms.TextInput(attrs={'class': 'contact-form'}),
        }
