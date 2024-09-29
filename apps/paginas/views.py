from django.shortcuts import render, get_object_or_404,redirect
from apps.manager.forms import ProdutoForm
from . models import Produto
# Create your views here.

def home(request):
    produto = Produto.objects.filter(publicada=True)
    return render(request, 'paginas/home.html', {'cards':produto})

def produtos(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'paginas/produtos.html', {'produto':produto})

def editar_produtos(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    form = ProdutoForm(instance=produto)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)

        if form.is_valid():
            form.save()
            return redirect('home') 
    return render(request, 'manager/editar_produto.html',{'form':form, 'produto_id':produto_id})


def deletar_produtos(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    produto.delete()
    return redirect('home')