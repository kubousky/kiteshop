from django.db import models
from tienda.models import Producto


class Pedido(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    direccion = models.CharField(max_length=250)
    codigo_postal = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    pagado = models.BooleanField(default=False)

    class Meta:
        ordering = ('-creado',)

    def __str__(self):
        return 'Pedido {}'.format(self.id)

    def calcular_precio_total(self):
        return sum(articulo.calcula_coste() for articulo in self.articulos.all())


class PedidoArticulo(models.Model):
    pedido = models.ForeignKey(Pedido,
                            related_name='articulos',
                            on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,
                                related_name='pedido_articulos',
                                on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def calcula_coste(self):
        return self.precio * self.cantidad

