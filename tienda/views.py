from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto
# from cart.forms import CartAddProductForm


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
    # cart_product_form = CartAddProductForm()
    return render(request,
                'tienda/producto/detalles.html',
                {'producto': producto})

# ,
# 'cart_product_form': cart_product_form