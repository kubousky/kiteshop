from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from tienda.models import Producto
from .cesta import Cesta
from .forms import AnadirProductoCestaFormulario


@require_POST # solo permite las requests tipo POST
def cesta_anadir(request, producto_id):
    """
    Añadir producto en la cesta o actualizar cantidad de productos existentes
    """
    cesta = Cesta(request)
    producto = get_object_or_404(Producto, id=producto_id)
    formulario = AnadirProductoCestaFormulario(request.POST) # hereda de clase Form
    # el objeto Form tiene un metodo is_valid: 
    # comprueba si los datos introducidos son validos -> devuelve True
    # guarda los datos en un atributo "cleaned_data"
    if formulario.is_valid():
        cd = formulario.cleaned_data
        cesta.anadir(producto=producto,
                    cantidad=cd['cantidad'],
                    actualizar_cantidad=cd['actualizacion'])
    return redirect('cesta:cesta_detalles')


def cesta_eliminar(request, producto_id):
    cesta = Cesta(request) # sacamos la cesta actual
    producto = get_object_or_404(Producto, id=producto_id)
    cesta.eliminar(producto)
    return redirect('cesta:cesta_detalles')


def cesta_detalles(request):
    cesta = Cesta(request)
    for articulo in cesta:
            # creamos un formulario para actualizar la cantidad y lo añadimos al diccionario
            articulo['actualizar_cantidad_formulario'] = AnadirProductoCestaFormulario(initial={'cantidad': articulo['cantidad'], 'actualizacion': True})
    return render(request, 'cesta/detalles.html', {'cesta': cesta})