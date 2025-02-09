from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from venda.models import CustomUser  # Importando CustomUser
from venda.forms import CadastroForm, LoginForm

# Função para cadastro de novos usuários
def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()  # Cria o usuário no banco de dados
            return redirect('login')  # Redireciona para o login após o cadastro
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

# Função de login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)  # Verifica se o usuário é válido
            if user is not None:
                login(request, user)  # Realiza o login
                return redirect('dashboard')  # Redireciona para a página do dashboard
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
