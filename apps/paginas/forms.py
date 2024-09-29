from django.forms import forms
from .models import Produto

class ProdutoForm(forms.Form):
    class META:
        model = Produto
        fields = []