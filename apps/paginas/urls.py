from django.urls import path
from .views import home, produtos

urlpatterns = [
    path('', home, name='home'),
    path('produtos/<int:produto_id>', produtos, name='produtos'),
]