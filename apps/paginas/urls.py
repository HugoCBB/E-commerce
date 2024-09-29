from django.urls import path
from .views import home, produtos, deletar_produtos, editar_produtos

urlpatterns = [
    path('', home, name='home'),
    path('produtos/<int:produto_id>', produtos, name='produtos'),
    path('editar-produto/<int:produto_id>', editar_produtos, name='editar-produto'),
    path('deletar-produto/<int:produto_id>', deletar_produtos, name='deletar-produto'),
]