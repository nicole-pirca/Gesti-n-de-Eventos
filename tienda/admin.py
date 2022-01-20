from django.contrib import admin
from django.http import request

from .models import CategoriaProd, Producto


class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fiels =("created", "updated")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fiels =("created", "updated")


admin.site.register(CategoriaProd, CategoriaProdAdmin)

admin.site.register(Producto, ProductoAdmin)