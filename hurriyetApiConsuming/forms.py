from django import forms
from django.contrib.auth.models import User
from .models import MyUser, userPreferences
from hurriyetApiConsuming.services import getPaths

class RegisterForm(forms.ModelForm):
        email = forms.CharField(widget = forms.EmailInput(attrs={'class': 'required form-control', 'placeholder': 'email_addr'}),label = '')
        password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'required form-control', 'placeholder': 'pwd'}),label = '')
        user = User()
        class Meta:
            model = MyUser
            fields = (
            'email',
            'password')

class UnknownForm(forms.Form): 
    choices = forms.CharField(max_length=300)