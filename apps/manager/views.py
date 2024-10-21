from django.shortcuts import render, redirect
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from apps.paginas.models import Produto
from .forms import ProdutoForm

# Create your views here.
@has_role_decorator('gerente')
def manager(request):
    return render(request, 'manager/manager.html')
    


@has_permission_decorator('adicionar_produtos')
def AdicionarProduto(request):
    form = ProdutoForm()
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'manager/forms.html', {'form':form})

def ExibirProdutos(request):
    produtos = Produto.objects.all()

    return render(request, 'manager/exibirprodutos.html',{'card':produtos})

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