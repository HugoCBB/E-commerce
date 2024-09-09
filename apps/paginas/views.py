from django.shortcuts import render, get_object_or_404
from . models import Produto
# Create your views here.
def home(request):
    produto = Produto.objects.filter(publicada=True)
    return render(request, 'paginas/home.html', {'cards':produto})

def produtos(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'paginas/produtos.html', {'produto':produto})