from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from . forms import LoginForm, CadastroForm

# Create your views here.
def login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = form['email'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                email=email,
                password = senha
            )

            if usuario is not None:
                return redirect('home')
            else:
                return redirect('login')

    return render(request, 'usuario/login.html', {'form':form})

def cadastrar(request):
    form = CadastroForm(request.POST or None)
    return render(request, 'usuario/cadastrar.html')