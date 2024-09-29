from django.shortcuts import render, redirect
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from .forms import ProdutoForm

# Create your views here.

@has_permission_decorator('adicionar_produtos')
def AdicionarProduto(request):
    form = ProdutoForm()
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'manager/forms.html', {'form':form})
