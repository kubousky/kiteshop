from django.shortcuts import render
from .models import PedidoArticulo
from .forms import FormularioDePedido
from cesta.cesta import Cesta
# from .tasks import order_created


def crear_pedido(request):
    cesta = Cesta(request) # sacamos de la session la cesta actual
    if request.method == 'POST':
        formulario = FormularioDePedido(request.POST)
        if formulario.is_valid():
            pedido = formulario.save() # creamos un pedido en la base de datos
            for articulo in cesta:
                PedidoArticulo.objects.create(pedido=pedido,
                                        producto=articulo['producto'],
                                        precio=articulo['precio'],
                                        cantidad=articulo['cantidad'])
            # clear the cart
            cesta.vaciar()
            # launch asynchronous task
            # order_created.delay(order.id)
            return render(request,
                        'pedidos/pedido/creado.html',
                        {'pedido': pedido})
    else:
        formulario = FormularioDePedido()
    return render(request,
                'pedidos/pedido/crear.html',
                {'cesta': cesta, 'formulario': formulario})