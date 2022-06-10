import graphene
from store.models import Producto, Producto_store, Category, Store
from .types import *

##################################
####  CAtegory Mutation ##########
##################################

class CreateCategoryMutation(graphene.Mutation):
  class Input:
    nombre = graphene.String()
    
  name = graphene.Field(CategoryType)
  
  @staticmethod
  def mutate(root, info, **kwargs):
    nombre = kwargs.get('nombre', '').strip()
    obj = Category.objects.create(nombre=nombre)
    return CreateCategoryMutation(name=obj)


###################################
##### Producto mutation ###########
###################################

class CreateProductoMutation(graphene.Mutation):
    class Input(object):
        nombre = graphene.String()
        descripcion = graphene.String()
        codigo = graphene.Int()
        category = graphene.Int()
        
    name = graphene.Field(ProductoType)
    
    @staticmethod
    def mutate(root, info, **kwargs):
        nombre = kwargs.get('nombre', '').strip()
        codigo = kwargs.get('codigo')
        descripcion= kwargs.get('descripcion','')
        category= kwargs.get('category')
        obj = Producto.objects.create(nombre=nombre, codigo=codigo, descripcion=descripcion, category=category)
        return CreateProductoMutation(name=obj)
    
    
#############################
####  Store Mutation ########
#############################

class CreateStoreMutation(graphene.Mutation):
    class Input(object):
        nombre = graphene.String()
        
    name= graphene.Field(StoreType)
    
    @staticmethod
    def mutate(root, info, **kwargs):
        nombre= kwargs.get('nombre','').strip()
        obj = Store.objects.create(nombre=nombre)
        return CreateStoreMutation(name=obj)
    
#########################
####  Mutations #########
#########################

class Mutation(graphene.AbstractType):
    create_category = CreateCategoryMutation.Field()
    create_producto = CreateProductoMutation.Field()
    create_store  =  CreateStoreMutation.Field()
