from django.urls import path
from . views import AdicionarProduto, manager
urlpatterns = [
    path('', manager, name='manager'),
    path('novo-produto', AdicionarProduto, name='novo-produto')

]
