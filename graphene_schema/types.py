from dataclasses import fields
import graphene
from graphene_django.types import DjangoObjectType
from store.models import Producto, Producto_store, Category, Store


class ProductoType(DjangoObjectType):
    class Meta:
        model = Producto
        fields = ('id','nombre','descripcion','category')

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id','nombre')
        
class StoreType(DjangoObjectType):
    class Meta:
        model = Store
        fields = ('id','nombre')
        
class ProductosStoreType(DjangoObjectType):
    class Meta:
        model = Producto_store
        fields = ('id','producto_id','store_id','precio','created_at') 
        
class Query(object):
    
    #producto
    producto = graphene.Field(ProductoType, id = graphene.Int(), nombre= graphene.String())
    all_productos = graphene.List(ProductoType)
    
    def resolve_all_productos(self, info,**kwargs):
        return Producto.objects.select_related('category').all()
    
    def resolve_producto(self, info, **kwargs):
        id = kwargs.get('id')
        nombre = kwargs.get('nombre')
        category = kwargs.get('category')
        if id is not None:
            return Producto.objects.select_related('category').get(pk=id)
        if nombre is not None:
            return Producto.objects.select_related('category').get(nombre=nombre)
        if category is not None:
            return Producto.objects.select_related('category').get(category=category)
        return None
    
    #Category
    all_categories = graphene.List(CategoryType)
    
    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()
    
    #Store
    all_store = graphene.List(StoreType)
    
    def resolve_all_store(self, info, **kwargs):
        return Store.objects.all()
    
    #Store_productos
    #all_store_products = graphene.List(Producto_store,store_id= graphene.Int())
    
    """ def resolve_all_store_products(self, info, **kwargs):
        store_id = kwargs.get('store_id')
        if store_id is not None:
            return Producto_store.objects.all()
        return None """