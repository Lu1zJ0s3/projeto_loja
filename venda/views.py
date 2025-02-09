from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from venda.models import CustomUser  
from venda.forms import CadastroForm, LoginForm


def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)  
            if user is not None:
                login(request, user)  
                return redirect('dashboard')  
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
