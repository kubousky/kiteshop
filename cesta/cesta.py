from decimal import Decimal
from django.conf import settings
from tienda.models import Producto


class Cesta(object):

    def __init__(self, request):
        """
        Iniciar la nueva cesta
        """
        self.session = request.session # usamos request.session para acceder a la sesion actual
        # se comporta como un diccionario de Python
        cesta = self.session.get(settings.CESTA_SESION_ID)
        if not cesta:
            # guardamos la cesta vacía en la sesión 
            cesta = self.session[settings.CESTA_SESION_ID] = {} # {'cesta': {}}
            # la llave del diccionario: ID de producto; los valores: cantidad y precio.
        self.cesta = cesta # {}

    def __iter__(self):
        """
        Iterar sobre los elementos en la cesta y sacar los productos de la base de datos
        """
        producto_ids = self.cesta.keys()
        # sacar objetos Producto y añadirlos en la carta
        productos = Producto.objects.filter(id__in=producto_ids)

        cesta = self.cesta.copy()
        for producto in productos:
            cesta[str(producto.id)]['producto'] = producto # -> {"id": {'cantidad': 2, "precio": 20, "producto": producto}}

        for v in cesta.values():
            v['precio'] = Decimal(v['precio'])
            v['precio_total'] = v['precio'] * v['cantidad']
            yield v  # {"id": {'cantidad': 2, "precio": 20, "producto": producto, 'precio_total': 40}}
    
    def __len__(self):
        """
        Contar elementos en la cesta
        """
        return sum(v['cantidad'] for v in self.cesta.values())

    def anadir(self, producto, cantidad=1, actualizar_cantidad=False):
        """
        Añadir un producto a la cesta o actualizar su cantidad
        """
        producto_id = str(producto.id)
        if producto_id not in self.cesta:
            self.cesta[producto_id] = {'cantidad': 0,
                                         'precio': str(producto.precio)}
        if actualizar_cantidad:
            self.cesta[producto_id]['cantidad'] = cantidad
        else:
            self.cesta[producto_id]['cantidad'] += cantidad
        self.guardar()

    def guardar(self):
        # marcamos el atributo "modified" de objeto "sesion" como True. 
        # Eso dice a Django que la sesion ha sido modificada y hay que guardarla.
        self.session.modified = True

    def eliminar(self, producto):
        """
        Eliminar producto de la cesta
        """
        producto_id = str(producto.id)
        if producto_id in self.cesta:
            del self.cesta[producto_id]
            self.guardar()

    def calcula_precio_total(self):
        return sum(Decimal(v['precio']) * v['cantidad'] for v in self.cesta.values())

    def vaciar(self):
        # remove cart from session
        # eliminar cesta de la sesion
        del self.session[settings.CESTA_SESION_ID]
        self.guardar()
