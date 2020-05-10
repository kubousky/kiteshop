from django.contrib import admin
from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaLadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}


@admin.register(Producto)
class ProductoLadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug', 'precio',
                    'disponible', 'creado', 'actualizado']
    list_filter = ['disponible', 'creado', 'actualizado']
    list_editable = ['precio', 'disponible']
    prepopulated_fields = {'slug': ('nombre',)} # para que los slugs se crean automaticamente