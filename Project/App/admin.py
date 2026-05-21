from django.contrib import admin
from .models import Categoria, Productos, FunkoPop


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('CodigoCategoria', 'Nombre')


@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('Codigo', 'Nombre', 'Precio', 'Stock', 'Categoria')
    list_filter = ('Categoria',)

  
@admin.register(FunkoPop)
class FunkoPopAdmin(admin.ModelAdmin):
    list_display = ('CodigoFunko', 'Nombre', 'SerieAnime', 'Personaje', 'Precio', 'Stock')
    search_fields = ('Nombre', 'SerieAnime', 'Personaje')
    list_filter = ('SerieAnime',)  

