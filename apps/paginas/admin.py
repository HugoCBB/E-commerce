from django.contrib import admin
from . models import categoria, Produto
# Register your models here.
admin.site.register(Produto)
admin.site.register(categoria)