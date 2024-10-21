from django.urls import path
from . views import AdicionarProduto, manager, ExibirProdutos, editar_produtos, deletar_produtos

urlpatterns = [
    path('', manager, name='manager'),
    path('novo-produto', AdicionarProduto, name='novo-produto'),
    path('exbir-produtos', ExibirProdutos, name='exibir-produto'),
    path('editar-produto/<int:produto_id>', editar_produtos, name='editar-produto'),
    path('deletar-produto/<int:produto_id>', deletar_produtos, name='deletar-produto'),


]
