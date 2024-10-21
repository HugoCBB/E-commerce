from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class categoria(models.Model):
    data = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome


class Produto(models.Model):

    COLECOES = [
        ("CALÇA","Calça"),
        ("BLUSA","Blusa"),
        ("SHORT","Short"),
    ]
    data = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=450, null=False, blank=False)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    # categorias = models.ForeignKey(categoria, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=150, choices=COLECOES, default='')
    publicada = models.BooleanField(default=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)


    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False
        )


    def __str__(self):
        return self.nome

