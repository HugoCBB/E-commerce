from django.contrib import admin
from . models import categoria, produtos
# Register your models here.
admin.site.register(produtos)
admin.site.register(categoria)