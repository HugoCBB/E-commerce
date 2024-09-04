from django.shortcuts import render
from . models import Produto
# Create your views here.
def home(request):
    produtos = Produto.objects.filter(publicada=True)
    return render(request, 'site/home.html', {'cards':produtos})

def produtos(request):
    return render(request, 'site/produtos.html')