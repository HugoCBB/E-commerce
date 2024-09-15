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
    if request.method == 'POST':
        
        if form.is_valid():
            if form.cleaned_data['senha1'] != form.cleaned_data['senha2']:
                return redirect('cadastro')                
            else:
                nome = form.cleaned_data['nome']
                email = form.cleaned_data['email']
                senha = form.cleaned_data['senha1']
            
            nome = form['nome'].value()
            email = form['email'].value()        
            senha = form['senha1'].value()

            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')
            else:
                usuario = User.objects.create_user(
                    username=nome,
                    email=email,
                    password=senha
                    )
                usuario.save()
                return redirect('login')
            
    return render(request, 'usuario/cadastrar.html', {'form':form})