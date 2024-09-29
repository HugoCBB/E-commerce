from django.urls import path
from . views import AdicionarProduto
urlpatterns = [
    path('novo-produto', AdicionarProduto, name='novo-produto')

]
