from django.urls import path
from . views import login, cadastrar, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastrar, name='cadastro'),
    path('logout/', logout, name='logout')
]