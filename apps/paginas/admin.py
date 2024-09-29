from django.contrib import admin
from . models import categoria, Produto
# Register your models here.
# class ListandoProduto(admin.ModelAdmin):
#     list_editable = ('publicada',) 

admin.site.register(Produto)
admin.site.register(categoria)