from django.urls import path
from . views import login, cadastrar

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastrar, name='cadastro')
]