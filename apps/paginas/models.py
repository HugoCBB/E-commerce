from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class categoria(models.Model):
    data = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

# class Produtos(models.Model):
#     data = models.DateField(auto_now_add=True)
#     nome = models.CharField(max_length=250)
#     descricao = models.CharField(max_length=450, null=False, blank=False)
#     preco = models.IntegerField()
#     categorias = models.ForeignKey(categoria, on_delete=models.CASCADE)
#     publicada = models.BooleanField(default=False)

#     usuario = models.ForeignKey(
#         to=User,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=False
#         )


#     def __str__(self):
#         return self.nome
class Produto(models.Model):
    data = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=450, null=False, blank=False)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categorias = models.ForeignKey(categoria, on_delete=models.CASCADE)
    publicada = models.BooleanField(default=False)

    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False
        )


    def __str__(self):
        return self.nome

