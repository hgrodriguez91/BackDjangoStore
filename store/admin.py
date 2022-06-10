from django.contrib import admin
from store.models import Producto, Producto_store, Category, Store

# Register your models here.

admin.site.register(Producto)
admin.site.register(Producto_store)
admin.site.register(Category)
admin.site.register(Store)

