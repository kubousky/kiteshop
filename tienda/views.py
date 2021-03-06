from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto
from cesta.forms import AnadirProductoCestaFormulario


def producto_lista(request, categoria_slug=None):
    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(disponible=True)
    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        productos = productos.filter(categoria=categoria)
    return render(request,
                'tienda/producto/lista.html',
                {'categoria': categoria,
                'categorias': categorias,
                'productos': productos})


def producto_detalles(request, id, slug): # podemos sacar de la bbdd la instancia solo con id pero usando tambien 'slug' en el url 
    producto = get_object_or_404(Producto,   # hacemos que sea más "SEO-fiendly"
                                id=id,
                                slug=slug,
                                disponible=True)
    cesta_producto_formulario = AnadirProductoCestaFormulario()
    return render(request,
                'tienda/producto/detalles.html',
                {'producto': producto,
                'cesta_producto_formulario': cesta_producto_formulario})

