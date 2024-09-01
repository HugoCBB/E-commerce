from django.urls import path
from .views import home, produtos

urlpatterns = [
    path('', home, name='home'),
    path('produtos/', produtos, name='produtos'),
]