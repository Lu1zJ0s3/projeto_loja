from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from venda.models import CustomUser  # Importando CustomUser


class CadastroForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Usando CustomUser no lugar de User
        fields = ['username', 'email', 'password1', 'password2']  # Campos para cadastro

# Formulário de Login
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
