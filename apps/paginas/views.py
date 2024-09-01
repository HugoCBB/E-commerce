from django.shortcuts import render
from . models import produtos
# Create your views here.
def home(request):
    return render(request, 'site/home.html')

def produtos(request):
    return render(request, 'site/produtos.html')