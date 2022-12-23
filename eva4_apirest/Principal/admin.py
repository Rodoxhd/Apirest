from django.contrib import admin
from .models import Producto, TipoProd

class ProductoAdmin(admin.ModelAdmin):
    list_display=["nombre", "precio", "laboratorio", "tipo"]
    list_per_page= 10

admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoProd)