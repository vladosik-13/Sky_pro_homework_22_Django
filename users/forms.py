from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text='Необязательное поле, введите ваш номер телефона')

    class Meta:
        model = CustomUser
        fields = ('email', 'phone_number', 'password1', 'password2')